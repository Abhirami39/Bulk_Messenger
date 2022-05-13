import pywhatkit
import time
import csv

f = open("C:\\doctor_loans\\content_test.txt", encoding="utf8")

with open('C:\\doctor_loans\\contacts_model.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row is None:
            break
        if line_count == 0:
            line_count += 1
            continue
        else:
            # print(f'\t{row[0]} the number of this person is {row[1]}.')
            line_count += 1

            # phone_number = row[1].strip()
            # name = row[0].strip()
            real_no = '+91'+row[1]
        pywhatkit.sendwhatmsg_instantly(real_no, "Greetings Dr. " + "*" + row[0] + "*" + " *Garu* \n" + f.read(), 20,
                                        True, 30)

        f.seek(0)

        # time.sleep(30)

    csv_file.seek(0)
    line_count = 0

f.close()
