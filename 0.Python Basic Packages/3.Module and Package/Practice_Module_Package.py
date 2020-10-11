#!/usr/bin/env python
# coding: utf-8

# # Module

# ### os Module

# In[1]:


from IPython.display import Image


# In[4]:


Image(r'OS_Command.jpg', width=700, height=600)


# #### Basic Commands

# In[5]:


import os


# In[6]:


print(os.name)


# In[7]:


print("Python path :", os.path)


# In[8]:


print("Environment Variable :", os.getenv('OS'))


# In[9]:


print("Process id :", os.getpid())


# In[10]:


print("Current working directory :", os.getcwd())


# In[11]:


print('List of files & folder : ', os.listdir())


# In[14]:


# Create a new directory.
os.mkdir("Sachin")
print(os.getcwd())


# In[15]:


#change the current working directory.
os.chdir(r'E:\Sachin\Learning\Meetup\3.Module and Package\Sachin')
print(os.getcwd())


# In[6]:


print(os.getcwd())
#os.chdir('../')  # comes 1 directory back
os.chdir(r'E:\Sachin\Learning\Meetup\3.Module and Package')
print(os.getcwd())


# In[18]:


print(os.rmdir('Sachin'))


# #### Assignment : Make Group of Folders/Directories

# In[7]:


import os
print('Current Path:', os.getcwd())

os.mkdir('MyProject')
os.chdir('MyProject')
path1 = os.getcwd()
print('Changed Directory :', path1)

with open(path1+r'\text.txt','w') as a:
    a.write("sachin text")

os.mkdir('Admin')
os.chdir(path1 + r'\Admin')
print('Changed Directory :', os.getcwd())
with open('admin.txt','w') as a:
    a.write("sachin text")
os.chdir('../')
os.mkdir('HR')
os.mkdir('User')

os.chdir(path1 + r'\User')
print('Current Path2 :', os.getcwd())

with open('user.txt','w') as a:
    a.write("sachin text")
a.close()

os.mkdir('Teacher')
os.mkdir('Student')
os.chdir(path1 + r'\User\Student')
print('Current Path3 :', os.getcwd())
with open('student.txt','w') as a:
    a.write("sachin text")
a.close()
os.mkdir('Other')
os.chdir(path1 + r'\User\Student\Other')
with open('other.txt','w') as a1:
    a1.write("sachin text")
a1.close()


# #### Assignment : Remove Group of Folders/Directories

# In[142]:


import os
print('Current Path:', os.getcwd())
#os.chdir(r'C:\Users\Ankush\Desktop\Python\Meetup\Module_Package')
#os.rmdir(r'C:\Users\Ankush\Desktop\Python\Meetup\Module_Package\MyProject')   #Cannot do as directory is not empty
print('List of Files/Folder : ', os.listdir())
for folder in os.listdir():
    os.rmdir(folder)

path2 = os.chdir('../')
print('Current Path:', os.getcwd())
print('List of Files/Folder : ', os.listdir())
for folder in os.listdir():
    os.rmdir(folder)

path3 = os.chdir('../')
print('Current Path:', os.getcwd())
print('List of Files/Folder : ', os.listdir())
os.rmdir('MyProject')


# In[70]:


print('List of Files/Folder : ', os.listdir())


# #### Generalization of Deleting the file

# In[3]:


import os
path=r"E:\Sachin\Learning\Meetup\3.Module and Package\MyProject"
foldername="MyProject"


# In[5]:


for (dirpath, dirnames, filenames) in os.walk(path,topdown=False):
    print("dirpath:",dirpath)
    #print(type(dirpath))
    print("dirname:",dirnames)
    #print(type(dirnames))
    print("filenames:",filenames)
    #print(type(filenames))
    
    
    if dirpath.find(foldername)!=-1:
        #if len(dirnames):
         #   print("Removing directory:",dirnames)
          #  os.rmdir(dirnames)
        if len(filenames):
            for i in filenames:
                print("Removing files",i)
                os.remove(dirpath+'\\'+i)
        ls=dirpath.split("\\")
        os.rmdir(dirpath)
        print("Removing root folder case 1",ls[-1])       
    #         else:
#             ls2=dirpath.split("\\")
#             os.rmdir(dirpath)
#             print("Removing root folder case 2",ls2[-1])
    print('*'*40)


# In[ ]:





# ### sys Module

# #### Basics Commands

# In[144]:


import sys
print('Parameters...{}, {}' .format(sys.argv[0], sys.argv[1]))


# In[145]:


#for path
print(sys.path)


# In[146]:


print(sys.path[0])


# In[147]:


#Python version
print(sys.version)


# In[10]:


#python 
try:
    10/0
except:
    print(sys.exc_info())
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info()[2])


# In[150]:


#for exiting from program
try:
    print ('1 Text file start...')
    print("Hii..", )
    sys.exit('We exit now')
    print("Version : ", sys.version)
except:
    print('We handle it')


# ### Math Module

# #### Basic Commands

# In[203]:


import math


# In[204]:


#ceil(x): Returns the smallest integer greater than or equal to x.
w = 5.25
x = 5.84
y = -5.25
z = -5.84
print('type of ceil :', type(math.ceil(x)))
print('ceil of w :', math.ceil(x))
print('ceil of x :', math.ceil(w))
print('ceil of y :', math.ceil(y))
print('ceil of z :', math.ceil(z))


# In[205]:


#floor(x): Returns the largest integer less than or equal to x
x = 5.253
y = 5.84
y = -5.25
z = -5.84
print('type of floor :', type(math.floor(x)))
print('floor of w :', math.floor(w))
print('floor of x :', math.floor(x))
print('floor of y :', math.floor(y))
print('floor of z :', math.floor(z))


# In[20]:


#fmod (x, y ): Returns the remainder when x is divided by y
print('1. fmaod : ', math.fmod(20,4))
print('2. fmaod : ', math.fmod(20,3))
#print('3. fmaod : ', math.fmod(20,0))
print('4. fmaod : ', math.fmod(0,4))


# In[23]:


#trunc (x): Returns the truncated integer value of x
print('trunc : ', math.trunc(x))


# In[24]:


#pow(x, y): Returns x raised to the power y
print('Power of : ', math.pow(3,4))


# In[26]:


#sqrt (x): Returns the square root of x
print('square root : ', math.sqrt(81))


# In[35]:


#cos(x): Returns the cosine of x
print('cos : ', math.cos(0))


# ### DateTime Module

# In[7]:


import datetime
#YYYY,MM,DD


# In[8]:


import time


# In[30]:


print("1. Today's Date Time : ", datetime.datetime.today())
print("2. Today's Date Time : ", datetime.datetime.now())
print('Type : ', type(datetime.datetime.now()))
print("Today's Date : ", datetime.datetime.now().date())
print("Today's Time : ", datetime.datetime.now().time())


# In[ ]:


print("Today's Date : ", datetime.date.today())
print("Min Date : ", datetime.date.min)
print("Max Date : ", datetime.date.max)
print("First Date Time : ", datetime.datetime.fromtimestamp(0))
print("datetime fromtimestamp : ", datetime.datetime.fromtimestamp((time.time())))
print("Date fromtimestamp : ", datetime.date.fromtimestamp(time.time()))


# In[13]:


print('Local time : ', time.localtime())


# In[27]:


d1 = datetime.date(2020,4,3)
print(type(d1))
print('d1 : ', d1)
print("ctime d1 : ", d1.ctime())


# In[107]:


print('timetuple : ', d1.timetuple())
print('weekday : ', d1.weekday())
print('isoweekday : ', d1.isoweekday())
print('isocalendar : ', d1.isocalendar())
print('isoformat : ', d1.isoformat())


# In[26]:


d2 = datetime.datetime(1990,6,21,21,6,23,5446)
print('d2 : ', d2)
print("ctime d2 : ", d2.ctime())
print ("Year is: %d" % d2.year)
print ("Month is: %d" % d2.month)
print ("Day is: %d" % d2.day)
print ("Hour is: %d" % d2.hour)
print ("Minute is: %d" % d2.minute)
print ("Second is: %d" % d2.second)
print ("Microsecond is: %d" % d2.microsecond)


# In[28]:


d3 = d1.replace(year=1992, month=7, day=14)
print(d3)
print(d1)


# #### Format of Datetime Module

# In[20]:


from IPython.display import Image
Image(r'C:\Users\Ankush\Desktop\Python\Meetup\Module_Package\DateTime_Format.jpg', width=600, height=600)


# In[32]:


print('Datetime : ', datetime.datetime.now())
print('Formatting : ', datetime.datetime.now().strftime('%' + input('Enter format... ')))


# In[40]:


#Change str value to Datetime
mystr = 'Jul 25 2014 2:43PM'
print('mystr : {} \t\t type : {} ' .format(mystr, type(str)))
DTformat = datetime.datetime.strptime(mystr, '%b %d %Y %I:%M%p')
print('DTformat : {} \t\t type : {} ' .format(DTformat, type(DTformat)))


# ### Random Module

# #### Basic Command

# In[41]:


import random


# - **random.random()** -- Generates a random float number between 0.0 to 1.0. The function doesn't need any arguments.

# In[117]:


print(type(random.random()))
print(random.random())


# - **random.uniform(a, b)** -- Generates a random float number in range [a, b].

# In[174]:


print(type(random.uniform(100, 200)))
print(random.uniform(100, 300))


# - **Randrange(): It will produce a random integer value less than the value specified by the [stop] argument**
# - random.randrange(start(opt),stop,step(opt))
# - Parameters :
# start(opt) :  Number consideration for generation starts from this,
# default value is 0. This parameter is optional.
# stop : Numbers less than this are generated. This parameter is mandatory.
# step(opt) : Step point of range, this won't be included. This is optional.
# Default value is 1.

# In[61]:


print(type(random.randrange(225)))
print(random.randrange(654))


# In[160]:


print(random.randrange(0, 102, 10))


# - **Randint(a, b)** -- Return random integer in range [a, b], including both value.

# In[151]:


print(type(random.randint(4,24)))
print(random.randint(4,24))


# In[116]:


print(random.randrange(1, 25,4))


# - **random.choice()** -- Returns a randomly selected element from a non-empty sequence. An empty sequence as argument raises an IndexError.

# In[185]:


#print(random.choice([12,23,45,67,65,43]))
mylst = [25,78,6,45,35,84,19,37,28,46]
#mylst = (52,65,85,75,35,95,15)
print(mylst)
print(type(random.choice(mylst)))
print(random.choice(mylst))


# - **random.sample(mylst, k)** -- Return a k length list of unique elements chosen from the mylst sequence or set. Used for random sampling without replacement.

# In[186]:


print(type(random.sample(mylst, 4)))
print(random.sample(mylst, 4))


# - **random.shuffle()** -- This functions randomly reorders the elements in a list. Cannot do the operation on Tuple

# In[187]:


print('Shuffle : ', random.shuffle(mylst))
print(mylst)


# ### Zip Module

# #### Basic Command

# In[ ]:





# In[ ]:





# In[ ]:





# ### User Defined Module

# Any text file with the .py extension containing Python code is basically a module. Different Python objects such as functions, classes, variables, constants, etc., defined in one module can be made available to an interpreter session or another Python script by using the import statement.

#  When the import statement is encountered either in an interactive session or in a script:
# - First, the Python interpreter tries to locate the module in current working directory.
# - If not found, directories in the **PYTHONPATH** environment variable are searched.
# - If still not found, it searches the installation default directory.
# - If the required module is not present in any of the directories, the message **ModuleNotFoundError** is thrown.

# In[ ]:




