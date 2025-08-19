# A simple contact book program to add, view, remove, search and update contacts.
# It uses a text file to store the contacts and performs operations based on user input.
# before running this code, make sure to create a 'Contacts.txt' file in the 'project' directory.

print('\n      Contact Book Menu\n\
1.Add contact \n\
2.View all contacts\n\
3.Remove a contact\n\
4.Search a contact\n\
5.Update a contact')   
        
def Email():
    '''Function to validate email address.'''
    # It checks if the email ends with '@gmail.com'.
    while True:          
        email = input('valid email id: ')
        if email[-10:] != '@gmail.com':
            print('--Give a valid email id')
            continue
        return email
    
def Phone():
    '''Function to validate phone number.'''
    # It checks if the phone number is a 10-digit integer.
    while True:
        try:
            phone = int(input('Phone no(10 digit): '))
            if len(str(phone)) != 10: #len works on str
                print('--It does not have 10 digits!')
                continue  
            return phone  #var defined in a certain lvl of indentation, their value can be
        except ValueError: #accessed in that/furthur(nested)lvl indentation only.??
            print('--give a valid phone no!') #only 'return' can be used 
                               #to use the value outside a func.
def Add(First,End): 
    '''Function to add a new contact.'''
    # It takes first and last name as input, validates phone number and email,
    No,Em = Phone(),Email()  #both func can be written side by side.
          #unpacking only defined for iterable obj and use to store data in 1 line??                 
    with open('project/Contacts.txt','a') as f:
        f.write(f'\nName--{First.strip()} {End}\nPhone--{No}\nEmail--{Em}\n')
    print('--New contact added\n') #in write,'a' mode anything written will be added in a single line.

def View():
    '''Function to view all contacts.'''
    # It reads the contacts from the text file and prints them.
    with open('project/Contacts.txt') as f:
        Read = f.read() #local variables(after being defined inside a block of code) 
        print(Read)     #can work/accessed only inside that block.??

with open('project/Contacts.txt') as f:
        lines = f.readlines() #global var can be used anywhere, in/out block of code.

def Remove():
    '''Function to remove a contact.'''
    # It takes first and last name as input, searches for the contact in the text file,
    # and removes the contact if found.
    # If not found, it prompts the user to continue or exit.
    while True:
        First = input('First name: ').upper().strip()
        End = input('last name: ').upper().strip()
        for i,n in enumerate(lines):        
            if (f'{First} {End}') in n:
                lines.remove(lines[i])
                lines.remove(lines[i])
                lines.remove(lines[i])
                with open('project/Contacts.txt','w') as f:
                    f.writelines(lines) #updated list to  lines
                print('    Successfully removed')
                return
        else:
            print('--Name not found')
        exit = input('---Wanna exit? 6 for Yes,anything else for No: ')
        # return None if exit == '6' else print('  pls continue') #dif logic is working??
        if exit == '6':
            return
        else:
            print('--pls continue')         

def Search(First,End):
    '''Function to search for a contact.'''
    # It takes first and last name as input, searches for the contact in the text file,   
    for i,n in enumerate(lines):
        if (f'{First.strip()} {End.strip()}') in n:
            print(f'\nName: {lines[i]}\n\
Phone: {lines[i+1]}\n\
Email: {lines[i+2]}')
            return
    print('--details not found')

def Update(First,End):
    '''Function to update a contact.'''
    # It takes first and last name as input, searches for the contact in the text file,
    # and updates the contact if found.
    for i,n in enumerate(lines):
        if f'{First.strip()} {End.strip()}' in n:
            lines[i] = f'Name--{input('New name(First):').upper().strip()\
                                } {input("last name:").upper().strip()}'
            lines[i+1] = f'\nPhone--{str(Phone())}' #\n ??
            lines[i+2] = f'\nEmail--{Email()}'
            with open('project/Contacts.txt','w') as f:
                f.writelines(lines)
            #in list of lines you can see escape chr in the lines.be careful with it 
            print('--Successfully updated')
            return
    else:
        print('--name not found') 
          

# Main program starts here
choice = input('----Enter your choice(1-5): ')
if choice == '1':
    Add(input('First name: ').upper(),input('Last name: ').upper())
elif choice == '2':
    View()
elif choice == '3':
    print("----you are going to delete one's whole details")
    Remove()
elif choice == '4':
    print("----Search for one's whole details")
    Search(input('First name: ').upper(),input('Last name: ').upper())
elif choice == '5':
    print('--Type name, whose details you want to update')
    Update(input('First name: ').upper(),input('Last name: ').upper())
else:
    print('---Pls give a right command')
    


        

    