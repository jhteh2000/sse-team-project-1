import os
import requests

def test_edamam_api_status():
    edamam_api = (
        "https://api.edamam.com/api/recipes/v2/?type=public&app_id="
        + os.getenv("EDAMAM_APP_ID")
        + "&app_key="
        + os.getenv("EDAMAM_APP_KEY")
    )
    response = requests.get(edamam_api)
    assert response.status_code == 200