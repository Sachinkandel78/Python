import subprocess

try:
    profiles = subprocess.check_output(
        "netsh wlan show profiles",
        shell=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    print("Saved Wi-Fi Profiles")
    print("-" * 30)

    wifi_names = []

    for line in profiles.splitlines():
        if "All User Profile" in line:
            name = line.split(":")[1].strip()
            wifi_names.append(name)

    if wifi_names:
        for i, name in enumerate(wifi_names, start=1):
            print(f"{i}. {name}")
    else:
        print("No Wi-Fi profiles found.")

except subprocess.CalledProcessError:
    print("Unable to retrieve Wi-Fi profiles.")