database = [(1,'Nishant'),(2,'Swayam')]

name = input("Enter Name: ")
id = int(input("Enter id: "))

box = (id,name)

def knowledgeBase(total):
    percentage = ((total)/50)*100
    return percentage

if box in database:
    com = -1
    while com < 0 or com > 10 :
        com = int(input("Enter Communication skills:(0 to 10)"))
    
    tech = -1
    while tech < 0 or tech > 10:
        tech = int(input("Enter technical skill: "))
    
    manage = -1
    while manage < 0 or manage > 10:
        manage = int(input("Enter management skill: "))

    soft = -1
    while soft < 0 or soft > 10:
        soft = int(input("Enter other softskills: "))

    att = -1
    while att < 0 or att > 10:
        att = int(input("Enter other Attendence: "))
    
    total = com + tech + manage + soft + att
    percentage = knowledgeBase(total)

    if percentage < 20:
        print("poor performance")
    elif percentage < 50:
        print("Performance could be better")
    elif percentage < 80:
        print("Good Overall performacne")
    else:
        print("Excellent performance")
else:
    print("Employee Not in database! Please Search again! ")