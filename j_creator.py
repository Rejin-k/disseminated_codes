import json

with open('data.json', 'r+') as f:
    data_json = json.load(f)
    new_id = "Date_of_birth"
    value1 = "00_00_00"
    f.seek(0)
    index=0
    for c_name in data_json:
        print c_name
        for value in c_name:
            if value=="Data":
                data_json[index][value][new_id] = value1
                index=index+1
                # print(data_json)
    json.dump(data_json, f, indent=4)
    f.truncate()