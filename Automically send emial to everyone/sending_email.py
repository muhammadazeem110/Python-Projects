letter = open("starting_letter.docx", mode="r")
names = open("invited_name.txt")

letter_content = letter.read()
name_content = names.readlines()

placeholder = "[name]"

for quest in name_content:
    stripped_name = quest.strip()
    new_letter = letter_content.replace(placeholder, stripped_name)

    # print(new_letter)
    send = open(f"../2.Pratice/ReadyToSend//letter for {stripped_name}.txt", mode="w")
    send.write(new_letter)


letter.close()
names.close()
send.close()
