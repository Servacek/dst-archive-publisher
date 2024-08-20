# Don't Starve Together World Archive Publisher
Webhook script for publishing Don't Starve Together world backups to Discord.

![image](https://github.com/user-attachments/assets/e4d9755d-125f-4181-8178-78f64d35006a)

## Dependencies
- Python 3+
- `requests` library

## Environment Variables
| Name  | Description | Optional |
| ------------- | ------------- | ------------- |
| WEBHOOK_URL  | The full discord URL of your desired webhook in a forum channel | False
| SAVE_NAME  | The name of the world backup to display as a title of the thread. | True
| SAVE_DESCRIPTION | The description of the world backup displayed as the thread's initial message content. | True
| MANUAL_URL | An discord url link to the message containing a manual for loading backups on clients. |True
| SAVE_SHARDS | A list of shards this backup contains worlds for. | True

You can use the run.* files if you want to store these environment variables to a separate file.

## Setup
Add your desired backup to the `saves` directory and run `python main.py` from inside the root directory.
It is especially useful when you already have some backup system setuped.

![image](https://github.com/user-attachments/assets/05fedf43-9493-4680-9ffb-25845f91c3ee)
*Photos from the [[CZ/SK] Don't Starve](https://discord.gg/RHzJxut) community Discord where this webhook is currently being used for uploading backups automatically and in style B)*
