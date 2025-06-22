import json
import os
import requests

class CareerGuideGenerator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url_text_generation = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key="
        self.headers = {'Content-Type': 'application/json'}

    def _call_gemini_api(self, prompt: str) -> str:
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}]
                }
            ]
        }

        full_api_url = f"{self.api_url_text_generation}{self.api_key}"

        try:
            response = requests.post(full_api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            result = response.json()

            if result.get("candidates") and len(result["candidates"]) > 0 and \
               result["candidates"][0].get("content") and \
               result["candidates"][0]["content"].get("parts") and \
               len(result["candidates"][0]["content"]["parts"]) > 0:
                return result["candidates"][0]["content"]["parts"][0]["text"]
            else:
                error_detail = result.get('error', {}).get('message', 'No specific error message.')
                raise Exception(f"Unexpected API response structure or error: {error_detail}. Full response: {json.dumps(result)}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network or API request error: {e}. Please check your internet connection and API key.")
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to decode JSON response from API: {e}. Response text: {response.text if 'response' in locals() else 'No response'}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred during API call: {e}")

    def get_career_guidance(self, user_profile: str, study_level: str) -> str:
        prompt = (f"As an expert career counselor for Pakistani students who have completed {study_level} or equivalent, "
                  f"provide personalized guidance based on the following profile:\n\n"
                  f"{user_profile}\n\n"
                  "Please suggest suitable Bachelor's degrees commonly offered in Pakistani universities, "
                  "potential career paths associated with those degrees within the Pakistani job market context, "
                  "and highlight key skills (both technical and soft) required. "
                  "Provide a comprehensive, encouraging, and clear response. "
                  "Focus on practical advice relevant to Pakistan's educational and employment landscape.")
        return self._call_gemini_api(prompt)
