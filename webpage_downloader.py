# python
import os
import urllib.request
import urllib.error


def download_webpage(url, output_dir):
    """
    Downloads the HTML content of a webpage and saves it locally for offline access.
    """
    if not url.startswith("http://") and not url.startswith("https://"):
        raise ValueError("url must start with 'http://' or 'https://'.")

    if not os.path.exists(output_dir):
        # create output directory if it doesn't exist
        os.makedirs(output_dir)

    # generate a valid filename from the URL
    filename = url.split("//")[-1].replace("/", "_").replace(":", "_") + ".html"
    file_path = os.path.join(output_dir, filename)

    # set up a request with a User-Agent header
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)

    # fetch the webpage content
    try:
        print(f"fetching webpage: {url}")
        response = urllib.request.urlopen(req)
        content = response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"failed to fetch the webpage: {e}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"failed to reach the server: {e}")

    # save the content to a local file
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"webpage saved as: {file_path}")
    except Exception as e:
        raise RuntimeError(f"failed to save the webpage: {e}")


if __name__ == "__main__":
    print("welcome to the website content downloader!")
    url = input("enter the URL of the webpage to download: ").strip()
    output_dir = input(
        "enter the directory to save the webpage (default: current directory): "
    ).strip()

    if not output_dir:
        # default to current directory
        output_dir = "."

    try:
        download_webpage(url, output_dir)
    except Exception as e:
        print(f"error: {e}")
