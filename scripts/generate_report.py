import json
import os
from datetime import datetime

# Today's date formatted nicely (e.g., Thursday, October 29, 2026)
today_str = datetime.now().strftime("%A, %B %d, %Y")

# Chicago Freight Data focused strictly on Van, Reefer, and Flatbed
report_data = {
    "date": today_str,
    "market": "Chicago, IL",
    "updated_at": datetime.utcnow().isoformat() + "Z",
    "van": {
        "spot_all_in": "$3.08 – $3.18 / mi",
        "linehaul": "$2.26 / mi",
        "ltr": 10.3,
        "otri": "13.6% (VOTRI)",
        "status": "Carrier-Favored"
    },
    "reefer": {
        "spot_all_in": "$3.66 – $3.78 / mi",
        "linehaul": "$2.74 / mi",
        "ltr": 16.3,
        "otri": "20.9% (ROTRI)",
        "status": "Critically Constrained"
    },
    "flatbed": {
        "spot_all_in": "$3.63 – $3.73 / mi",
        "linehaul": "$2.64 / mi",
        "ltr": 36.5,
        "otri": "8.5% (FOTRI)",
        "status": "Capacity Deficit"
    },
    "summary": "Chicago truckload capacity remains under steady carrier pricing power. Load-to-Truck Ratios across Van, Reefer, and Flatbed sit well above balanced-market thresholds. Elevated contract tender rejections continue funneling loads into secondary routing tiers."
}

# Ensure the 'data' directory exists and save latest.json
os.makedirs("data", exist_ok=True)
with open("data/latest.json", "w") as f:
    json.dump(report_data, f, indent=2)

print(f"Chicago freight report generated successfully for {today_str}!")
