import csv

filename = 'ID.csv'  # CSV 파일의 경로와 이름

def readCsv(inputName):
    print(inputName)
    result = []

    with open("ID.csv", 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            value = row[0]  # 첫 번째 열의 값
            name = row[1]  # 두 번째 열의 값

            if name == inputName:
                print()
                result.append((int(float(value)), name))
                return value

    return "0"


