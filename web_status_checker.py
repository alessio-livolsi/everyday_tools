# python
import http.client
import urllib.parse
import time


def check_website_status(url):
    """
    Check the HTTP status of a given website and display information.
    Handles a single redirect if necessary.
    """
    # ensure the URL has a scheme, default to HTTP if missing
    if not url.startswith(("http://", "https://")):
        url = f"http://{url}"

    parsed_url = urllib.parse.urlparse(url)

    try:
        # measure response time
        start_time = time.time()

        # use HTTPS if the scheme is https, otherwise use HTTP
        connection = (
            http.client.HTTPSConnection
            if parsed_url.scheme == "https"
            else http.client.HTTPConnection
        )(parsed_url.netloc, timeout=10)

        connection.request("GET", parsed_url.path or "/")
        response = connection.getresponse()
        response_time = round((time.time() - start_time) * 1000, 2)

        # display the initial response
        print(f"\nURL: {url}")
        print(f"Status: {response.status} {response.reason}")
        print(f"Response Time: {response_time} ms")

        # display response headers
        print("\nHeaders:")
        for header, value in response.getheaders():
            print(f"  {header}: {value}")

        # handle a single redirect, if any
        if response.status in (301, 302):
            redirect_url = response.getheader("Location")
            print(f"\nRedirected to: {redirect_url}")

            # follow the redirect and check the final status
            if redirect_url:
                # parse the redirected URL
                parsed_redirect_url = urllib.parse.urlparse(redirect_url)
                connection.close()

                # establish a new connection based on the scheme of the redirected URL
                new_connection = (
                    http.client.HTTPSConnection
                    if parsed_redirect_url.scheme == "https"
                    else http.client.HTTPConnection
                )(parsed_redirect_url.netloc, timeout=10)

                # measure response time for the redirected URL
                start_time = time.time()
                new_connection.request("GET", parsed_redirect_url.path or "/")
                final_response = new_connection.getresponse()
                final_response_time = round((time.time() - start_time) * 1000, 2)

                # display the final response after redirection
                print(f"\nFinal URL: {redirect_url}")
                print(f"Final Status: {final_response.status} {final_response.reason}")
                print(f"Final Response Time: {final_response_time} ms")

                print("\nFinal Headers:")
                for header, value in final_response.getheaders():
                    print(f"  {header}: {value}")

                new_connection.close()

    except Exception as e:
        print(f"\nError checking {url}: {e}")
    finally:
        connection.close()


def main():
    """Main function to prompt user for URLs and check their status."""
    print("Web Status Checker")
    while True:
        url = input("\nEnter the URL to check (or type 'q' to quit): ").strip()
        if url.lower() == "q":
            break
        if url:
            check_website_status(url)


if __name__ == "__main__":
    main()
