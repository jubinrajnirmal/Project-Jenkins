from datetime import datetime

def read_version():
        return "V1.0"

def display_date_time_and_version():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    version = read_version()
    print(f"Current Date and Time: {current_time}")
    print(f"Version: {version}")

if __name__ == "__main__":
    display_date_time_and_version()