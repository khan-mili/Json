from functions import createFile, addInfo, clearFileInfo, readFile 

# Creating initial data for the JSON file
init = {
    "name": "Person name",
    "age": 30,
    "city": "Vantaa"
}

# Call the function to create JSON file with initial data
createFile(init)

# Adding more data to JSON file
new_data = {
    "occupation": "Engineer",
    "salary": 50000
}

addInfo(new_data)

# Reading JSON file
readFile()

# Clearing JSON file ---***
# clearFileInfo()


