import os
import tkinter as tk


class Product:
  def __init__(self, barcode, name, ingredients):
    self.barcode = barcode
    self.name = name
    self.ingredients = ingredients
  
  
def CreateAccount(): 
  """
  print("Creating account.")
  accountfile =  open('account.txt', "w")
  name = input("Enter name: ")
  accountfile.write(name + "\n")
  print("\nPlease enter the number of any allergies you have: \n1. Gluten\n2. Peanuts\n3. Soy")
  allergies = input()
  accountfile.write(allergies + "\n")
  accountfile.close()
  """
  newWindow = tk.Tk()
  newWindow.title("Create your profile")
  newWindow.geometry("400x400")
  #account = open('account.txt', "r")
  
  #account.close()
  NameLabel = tk.Label(newWindow, text ="Enter your name:").pack()
  NameText = tk.Text(newWindow, height = "1")
  NameText.pack()
  nuta = tk.BooleanVar(newWindow)
  glutena = tk.BooleanVar(newWindow)
  soya = tk.BooleanVar(newWindow)
  AllergyLabel = tk.Label(newWindow, text="Please check the boxes you are allergic to: ").pack()
  nutcheck = tk.Checkbutton(newWindow, text='Peanuts', variable=nuta, onvalue=True, offvalue=False).pack()
  glutencheck = tk.Checkbutton(newWindow, text='Gluten', variable=glutena, onvalue=True, offvalue=False).pack()
  soycheck = tk.Checkbutton(newWindow, text="Soy", variable=soya, onvalue=True, offvalue=False).pack()
  f = open('account.txt', 'w')
  f.close()
  submitB = tk.Button(newWindow, text="Save Profile", command= lambda: writeToFile(NameText.get(1.0, "end-1c"), nuta.get(), glutena.get(), soya.get())).pack()
  
  
  #NameLabel.grid(row = 0, column = 0, sticky="W")
  #NameText.grid(row = 1, column = 0, sticky="W")
  #AllergyLabel.grid(row = 2, column = 0, sticky="W")
  #nutcheck.grid(row = 3, column = 0, sticky="W")
  #glutencheck.grid(row = 4, column = 0, sticky="W")
  #soycheck.grid(row = 5, column = 0, sticky="W")
  #submitB.grid(row = 6, column = 0, sticky="W")
  newWindow.mainloop()

def initialize():
  global PB, CEREAL
  PB = Product(1111, "Peanut Butter", ["peanuts", "palm oil", "sugar"]) #nuts allergy
  CEREAL = Product(2222, "Cereal", ["whole grain oats", "Corn Starch", "Sugar","Salt"]) #gluten allergy

def writeToFile(iname, inut, igluten, isoy):
  accountfile = open('account.txt', 'w')
  accountfile.write(iname + "\n")
  if(inut == True):
    print(iname + " is allergic to nuts")
    accountfile.write("True\n")
  else:
    print(iname + " false nuts")
    accountfile.write("False\n")
  if(igluten == True):
    print(iname + " is allergic to gluten")
    accountfile.write("True\n")
  else:
    print(iname + " false gluten")
    accountfile.write("False\n")
  if(isoy == True):
    print(iname + " is allergic to soy.")
    accountfile.write("True\n")
  else:
    accountfile.write("False\n")
    print(iname + " false soy")
  accountfile.close()
  

def CheckUser():
  accountCheck = 'account.txt'
  if os.path.isfile(accountCheck):
    account = open('account.txt', "r")
    initialize()
    global username ; username = account.readline()[:-1]
    print("Account found. Hello " + username + ".")
    account.close()
  else: 
    print("Please create account.")
    CreateAccount()
    CheckUser()

def editProfile():
  newWindow = tk.Toplevel(mainPage)
  newWindow.title("Edit your profile")
  newWindow.geometry("400x400")
  #account = open('account.txt', "r")
  
  #account.close()
  NameLabel = tk.Label(newWindow, text ="Your name:").pack()
  NameText = tk.Text(newWindow, height = "1")
  NameText.insert(1.0, username)
  NameText.pack()
  nuta = tk.BooleanVar(newWindow)
  glutena = tk.BooleanVar(newWindow)
  soya = tk.BooleanVar(newWindow)
  AllergyLabel = tk.Label(newWindow, text="Please check the boxes you are allergic to: ").pack()
  nutcheck = tk.Checkbutton(newWindow, text='Peanuts', variable=nuta, onvalue=True, offvalue=False).pack()
  glutencheck = tk.Checkbutton(newWindow, text='Gluten', variable=glutena, onvalue=True, offvalue=False).pack()
  soycheck = tk.Checkbutton(newWindow, text="Soy", variable=soya, onvalue=True, offvalue=False).pack()
  submitB = tk.Button(newWindow, text="Save Profile", command= lambda: writeToFile(NameText.get(1.0, "end-1c"), nuta.get(), glutena.get(), soya.get())).pack()
  
  
  #NameLabel.grid(row = 0, column = 0, sticky="W")
  #NameText.grid(row = 1, column = 0, sticky="W")
  #AllergyLabel.grid(row = 2, column = 0, sticky="W")
  #nutcheck.grid(row = 3, column = 0, sticky="W")
  #glutencheck.grid(row = 4, column = 0, sticky="W")
  #soycheck.grid(row = 5, column = 0, sticky="W")
  #submitB.grid(row = 6, column = 0, sticky="W")
  newWindow.mainloop()


def TestPB(allergylist):
  pbWindow = tk.Toplevel(mainPage)
  pbWindow.geometry("200x200")
  if(allergylist[1] == "True\n"):
    result = username + " is allergic to peanut butter."
    color = "red"
  else:
    result = username + " is not allergic to peanut butter."
    color = "green"
  output = tk.Label(pbWindow, text = result, fg= color)
  output.grid(row = 0, column = 0)

def TestGluten(allergylist):
  gWindow = tk.Toplevel(mainPage)
  gWindow.geometry("200x200")
  if(allergylist[2] == "True\n"):
    result = username + " is allergic to cereal."
    color = "red"
  else:
    result = username + " is not allergic to cereal."
    color = "green"
  output = tk.Label(gWindow, text = result, fg= color)
  output.grid(row = 0, column = 0)

def TestSoy(allergylist):
  soyWindow = tk.Toplevel(mainPage)
  soyWindow.geometry("200x200")
  if(allergylist[3] == "True\n"):
    result = username + " is allergic to tofu."
    color = "red"
  else:
    result = username + " is not allergic to tofu."
    color = "green"
  output = tk.Label(soyWindow, text = result, fg= color).pack()
  output.grid(row = 0, column = 0)


print("Checking for user information.")
CheckUser()

mainPage = tk.Tk()
mainPage.title("Scan My Food")
mainPage.geometry("800x600")
userGreeting = "Hello, " + username
greeting = tk.Label(text = userGreeting)
greeting.pack(anchor='center')

greeting.config(font=("Courier bold", 26))
greeting.config(fg="blue")
greeting.config(bg="white")
greeting.grid(row=0, column = 0, pady = 3)

editProfileB = tk.Button(text="Edit Profile", command=editProfile)
editProfileB.grid(row = 1, column = 0, pady = 5)

f = open('account.txt', "r")
allergies = f.readlines()
"""
for x in range(len(allergies)):
  print(allergies[x])
f.close()
if(allergies[1] == "True\n"):
  print(username + "is allergic to nuts")
else:
  print(username + "is not allergic to nuts")
if(allergies[2] == "True\n"):
  print(username + "is allergic to gluten")
else: 
  print(username + "is not allergic to gluten")
if(allergies[3] == "True\n"):
  print(username + "is allergic to soy")
else:
  print(username + "is not allergic to soy")
""" 
pcheck = tk.Button(mainPage, text="Test Peanut Butter", command= lambda: TestPB(allergies))
gcheck = tk.Button(mainPage, text= "Test Cereal", command= lambda: TestGluten(allergies))
scheck = tk.Button(mainPage, text="Test Tofu", command = lambda: TestSoy(allergies))

pcheck.grid(row = 3, column = 0, padx = 50)
gcheck.grid(row = 3, column = 1, padx = 50)
scheck.grid(row = 3, column = 2, padx = 50)
mainPage.mainloop()
