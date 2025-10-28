import requests
import time

def check_website_status(url: str, timeout: int = 5) -> None:
    """
    Check if a website is online and measure response time.
    """
    try:
        start_time = time.time()
        response = requests.get(url, timeout=timeout)
        elapsed = round(time.time() - start_time, 3)

        if response.status_code == 200:
            print(f" {url} is ONLINE | Response Time: {elapsed}s")
        else:
            print(f" {url} responded with status code {response.status_code}")

    except requests.exceptions.ConnectionError:
        print(f" {url} is OFFLINE (Connection Error)")
    except requests.exceptions.Timeout:
        print(f" {url} timed out after {timeout} seconds")
    except Exception as e:
        print(f" Error checking {url}: {e}")


if __name__ == "__main__":
    url = input("Enter website URL (e.g. https://example.com): ").strip()
    if not url.startswith("http"):
        url = "https://" + url
    check_website_status(url)
