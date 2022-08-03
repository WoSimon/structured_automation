import json, os, datetime, platform, glob, shutil

search_dir = "/Users/SimonWosnitza/Library/Mobile Documents/iCloud~com~leomehlig~today/Documents/Backups"
filenames = glob.glob(search_dir + "/*.backup")
dictionary = {}


def get_file_creation_time(filename):
    return datetime.datetime.fromtimestamp(os.stat(filename).st_birthtime)


for file in filenames:
    # Get the creation time of the file
    creation_time = get_file_creation_time(file)
    # Create a new key in the dictionary with the creation time as key
    dictionary[file] = creation_time

# Sort the dictionary by the creation time
sorted_dictionary = sorted(dictionary.items(), key=lambda kv: kv[1])

# Get last backup
last_backup = sorted_dictionary[-1][0]
print("Last Backup: " + last_backup)

# Open the JSON file
json_file = open(last_backup, "r")

# Load the JSON object into the variable data
data = json.load(json_file)

# cd_day: 19200 ist 27.07.2022
reference_date = datetime.datetime(2022, 7, 27)
today_date = datetime.datetime.now()
weekday_str = today_date.strftime("%A").lower()

# Calculate the difference between the reference date and the current date
difference = today_date - reference_date
today = 19200 + difference.days
print(today)


def extract_tasks(data):
    for task in data['content']['tasks']:
        if task['cd_day'] == today:
            # Stat von float zu Zeit formatieren
            start_hour = int(task['start'])
            start_minute = int((task['start'] - start_hour) * 60)
            start_time = f"{start_hour:02d}:{start_minute:02d}"

            # Endezeit ausrechnen (Startzeit + Dauer)
            length_hrs, length_mins = divmod(task['duration'], 60)
            end_hrs = start_hour + length_hrs
            end_mins = start_minute + length_mins
            end_time = f"{end_hrs:02d}:{end_mins:02d}"

            print(task['title'] + ", " + "Von: " + start_time + " bis: " + end_time + " (Dauer: " + str(
                task['duration']) + " min)")


extract_tasks(data)

##############################################################################
# if 'cd_day' in task.keys():
# print(str(task['cd_day']) + " : " + task['title'])
# else:
# print("- : " + task['title'])
# print(task.keys())
