def delete(line):
    lines = open('file.txt', 'r')
    phone = lines.readline()
    for i in range(len(phone)):
        if line in phone[i]:
            phone[i] = ""
    with open('file.txt', 'w') as file:
        file.writelines(phone)
    print('Выбранный контакт удален!')
