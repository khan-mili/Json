import json

def createFile(data):
    try:
        with open("info.json", "w") as jsonFile:
            json.dump(data, jsonFile, indent=4)
        print("JSON file created successfully.")
    except Exception as e:
        print(f"Error occurred while creating JSON file: {e}")


def addInfo(data):
    try:
        with open("info.json", "r+") as jsonFile:
            file_data = json.load(jsonFile)
            file_data.update(data)
            jsonFile.seek(0)
            json.dump(file_data, jsonFile, indent=4)
        print("Data added to JSON file successfully.")
    except Exception as e:
        print(f"Error occurred while adding data to JSON file: {e}")


def clearFileInfo():
    try:
        with open("info.json", "w") as jsonFile:
            jsonFile.write("")
        print("JSON file cleared successfully.")
    except Exception as e:
        print(f"Error occurred while clearing JSON file: {e}")


def readFile():
    try:
        with open("info.json", "r") as jsonFile:
            data = json.load(jsonFile)
            print("Data in JSON file:")
            print(data)
    except FileNotFoundError:
        print("JSON file not found.")
    except Exception as e:
        print(f"Error occurred while reading JSON file: {e}")
