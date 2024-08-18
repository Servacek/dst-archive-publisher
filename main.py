import requests
import os

SAVES_FOLDER = "saves"
VERSION_FILE_PATH = "version.txt"

# CONFIG

# Get the token from an environment variable
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
SAVE_NAME = os.environ.get("SAVE_NAME")
SAVE_DESCRIPTION = os.environ.get("SAVE_DESCRIPTION")
MANUAL_URL = os.environ.get("MANUAL_URL")
# Should be already formatted the way you want it to be displayed.
SAVE_SHARDS = os.environ.get("SAVE_SHARDS")

###########

version = 1
if os.path.exists(VERSION_FILE_PATH):
    with open(VERSION_FILE_PATH, "r") as version_file:
        version = int(version_file.read() or 0)

# Create a dictionary with the webhook content
payload = {
    "content": (
        SAVE_DESCRIPTION if SAVE_DESCRIPTION else "## Záloha " +
        (f"pre shard(y) {SAVE_SHARDS}" if SAVE_SHARDS else "Servera")
    ) + (f"\n> [Návod na inštaláciu.]({MANUAL_URL})" if MANUAL_URL else ""),
    "thread_name": SAVE_NAME if SAVE_NAME else f"Záloha Komunitného Servera #{version}",
}

filename = None
for file in os.listdir(SAVES_FOLDER):
    if file.endswith(".zip"):
        filename = file

if filename is None:
    raise FileNotFoundError

print("Found save file: " + filename)

# Open and send the ZIP file
savefilepath = SAVES_FOLDER + "/" + filename
with open(savefilepath, "rb") as f:
    print("Sending it to discord...")

    files = {"file": (filename, f)}
    response = requests.post(WEBHOOK_URL,
        data=payload,
        files=files,
        params={ "wait": True }
    )

# Check the response status (optional)
if response.ok:
    print(f"[{response.status_code}] ZIP file sent successfully!")
    version += 1
    with open("version.txt", "w") as version_file:
        version_file.write(str(version))
else:
    print(f"[Error] [{response.status_code}]  Failed to send ZIP file. Reason: {response.reason} Body: {response.text}")
    exit(1)
