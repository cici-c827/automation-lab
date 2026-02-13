import requests
import time
from writer import generate_proposal

REMOTEOK_API = "https://remoteok.com/api"


KEYWORDS = [
    "python",
    "automation",
    "data",
    "ai",
    "engineer",
    "developer"
]


def fetch_jobs():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(REMOTEOK_API, headers=headers, timeout=30)
    return r.json()


def match_job(job):
    text = (job.get("position", "") + job.get("description", "")).lower()
    return any(k in text for k in KEYWORDS)


def main_loop():
    print("MoneyAgent scanning real remote jobs...\n")

    while True:
        try:
            jobs = fetch_jobs()

            total = len(jobs)
            matched = 0

            for job in jobs:
                if not isinstance(job, dict):
                    continue

                if not match_job(job):
                    continue

                matched += 1

                title = job.get("position", "Unknown Role")
                url = job.get("url", "No URL")

                print("MATCH :", title)
                print("APPLY :", url)
                print("-" * 60)

                generate_proposal(title, url)

            print(f"\nTotal jobs: {total} | Matched: {matched}")
            print("Sleeping 30 minutes before next scan...\n")

            time.sleep(1800)

        except Exception as e:
            print("Loop error:", e)
            time.sleep(60)


if __name__ == "__main__":
    main_loop()
