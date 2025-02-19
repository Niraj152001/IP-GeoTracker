import requests
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

# Replace with your actual API key
API_KEY = "your_api_key_here"
BASE_URL = "https://api.ip2location.io/"

def get_ip_info(ip):
    params = {
        "key": API_KEY,
        "ip": ip,
        "format": "json"
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        
        if response.status_code != 200:
            return {"Error": f"HTTP Error {response.status_code}"}
        
        data = response.json()  
        
        if "ip" in data:
            result = {
                "IP Address": data.get("ip"),
                "Country": data.get("country_name"),
                "Region": data.get("region_name"),
                "City": data.get("city_name"),
                "Latitude": data.get("latitude"),
                "Longitude": data.get("longitude"),
                "ISP": data.get("isp"),
                "ISP Domain": data.get("domain"),
                "ASN (Autonomous System Number)": data.get("asn"),
                "Connection Type": "Mobile Data" if data.get("mobile_carrier") else "Wi-Fi/Ethernet",
                "Mobile Carrier": data.get("mobile_carrier"),
                "Proxy": "Yes" if data.get("is_proxy") else "No",
                "VPN": "Yes" if data.get("is_vpn") else "No",
                "TOR": "Yes" if data.get("is_tor") else "No",
            }
            
            # Remove empty fields
            return {key: value for key, value in result.items() if value}
        else:
            return {"Error": "Invalid response from API"}
    
    except requests.exceptions.RequestException as e:
        return {"Error": f"Request failed: {str(e)}"}
    except ValueError:
        return {"Error": "Invalid JSON response from API"}

def print_colored_result(result):
    print(f"\n{Fore.CYAN}--- IP Information ---{Style.RESET_ALL}")
    
    if "Error" in result:
        print(f"{Fore.RED}Error: {result['Error']}{Style.RESET_ALL}")
    else:
        latitude = result.get("Latitude")
        longitude = result.get("Longitude")

        for key, value in result.items():
            color = Fore.GREEN if key in ["IP Address", "ISP", "Connection Type"] else Fore.YELLOW
            print(f"{color}{key}: {Fore.WHITE}{value}{Style.RESET_ALL}")

        # Print Google Maps link instead of opening it
        if latitude and longitude:
            maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
            print(f"\n{Fore.BLUE}Google Maps Location: {Fore.WHITE}{maps_url}{Style.RESET_ALL}\n")

if __name__ == "__main__":
    while True:
        ip_address = input(f"{Fore.CYAN}Enter an IP address (or type 'exit' to quit): {Style.RESET_ALL}").strip()
        
        if ip_address.lower() == "exit":
            print(f"{Fore.RED}Exiting...{Style.RESET_ALL}")
            break

        result = get_ip_info(ip_address)
        print_colored_result(result)
