class List:
    name = 'default'
    contact = 'default'
    adress = 'default'
    def __init__ (self, name,contact,adress):
        self.name = name
        self.contact = contact
        self.adress = adress
Turat = List('Turat','0780546004','Asanbay')
Kirill = List('Kirill','0564604650','8 mkr')
Taalay = List('Taalay','0708955999','Alamedin-1')
Aito = List('Aito','0550202002','Alamedin')
class ContactList(list):
    name = 'default'
    def search_by_name(self, name):
        self.name = 1
all_contact = ['Turat','Kirill','Taalay','Aito']
all_contact = ContactList()
all_contact.search_by_name(1)
for i in range(0,5):
    all_contact.name = str(input('name:'))
    if all_contact.name == 'Turat':
        print(Turat.name,Turat.contact,Turat.adress)
    elif all_contact.name == 'Kirill':
        print(Kirill.name,Kirill.contact,Kirill.adress)
    elif all_contact.name == 'Taalay':
        print(Taalay.name,Taalay.contact,Taalay.adress)
    elif all_contact.name == 'Aito':
        print(Aito.name,Aito.contact,Aito.adress)
    else:
        print('Такого контакта нет')