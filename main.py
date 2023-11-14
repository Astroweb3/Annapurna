from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
import mysql.connector
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.lang import Builder
import mysql.connector
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog
from kivymd.uix.toolbar import MDTopAppBar
from pyzbar.pyzbar import decode
import cv2
from kivy.graphics.texture import Texture
from kivymd.uix.button import MDFlatButton
import time
from collections import OrderedDict
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.pickers import MDDatePicker 
import mysql.connector
from datetime import timedelta, date
import datetime
import pandas as pd
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
import re
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.datatables import MDDataTable
from PyQt5.QtWidgets import QApplication, QFileDialog
import sys
from sqlalchemy import create_engine

Window.size = (310, 580)
from_date = [] 
to_date = []
food = []
date4 = []
date2 = []
date3 = []
date1 = []
lunch = []
lunch1 = []
snaks = []
snaks1 = []
name = []
t = []
food1 = []
t1 = []
price = []
price1 = []
delete_Canteen_id = []
delete_Student_id = []
Accept_User_id = []
Reject_User_id = []
instance_stud = []
User_id = []
name = []
det_date = []
det_date1 = []
det_food = []
det_t = []
det_snaks = []
det_price = []
det_lunch = []
det_name = []
det_roll = []
Att_date = []
Att_date1 = []
Att_name = []
Att_roll = []
Att_food = []
Att_t = []
names = []
rollno = []
counts = []
can_food = []
can_food1 = []
can_food2 = []
cat_name = []
cat_name2 = []
Canteen_RN = []
can = []
c = []
Can_no = []
Can_date = []
Can_Food = []
Can_Name = []
Stu_Name = []
Stu_roll = []
Can_no1 = []
Can_date1 = []
Can_Food1 = []
Can_Name1 = []
class DropdownButton(MDFloatLayout, Button):
    pass

class SearchBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class Example(Screen):
    def __init__(self, **kwargs):
        super(Example,self).__init__(**kwargs)
    #    layout=MDBoxLayout(orientation='vertical')
    #    TopBar = MDTopAppBar(title = "QRScanner", font_name= "Poppins/Poppins-SemiBold.ttf", font_size= "26sp", pos_hint= {"center_x": .5, "center_y": .1}, text_color = (0.49, 0.498, 0.498, 1), left_action_items = ([["arrow-left-circle-outline", lambda x : app.root.current = "bottom"]]))
       #, left_action_items = [["arrow-left-circle-outline", lambda *args : setattr(self.manager, "current", "third")]]
       #ViewReport = MDFlatButton(text = "View Report", on_press = self.MovetoFourScreen, pos_hint = {'center_x': 0.5, 'center_y': 0.2})
        TopTools = Builder.load_string(TopTool)
        self.add_widget(TopTools)
        menu1_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Export Orders", 
                "height": dp(56),
                "on_release": lambda x=f"Export Orders": self.print_check(),
               
             } ,]
            
        
        self.menu1 = MDDropdownMenu(
            items=menu1_items,
            elevation=4,
            background_color=(1, 1, 1, 1),
            border_margin=dp(100),
            width_mult=4,
            radius=[24, 0, 24, 0]
        )
        self.back = MDTopAppBar(
                id = 'button1' ,
                title= "Food Orders",
                anchor_title= "left",
                pos_hint = {"center_y":0.95},
                left_action_items = [["arrow-left", lambda x: LoginPage.logout3(self), "Back To Home Page"]],
                right_action_items = [["dots-vertical", lambda x: self.dropdown1(x)]])
        
        self.add_widget(self.back)
        database1 = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        mycursor1 = database1.cursor()
        mycursor2 = database1.cursor()
        mycursor3 = database1.cursor()
        mycursor4 = database1.cursor()
        mycursor5 = database1.cursor()
        mycursor6 = database1.cursor()
        
        mycursor1.execute("SELECT can_id FROM canteen_table ")
        myresult = mycursor1.fetchall()
        
        mycursor2.execute("SELECT  entryDateTime FROM canteen_table ")
        myresult2 = mycursor1.fetchall()
        
        mycursor3.execute("SELECT food_category FROM canteen_table ")
        myresult3 = mycursor1.fetchall()
        
        mycursor4.execute("SELECT studName FROM canteen_table ")
        myresult4 = mycursor1.fetchall()

        mycursor5.execute("SELECT studRoll FROM canteen_table ")
        myresult5 = mycursor1.fetchall()
        
        mycursor6.execute("SELECT canteenname FROM canteen_table ")
        myresult6 = mycursor1.fetchall()

        result = []
        result2= []
        result3 = []
        result4 = []
        result5 = []
        result6 = []
        
        for i in range(0,len(myresult)):
            result.extend(myresult[i])
            result2.extend(myresult2[i])
            result3.extend(myresult3[i])
            result4.extend(myresult4[i])
            result5.extend(myresult5[i])
            result6.extend(myresult6[i])
        
        self.data_tables = MDDataTable(
            use_pagination=True,
            size_hint = (0.99,0.89),
            column_data=[
                ("No.", dp(20)),
                ("Date", dp(20)),
                ("Food", dp(20)),
                ("Name", dp(20)),
                ("Roll No", dp(20)),
                ("Canteen Name", dp(20)),
            ],
            row_data=[
                (
                    result[i],
                    result2[i],
                    result3[i],
                    result4[i],
                    result5[i],
                    result6[i],
                )for i in range(0,len(result)) ],
            
            sorted_on="Schedule",
            sorted_order="ASC",
            elevation=2,
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)
        self.add_widget(self.data_tables)
   
    def dropdown1(self,button1):   
        self.menu1.caller = button1
        self.menu1.open()
        
    def print_check(self):
        
        database = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        mycursor = database.cursor()
        mycursor.execute("SELECT * FROM canteen_table ")
        dd = mycursor.fetchall()
        df = pd.DataFrame(dd,columns=['No','Date','Food','Name','RollNo','Canteen Name'])
        df.to_excel("Orders{}.xlsx".format(pd.datetime.today().strftime('%Y-%m-%d %H_%M_%S')))    
        
    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''

        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''

        print(instance_table, current_row)

    # Sorting Methods:
    # since the https://github.com/kivymd/KivyMD/pull/914 request, the
    # sorting method requires you to sort out the indexes of each data value
    # for the support of selections.
    #
    # The most common method to do this is with the use of the builtin function
    # zip and enumerate, see the example below for more info.
    #
    # The result given by these funcitons must be a list in the format of
    # [Indexes, Sorted_Row_Data]

    def sort_on_signal(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][2]))

    def sort_on_schedule(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: sum(
                    [
                        int(l[1][-2].split(":")[0]) * 60,
                        int(l[1][-2].split(":")[1]),
                    ]
                ),
            )
        )

    def sort_on_team(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-1]))

TopTool_Example = """

MDBoxLayout:
    orientation: "vertical"

    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_y": .95}
        user_font_size: "30sp"
        theme_text_color: "Custom"
        text_color: rgba(26, 24, 58, 255)
        on_release:
            app.root.transition.direction = "right"
            app.root.current = "bottom"    
"""

class Request(Screen):
    def __init__(self, **kwargs):
        super(Request,self).__init__(**kwargs)
        menu1_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Accept", 
                "height": dp(56),
                "on_release": lambda x=f"Brief Report": self.Accept_User(),

                # "viewclass": "OneLineListItem",
                # "text": f"Reject", 
                # "height": dp(56),
                # "on_release": lambda x=f"Brief Report": self.Reject_User(),
               
             } ,]
            
        
        self.menu1 = MDDropdownMenu(
            items=menu1_items,
            elevation=4,
            background_color=(1, 1, 1, 1),
            border_margin=dp(100),
            width_mult=4,
            radius=[24, 0, 24, 0]
        )
        
        database = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        my1 = database.cursor()    
        my2 = database.cursor()
        my3 = database.cursor()
        my4 = database.cursor()  
        
        my1.execute("SELECT request_id FROM request_table WHERE req_status = 'Pending'")
        myr1 = my1.fetchall()
        
        my2.execute("SELECT req_username FROM request_table WHERE req_status = 'Pending'")
        myr2 = my1.fetchall()
        
        my3.execute("SELECT req_canteenname FROM request_table WHERE req_status = 'Pending'")
        myr3 = my1.fetchall()
        
        my4.execute("SELECT req_apprights FROM request_table WHERE req_status = 'Pending'")
        myr4 = my1.fetchall()
        #myresult = mycursor.fetchall()   
                                                                                                  
        rr1 = []
        rr2 = []
        rr3 = []
        rr4 = []
        for i in range(0,len(myr1)):
            rr1.extend(myr1[i])
            rr2.extend(myr2[i])
            rr3.extend(myr3[i])
            rr4.extend(myr4[i])
        
        self.back = MDTopAppBar(
                id = 'button1' ,
                title= "Request User",
                anchor_title= "left",
                pos_hint = {"center_y":0.95},
                left_action_items = [["arrow-left", lambda x: LoginPage.logout2(self), "Back To Home Page"]],
                right_action_items = [
                                        ["account-check-outline", lambda x: self.Insert_User(), "Account Check", "Account Check"],
                                        ["account-remove-outline", lambda x: self.Reject_User(), "Remove Account", "Remove Account"],
                                        ])
        self.add_widget(self.back)
        
        self.student_table =MDDataTable(
            check=True,
            use_pagination=True,
            size_hint = (0.99,0.89),
            rows_num = 10,
            column_data=[
                ("No.", dp(20)),
                ("Name", dp(20)),
                ("Roll No", dp(20)),
                ("Dept", dp(20)),],  
            row_data=[
                (
                    rr1[i],
                    rr2[i],
                    rr3[i],
                    rr4[i],
                )for i in range(0,len(rr1))],)
        
        self.student_table.bind(on_check_press=self.on_check_student)
        self.add_widget(self.student_table)
        
    def dropdown1(self,button1):   
        self.menu1.caller = button1
        self.menu1.open()   
    #student data delete function 
    def Insert_User(self):
        data = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        cursor1 = data.cursor()
        cursor2 = data.cursor()
        for i in range(0, len(User_id)):
            query = "SELECT * FROM request_table WHERE request_id = {}".format(User_id[i])
            userName = ''
            userPassw = ''
            canteen_name = ''
            name = ''
            AppRights = ''
            cursor1.execute(query)
            users = cursor1.fetchall()
            for user in users:
                userName = f'{userName}{user[1]}'
                userPassw = f'{userPassw}{user[4]}'
                canteen_name = f'{canteen_name}{user[2]}' 
                name = f'{name}{user[3]}'
                AppRights = f'{AppRights}{user[6]}'
                InsertQuery = "INSERT INTO login_table (username, passw, canteenname, name, apprights) VALUES ('"+userName+"', '"+userPassw+"', '"+canteen_name+"', '"+name+"', '"+AppRights+"')"
                cursor2.execute(InsertQuery)
                Status = "UPDATE request_table SET req_status = 'Accepted' WHERE request_id = " + User_id[i]
                cursor1.execute(Status)
                print(userName, userPassw)
            data.commit()

    def Accept_User(self):
        data = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        cursor1 = data.cursor()
        for i in range(0,len(User_id)):
            query = "UPDATE request_table SET req_status = 'Accepted' WHERE request_id={}".format(User_id[i])
            cursor1.execute(query) 
            data.commit()

       # self.Insert_User()
    def Reject_User(self):
        data = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        cursor1 = data.cursor()
        for i in range(0,len(User_id)):
            query = "UPDATE request_table SET req_status = 'Rejected' WHERE request_id={}".format(User_id[i])
            cursor1.execute(query) 
            data.commit()

    def on_check_student(self,instance_table1,current_row1):
        User_id.append(current_row1[0])
        instance_stud.append(instance_table1)
        

class Student_delete(Screen):
    def __init__(self, **kwargs):
        super(Student_delete,self).__init__(**kwargs)
        menu1_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Delete the Selected Items", 
                "height": dp(56),
                "on_release": lambda x=f"Brief Report": self.delete_student_check(),
               
             } ,]
            
        
        self.menu1 = MDDropdownMenu(
            items=menu1_items,
            elevation=4,
            background_color=(1, 1, 1, 1),
            border_margin=dp(100),
            width_mult=4,
            radius=[24, 0, 24, 0]
        )
        
        database = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        my1 = database.cursor()    
        my2 = database.cursor()
        my3 = database.cursor()
        my4 = database.cursor()  
        
        my1.execute("SELECT ID FROM student_table ")
        myr1 = my1.fetchall()
        
        my2.execute("SELECT studName FROM student_table ")
        myr2 = my1.fetchall()
        
        my3.execute("SELECT studRoll FROM student_table ")
        myr3 = my1.fetchall()
        
        my4.execute("SELECT studDept FROM student_table ")
        myr4 = my1.fetchall()
        #myresult = mycursor.fetchall()   
                                                                                                  
        rr1 = []
        rr2 = []
        rr3 = []
        rr4 = []
        for i in range(0,len(myr1)):
            rr1.extend(myr1[i])
            rr2.extend(myr2[i])
            rr3.extend(myr3[i])
            rr4.extend(myr4[i])
        
        self.back = MDTopAppBar(
                id = 'button1' ,
                title= "Delete User",
                anchor_title= "left",
                pos_hint = {"center_y":0.95},
                left_action_items = [["arrow-left", lambda x: LoginPage.logout2(self), "Back To Home Page"]],
                right_action_items = [["dots-vertical", lambda x: self.dropdown1(x)]],)
        self.add_widget(self.back)
        
        self.student_table =MDDataTable(
            check=True,
            use_pagination=True,
            size_hint = (0.99,0.89),
            rows_num = 10,
            column_data=[
                ("No.", dp(20)),
                ("Name", dp(20)),
                ("Roll No", dp(20)),
                ("Dept", dp(20)),],  
            row_data=[
                (
                    rr1[i],
                    rr2[i],
                    rr3[i],
                    rr4[i],
                )for i in range(0,len(rr1))],)
        
        self.student_table.bind(on_check_press=self.on_check_student)
        self.add_widget(self.student_table)
        
    def dropdown1(self,button1):   
        self.menu1.caller = button1
        self.menu1.open()   

    
        
    def on_check_student(self,instance_table1,current_row1):
        delete_Student_id.append(current_row1[0])
        instance_stud.append(instance_table1)
        
    #student data delete function        
    def delete_student_check(self):
        data = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        cursor1 = data.cursor()
        for i in range(0,len(delete_Student_id)):
            query = "DELETE FROM student_table WHERE ID={}".format(delete_Student_id[i])
            cursor1.execute(query) 
            data.commit()

class Food_Order(Screen):
    def __init__(self, **kwargs):
        super(Food_Order,self).__init__(**kwargs)
        
        #data table for canteen delete 
        database1 = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        mycursor1 = database1.cursor()
        mycursor2 = database1.cursor()
        mycursor3 = database1.cursor()
        mycursor4 = database1.cursor()
        mycursor5 = database1.cursor()
        mycursor6 = database1.cursor()

        mycursor1.execute("SELECT can_id FROM canteen_table ")
        myresult = mycursor1.fetchall()
        
        mycursor2.execute("SELECT  entryDateTime FROM canteen_table ")
        myresult2 = mycursor1.fetchall()
        
        mycursor3.execute("SELECT food_category FROM canteen_table ")
        myresult3 = mycursor1.fetchall()

        mycursor4.execute("SELECT studName FROM canteen_table ")
        myresult4 = mycursor1.fetchall()

        mycursor5.execute("SELECT studRoll FROM canteen_table ")
        myresult5 = mycursor1.fetchall()

        mycursor6.execute("SELECT canteenname FROM canteen_table ")
        myresult6 = mycursor1.fetchall()

        res = []
        result2= []
        result3 = []
        result4 = []
        result5 = []
        result6 = []
        
        for i in range(0,len(myresult)):
            res.extend(myresult[i])
            result2.extend(myresult2[i])
            result3.extend(myresult3[i])
            result4.extend(myresult4[i])
            result5.extend(myresult5[i])
            result6.extend(myresult6[i])

        self.add_widget(
            MDTopAppBar(
                id = 'button1' ,
                title= "Food Orders",
                anchor_title= "left",
                left_action_items = [["arrow-left", lambda x: LoginPage.logout2(self), "Back To Home Page"]],
                pos_hint = {"center_y":0.95}))
       
        self.datatables = MDDataTable(
            use_pagination=True,
            rows_num = 10,
            size_hint = (0.999,0.89),
            column_data=[
                ("No.", dp(20)),
                ("Date", dp(20)),
                ("Food", dp(20)),
                ("Name", dp(20)),
                ("Roll No", dp(20)),
                ("Canteen Name", dp(20)),],  
            row_data=[
                (
                    res[i],
                    result2[i],
                    result3[i],
                    result4[i],
                    result5[i],
                    result6[i],
                )for i in range(0,len(res))],)   

        self.add_widget(self.datatables)
        
class Canteen_user(Screen):
    def __init__(self, **kwargs):
        super(Canteen_user,self).__init__(**kwargs)
        
       #dropdown for delete in canteen
        down_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Delete the Slected Iteams", 
                "height": dp(56),
                "on_release": lambda x=f"Brief Report": self.delete_canteen_check(),
               
             } ,]
        self.canteen_delete = MDDropdownMenu(
            items=down_items,
            elevation=4,
            background_color=(1, 1, 1, 1),
            border_margin=dp(100),
            width_mult=4,
            radius=[24, 0, 24, 0]
        )
        
        database = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        my1 = database.cursor()    
        my2 = database.cursor()
        my3 = database.cursor()
        my4 = database.cursor()
        my5 = database.cursor()
        my6 = database.cursor()  
        
        my1.execute("SELECT log_id FROM login_table ")
        myr1 = my1.fetchall()
        
        my2.execute("SELECT name FROM login_table ")
        myr2 = my1.fetchall()
        
        my3.execute("SELECT canteenname FROM login_table ")
        myr3 = my1.fetchall()
        
        my4.execute("SELECT username FROM login_table ")
        myr4 = my1.fetchall()

        my5.execute("SELECT passw FROM login_table ")
        myr5 = my1.fetchall()

        my6.execute("SELECT apprights FROM login_table ")
        myr6 = my1.fetchall()
        #myresult = mycursor.fetchall()   
                                                                                                  
        rr1 = []
        rr2 = []
        rr3 = []
        rr4 = []
        rr5 = []
        rr6 = []
        for i in range(0,len(myr1)):
            rr1.extend(myr1[i])
            rr2.extend(myr2[i])
            rr3.extend(myr3[i])
            rr4.extend(myr4[i])
            rr5.extend(myr5[i])
            rr6.extend(myr6[i])
        
        self.back = MDTopAppBar(
                id = 'button1' ,
                title= "Delete User",
                anchor_title= "left",
                pos_hint = {"center_y":0.95},
                left_action_items = [["arrow-left", lambda x: LoginPage.logout2(self), "Back To Home Page"]],
                right_action_items = [["dots-vertical", lambda x: self.Canteendown(x)]],)
        self.add_widget(self.back)
        
        self.student_table =MDDataTable(
            check=True,
            use_pagination=True,
            size_hint = (0.99,0.89),
            rows_num = 10,
            column_data=[
                ("No.", dp(20)),
                ("Name", dp(20)),
                ("Canteen Name", dp(20)),
                ("User Name", dp(20)),
                ("Password", dp(20)),
                ("AppRights", dp(20)),],  
            row_data=[
                (
                    rr1[i],
                    rr2[i],
                    rr3[i],
                    rr4[i],
                    rr5[i],
                    rr6[i],
                )for i in range(0,len(rr1))],)
        
        self.student_table.bind(on_check_press=self.on_check_press)
        self.add_widget(self.student_table)   
            
    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''
        delete_Canteen_id.append(current_row[0])    
        
    #canteen delete drop down call function 
    def Canteendown(self,button):   
        self.canteen_delete.caller = button
        self.canteen_delete.open()   

    #canteen delete function
    def delete_canteen_check(self):
        data = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        cursor1 = data.cursor()
        for i in range(0,len(delete_Canteen_id)):
            query = "DELETE FROM login_table WHERE log_id={}".format(delete_Canteen_id[i])
            cursor1.execute(query) 
            data.commit()   

class LoginPage(MDApp):

    btn_color = ListProperty((177/255, 35/255, 65/255, 1))
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    database = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
    cursor = database.cursor()
    
    def build(self):
        
        database = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        mycursor = database.cursor()
        mycursor.execute("SELECT canteenname FROM canteen_table ")
        my = mycursor.fetchall()
        
        for i in my:
            if i not in cat_name:
                cat_name.append(i)
        for k in cat_name:
            cat_name2.extend(k)
            
        #drop down menu code for report
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Brief Report", 
                "height": dp(56),
                "on_release": lambda x=f"Brief Report": self.genrate_report(),
               
             } ,
            {"viewclass": "OneLineListItem",
                "text": f"Detailed Report",
                "height": dp(56),
                "on_release": lambda x=f"Detailed Report": self.Detailed_report(),},
            
            {"viewclass": "OneLineListItem",
                "text": f"Attendence",
                "height": dp(56),
                "on_release": lambda x=f"Attendence": self.Attendance_report(),}]
        
        self.menu = MDDropdownMenu(
            items=menu_items,
            elevation=4,
            background_color=(1, 1, 1, 1),
            border_margin=dp(100),
            width_mult=4,
            radius=[24, 0, 24, 0]
        )
        
        #reload page menu
        menu1_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Delete the Selected Items", 
                "height": dp(56),
                "on_release": lambda x=f"Brief Report": self.delete_student_check(),
               
             } ,]
            
        
        self.menu1 = MDDropdownMenu(
            items=menu1_items,
            elevation=4,
            background_color=(1, 1, 1, 1),
            border_margin=dp(100),
            width_mult=4,
            radius=[24, 0, 24, 0]
        )
        
        #user dropdown
        men = [
            {
                "viewclass": "OneLineListItem",
                "text": f"User", 
                "height": dp(58),
                "on_release": lambda x=f"User": self.user_name(),
               
             } ,]
        
        self.me = MDDropdownMenu(
            items=men,
            elevation=4,
            background_color=(1, 1, 1, 1),
            border_margin=dp(15),
            position = "center",
            width_mult=4,
            radius=[24, 0, 24, 0]
        )
        #user dropdown for add canteen
        add_apr = [
            {
                "viewclass": "OneLineListItem",
                "text": f"User", 
                "height": dp(58),
                "on_release": lambda x=f"User": self.add_apr_user(),
               
             } ,]
        
        self.add = MDDropdownMenu(
            items=add_apr,
            elevation=4,
            background_color=(1, 1, 1, 1),
            border_margin=dp(15),
            position = "center",
            width_mult=4,
            radius=[24, 0, 24, 0]
        )
        
        #user dropdown for signup
        aprk = [
            {
                "viewclass": "OneLineListItem",
                "text": f"User", 
                "height": dp(58),
                "on_release": lambda x=f"User": self.aprsk_name(),
               
             } ,{
                "viewclass": "OneLineListItem",
                "text": f"Admin", 
                "height": dp(58),
                "on_release": lambda x=f"Admin": self.aprsk_name1(),
               
             }]
        
        self.aprs = MDDropdownMenu(
            items=aprk,
            elevation=4,
            background_color=(1, 1, 1, 1),
            border_margin=dp(15),
            position = "center",
            width_mult=4,
            radius=[24, 0, 24, 0]
        )
        mee = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{cat_name2[i]} ", 
                "height": dp(50),
                "on_release": lambda x=f"{cat_name2[i]}": self.c_name(x),
               
             } for i in range(0,len(cat_name2))]

        self.m = MDDropdownMenu(
            items=mee,
            elevation=4,
            background_color=(1, 1, 1, 1),
            border_margin=dp(8),
            width_mult=4,
            radius=[24, 0, 24, 0]
        )
        
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(QrScanner(name = "QrScanner"))
        screen_manager.add_widget(Builder.load_file("details.kv"))
        screen_manager.add_widget(Builder.load_file("bottom.kv"))
        screen_manager.add_widget(Builder.load_file("Admin_page.kv"))
        screen_manager.add_widget(Student_delete(name = "Student_delete"))
        screen_manager.add_widget(Example(name = "Example"))
        screen_manager.add_widget(Request(name = "Requests"))
        screen_manager.add_widget(Food_Order(name = "Food_Order"))
        screen_manager.add_widget(Canteen_user(name = "Canteen_user"))
        return screen_manager
    
    def set_snackLunch(self, category, stud_roll, stud_name, canteen_name):

        try:
            Today_Date = date.today() # current date and time
            date_string = Today_Date.strftime("%Y-%m-%d")
            connections = Db_Operations()
            val = connections.Last_Date(stud_roll, category)
            if val == date_string:
                print("User Already bought!")
                self.dialog = MDDialog(
                    text="User already bought " + category + " today.",
                    buttons=[
                        MDFlatButton(
                            text="Ok",
                            on_press = self.RemainSameScreen
                        ),
                    ],)
                self.dialog.open()
            else:
                self.cursor.execute(f"INSERT INTO canteen_table (entryDateTime, food_category, studRoll, studName, canteenname) VALUES( '{date_string}', ' {category.strip()}', '{stud_roll}', '{stud_name}', '{canteen_name}')")     
                self.database.commit() #this is importnt to insert query to database
                print("Values successfully inserted!")
                print(date_string)
        except Exception as e:
            print(e)
        finally:
            print("Send data function ends here")
            self.root.current = "QrScanner"
           
    def RemainSameScreen(self, *args):
        self.dialog.dismiss(force=True)

    def on_start(self):     
        Clock.schedule_once(self.login, 2)

    def logout(self):
        screen_manager.current = "login"
        return True
    
    def adminpage(self):
        screen_manager.get_screen("Admin").ids.scr.current = "Home1"
        return True
    
    def logout2(self):
        screen_manager.current = "Admin"
        return True
    
    def logout3(self):
        screen_manager.current = "bottom"
        return True

    def callback(self):
        screen_manager.get_screen("Admin").ids.scr.current = "Home"
        return True
    
    def login(self, *args):
        screen_manager.current = "main"

    def get_id(self, instance):
        for id, widget in instance.parent.parent.parent.ids.items():
            if widget.__self__ == instance:
                return id
            
    def change_color(self,instance):
        if instance in self.root.ids.values():
            current_id = list(self.root.ids.keys())[list(self.root.ids.values()).index(instance)]
            for i in range(4):
                if f"nav_icon{i+1}" == current_id:
                    self.root.ids[f"nav_icon{i+1}"].text_color = 0, 0, 0, 1
                else:
                    self.root.ids[f"nav_icon{i+1}"].text_color = 1, 0, 0, 0
                                        
    #excel file upload
    def excelupload(self):
        app = QApplication(sys.argv)
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Excel files (*.xlsx)")
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        file_dialog.exec_()
        file_path = file_dialog.selectedFiles()[0] 
        df = pd.read_excel(file_path)
        
        # Connect to the database using sqlalchemy
        engine = create_engine('mysql+pymysql://root:%40Harishvenkat2000@localhost:3306/silverpos')
        
        # Write the DataFrame to the database
        df.to_sql('student_table', engine, if_exists='replace')
        
    #canten name drop down
    def can_n(self,buttton):
        self.m.caller = buttton
        self.m.open()
        
    def c_name(self,text_item):
        screen_manager.get_screen("Admin").ids.Can_Name.text = text_item
        Canteen_RN.append(text_item)
        self.m.dismiss()

    #update dialog box   
    def show_alert_dialog1(self):
        self.dialog1 = MDDialog(
            title = "Check Data",
            text= "Press Ok to Save",
            buttons=[
                MDFlatButton(
                    text="Ok",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.UpdateUser,
                    
                ),
                MDRaisedButton(
                    text="DISCARD",
                    md_bg_color = "red" ,
                    on_release=self.close1,                        
                ),
            ],
        )
        self.dialog1.open()
        
    def close1(self,obj):
        self.dialog1.dismiss()
        
    #update student data
    def UpdateUser(self,obj):
        
        database11 = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
 
        mycursor11 = database11.cursor()
        sql11 = 'UPDATE student_table SET studName =%s ,studRoll=%s,studDept=%s WHERE studRoll=%s'   
        kk =  screen_manager.get_screen("Admin").ids.name1.text
        kk1 =screen_manager.get_screen("Admin").ids.rollno2.text
        kk2 = screen_manager.get_screen("Admin").ids.department2.text
        values11 =[kk,kk1,kk2,kk1]
        mycursor11.execute(sql11,values11)
        self.dialog1.dismiss()
        database11.commit()
                
    #add dialog box
    def show_alert_dialog(self):
        
        self.dialog = MDDialog(
            title = "Check Data",
            text= "Press Ok to Save",
            buttons=[
                MDFlatButton(
                    text="Ok",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.manageuser,
                    
                ),
                MDRaisedButton(
                    text="DISCARD",
                    md_bg_color = "red" ,
                    on_release=self.close,
                    
                ),
            ],
        )
        self.dialog.open()  
         
    #add close   
    def close(self,obj):
        self.dialog.dismiss()   
        
    #save canteen user data
    def manageuser(self,obj):
        database1 = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        mycursor1 = database1.cursor()
        sql = 'INSERT INTO login_table(name,canteenname,username,passw,apprights) VALUES(%s,%s,%s,%s,%s)'
    
        kk = screen_manager.get_screen("Admin").ids.name4.text
        kk1 = screen_manager.get_screen("Admin").ids.Canteen_Name2.text
        kk2 = screen_manager.get_screen("Admin").ids.username.text
        kk3 = screen_manager.get_screen("Admin").ids.password4.text
        kk4 = screen_manager.get_screen("Admin").ids.apprights.text
        values =[kk,kk1,kk2,kk3,kk4]
        mycursor1.execute(sql,values)
        database1.commit()
        self.dialog.dismiss()
        
    #update canteen user data
    #update dialog box   
    def Cupdate(self):
        self.Cupdate1 = MDDialog(
            title = "Check Data",
            text= "Press Ok to Save",
            buttons=[
                MDFlatButton(
                    text="Ok",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.UpdateCanteen,
                    
                ),
                MDRaisedButton(
                    text="DISCARD",
                    md_bg_color = "red" ,
                    on_release=self.close2,                        
                ),
            ],
        )
        self.Cupdate1.open()
        
    def close2(self,obj):
        self.Cupdate1.dismiss()
        
    #update student data
    def UpdateCanteen(self,obj):
        
        database11 = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
 
        mycursor11 = database11.cursor()
        sql11 = 'UPDATE login_table SET name = %s,canteenname = %s,username = %s, passw = %s, apprights = %s WHERE canteenname=%s'   
        kk = screen_manager.get_screen("Admin").ids.name4.text
        kk1 = screen_manager.get_screen("Admin").ids.Canteen_Name2.text
        kk2 = screen_manager.get_screen("Admin").ids.username.text
        kk3 = screen_manager.get_screen("Admin").ids.password4.text
        kk4 = screen_manager.get_screen("Admin").ids.apprights.text
        values11 =[kk,kk1,kk2,kk3,kk4,kk1]
        mycursor11.execute(sql11,values11)
        self.Cupdate1.dismiss()
        database11.commit() 

    #Report Date Pickers    
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        from_date.append(value)
        date_format = "%Y-%m-%d"
        textt = value.strftime(date_format)
        screen_manager.get_screen("Admin").ids.f_date.text = textt
        
     
        """
        self.text_field = MDTextField(
            pos_hint = {'center_x': .86,'center_y':.7},
        )
        self.text_field.text = str(textt)
        screen_manager.get_screen("Admin").ids.r_screen.add_widget(self.text_field)"""
        
    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
    
    #report dropdown
    def dropdown(self,button):   
        self.menu.caller = button
        self.menu.open()  
    #user dropdown
    def user_n(self,buttons):
        self.me.caller = buttons
        self.me.open()
    
    def aprs_sel(self,but):
        self.aprs.caller = but
        self.aprs.open()
        
    #user name
    def user_name(self):
          screen_manager.get_screen("Admin").ids.apprights.text = "User"
          self.me.dismiss()
        
    #aprs name
    def aprsk_name(self):
          screen_manager.get_screen("signup").ids.apprights.text = "User"
          self.aprs.dismiss() 
          
    def aprsk_name1(self):
          screen_manager.get_screen("signup").ids.apprights.text = "Admin"
          self.aprs.dismiss()
    #add aprs in add canteen
    def add_apr(self,kir):
        self.add.caller = kir
        self.add.open()
        
    def add_apr_user(self):
        screen_manager.get_screen("Admin").ids.apprights3.text = "User"
        self.add.dismiss()
        
    def MovetoRequestScreen(self):
        self.root.current = "Requests"

    def MovetoPreviousScreen(self):
        self.root.current = "Admin"

    def send_data(self, name, canteen_name, user_name, passw, apprights):
       #here is the function to send data from python to mysql
       try:
               self.cursor.execute(f"INSERT INTO request_table (req_name, req_canteenname, req_username, req_passw, req_apprights, req_status) VALUES('{name.text}', '{canteen_name.text}', '{user_name.text}', '{passw.text}', '{apprights.text}', 'Pending')")     
               self.database.commit() #this is importnt to insert query to database
               name.text = ""
               canteen_name.text = ""
               user_name.text = ""
               passw.text = ""
               apprights.text = ""
               print("Values successfully inserted!")
       except Exception as e:
            print(e)
       finally:
            print("Send data function ends here")
            self.root.current = "login"

    def show_date_picker1(self):
        date_dialog1 = MDDatePicker()
        date_dialog1.bind(on_save=self.on_save1, on_cancel=self.on_cancel1)
        date_dialog1.open()
    
       
    def on_save1(self, instance1, value1, date_range1):
        database1 = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
   

        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance1: <kivymd.uix.picker.MDDatePicker object>;

        :param value1: selected date;
        :type value1: <class 'datetime.date'>;

        :param date_range1: list of 'datetime.date' objects in the selected range;
        :type date_range1: <class 'list'>;
        '''
        
        to_date.append(value1)      
        date_format = "%Y-%m-%d"
        textt = value1.strftime(date_format)
        can_food.clear()
        lunch1.clear()
        price1.clear()
        snaks1.clear()
        
        screen_manager.get_screen("Admin").ids.t_date.text = textt  
        fro = screen_manager.get_screen("Admin").ids.f_date.text
        to=screen_manager.get_screen("Admin").ids.t_date.text
        # nn = canteen name
        nn = screen_manager.get_screen("Admin").ids.Can_Name.text

        #total amount 
        database = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        mycursor = database.cursor()      
        query = f"SELECT * FROM canteen_table WHERE canteenname='{nn}' AND entryDateTime >= '{fro}' AND entryDateTime <= '{to}'"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        for i in myresult:
            can_food.append(i)

        
        l = "Lunch"
        s = "Snack"
        lunch_price = 40
        snack_price = 30
        
        for k in can_food:
            if l in k:
                lunch1.append(k)
                price1.append(lunch_price)
            elif s in k:
                snaks1.append(k)
                price1.append(snack_price)
                
        total_amount_lunch = len(lunch1)*40
        total_amount_snacks = len(snaks1)*30
        payment = total_amount_lunch + total_amount_snacks
        screen_manager.get_screen("Admin").ids.totals.text = str(payment)
        
    def on_cancel1(self, instance1, value1):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
    #genrating breif report  
    def genrate_report(self):
        
        can_food1.clear()
        snaks.clear()
        price.clear()
        lunch.clear()
        Can_no.clear()
        Can_date.clear()
        Can_Food.clear()
        Can_Name.clear()
        
        fro = screen_manager.get_screen("Admin").ids.f_date.text
        to=screen_manager.get_screen("Admin").ids.t_date.text
        # nn = canteen name
        nn = screen_manager.get_screen("Admin").ids.Can_Name.text

        #total amount 
        database = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        mycursor = database.cursor()      
        query = f"SELECT * FROM canteen_table WHERE canteenname='{nn}' AND entryDateTime >= '{fro}' AND entryDateTime <= '{to}'"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        for i in myresult:
            can_food1.append(i)
            
        l = "Lunch"
        s = "Snack"
        lunch_price = 40
        snack_price = 30
        
        for k in can_food1:
            if l in k:
                lunch.append(k)
                price.append(lunch_price)
                
            elif s in k:
                snaks.append(k)
                price.append(snack_price)
                
        for i in can_food1:
            Can_no.append(i[0])
            Can_date.append(i[1])
            Can_Food.append(i[2])
            Can_Name.append(i[5])
            
        dd = list(zip(Can_no,Can_date,Can_Food,Can_Name,price))           
        df = pd.DataFrame(dd,columns=['No','Date','Food','Canteen Name','Cost'])
        df.to_excel("Brief_report{}.xlsx".format(pd.datetime.today().strftime('%Y-%m-%d %H_%M_%S')))
        
    #canteen delete drop down call function 
    def Canteendown(self,button):   
        self.canteen_delete.caller = button
        self.canteen_delete.open()    

    def receive_data(self, name, password):
        #here is the function to receive data from mysql to python and validate it with text field text
        self.cursor.execute("SELECT * FROM login_table")
        name_list = []
        for i in self.cursor.fetchall():
            name_list.append(i[3])
        if name.text in name_list and name.text !="":
            self.cursor.execute(f"SELECT passw FROM login_table WHERE username='{name.text}'")
            for j in self.cursor:
                if password.text == j[0]:
                    connections = Db_Operations()
                    AppRights = connections.Check_Apprights(name.text, password.text)
                    if AppRights == 'User':
                        print("You have Successfully Logged In !!")
                        self.root.current = "bottom"
                        Canteen_name = connections.Get_CanteenName(name.text, password.text)
                        FullName = connections.Get_FullName(name.text, password.text)
                        self.root.get_screen("bottom").ids.username.text = name.text
                        self.root.get_screen("bottom").ids.Canteen_Name.text = Canteen_name
                        self.root.get_screen("bottom").ids.email.text = FullName
                        self.root.get_screen('bottom').ids.username.text = name.text
                    else:
                        self.root.current = "Admin"
                else:
                    print("Incorrect Password")
        else:
            print("Invalid Username")

    def Detailed_report(self):
        can_food2.clear()
        det_snaks.clear()
        det_price.clear()
        det_lunch.clear()
        Can_no1.clear()
        Can_date1.clear()
        Can_Food1.clear()
        Stu_Name.clear()
        Stu_roll.clear()
        Can_Name1.clear()
        
        fro = screen_manager.get_screen("Admin").ids.f_date.text
        to=screen_manager.get_screen("Admin").ids.t_date.text
        # nn = canteen name
        nn = screen_manager.get_screen("Admin").ids.Can_Name.text

        #total amount 
        database = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        mycursor = database.cursor()      
        query = f"SELECT * FROM canteen_table WHERE canteenname='{nn}' AND entryDateTime >= '{fro}' AND entryDateTime <= '{to}'"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        for i in myresult:
            can_food2.append(i)
        
        l = "Lunch"
        s = "Snack"
        lunch_price = 40
        snack_price = 30
        
        for k in can_food2:
            if l in k:
                det_lunch.append(k)
                det_price.append(lunch_price)
            elif s in k:
                det_snaks.append(k)
                det_price.append(snack_price)
        for i in can_food2:
            Can_no1.append(i[0])
            Can_date1.append(i[1])
            Can_Food1.append(i[2])
            Stu_Name.append(i[3])
            Stu_roll.append(i[4])
            Can_Name1.append(i[5])
            
        dd = list(zip(Can_no,Can_date,Can_Food,Stu_Name,Stu_roll,Can_Name,det_price))           
        df = pd.DataFrame(dd,columns=['No','Date','Food','Student Name','RollNo','Canteen Name','Cost'])
        df.to_excel("Detailed_report{}.xlsx".format(pd.datetime.today().strftime('%Y-%m-%d %H_%M_%S')))
        
    def Attendance_report(self):
        names.clear()
        rollno.clear()
        counts.clear()
        database = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        mycursor = database.cursor(buffered=True)
        mycursor1 = database.cursor(buffered=True)    
        mycursor2 = database.cursor(buffered=True)  
          
        mycursor.execute("SELECT entryDateTime FROM canteen_table ")
        myresult = mycursor.fetchall()     
        
        mycursor.execute("SELECT studName FROM canteen_table ")
        
        mycursor2.execute("SELECT studRoll FROM canteen_table ")
        
        for x in myresult:
            Att_date.append(x)
            
        mycursor1.execute("SELECT food_category FROM canteen_table ")
        
        start_date = from_date[0]
        end_date = to_date[0]
        delta = timedelta(days=1)
        
        while start_date <= end_date:
            dd = start_date
            start_date += delta
            Att_date1.append(dd)            
                
        for y in Att_date:
            for z in Att_date1:
                if z in y:
                    rr=mycursor1.fetchone()
                    myresult2 = mycursor.fetchone()  
                    myresult3 = mycursor2.fetchone()
                    Att_name.append(myresult2)
                    Att_roll.append(myresult3)
                    Att_food.append(rr)
                    Att_t.append(z)
        
        for k in Att_name:
            if k not in names:
                names.append(k)

        for s in Att_roll:       
            if s not in rollno:
                rollno.append(s)
                
        for l in Att_roll:
            c = Att_roll.count(l)
            counts.append(c)
            

        dd = list(zip(names,rollno,counts))    
        df = pd.DataFrame(dd,columns=['Name','RollNo','No of Presant'])
        df.to_excel("Attendence_report{}.xlsx".format(pd.datetime.today().strftime('%Y-%m-%d %H_%M_%S')))   
          
    def PendingRequests(self):
        connections = Db_Operations()
        values = connections.Get_PendingRequests()
        return values
    
    # def Show_DataTable(self):
    #     self.root.current = "DataTable"

class Db_Operations:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='@Harishvenkat2000',
            database='silverpos'
        )
        self.mycursor = self.mydb.cursor()
        self.studRoll = ""

    def get_studentDetails(self):
        _student = OrderedDict()
        _student['studRoll'] = {}
        global studRolls
        studRolls = []
        sql = "SELECT * FROM student_table"
        self.mycursor.execute(sql)
        students = self.mycursor.fetchall()
        for student in students:
            studRolls.append(student[3])
        users_length = len(studRolls)
        idx = 0
        while idx < users_length:
            _student['studRoll'][idx] = studRolls[idx]
            idx += 1
    
    def set_rollno(self, rollno):
        self.studRoll = rollno
        print("Roll Number: "+ self.studRoll)
        _stud = OrderedDict()
        _stud['studName'] = {}
        global studName
        studName = ''
        sql = "SELECT * FROM student_table WHERE studRoll = '" +  rollno + "'"
        self.mycursor.execute(sql)
        studs = self.mycursor.fetchall()
        for stud in studs:
            studName = f'{studName}{stud[2]}'
        print("N: "+studName)
        print("N: " + rollno)
        return studName
    
    def Last_Date(self, studentRoll, category):
        LDate = ''
        sql = "SELECT MAX(entryDateTime) FROM canteen_table WHERE studRoll = '" + studentRoll + "' AND food_category = '" + category + "'"
        self.mycursor.execute(sql)
        LDates = self.mycursor.fetchall()
        for LDat in LDates:
            LDate = f'{LDate}{LDat[0]}'
        print("Last Time Student Ate on: " + LDate)
        return LDate
    
    def Check_Apprights(self, user_name, password):
        AppRight = ''
        sql = "SELECT apprights FROM login_table WHERE username='"+user_name+"' AND passw = '"+password+"'"
        self.mycursor.execute(sql)
        AppRights = self.mycursor.fetchall()
        for AppRigh in AppRights:
            AppRight = f'{AppRight}{AppRigh[0]}'
        print("The user is a " + AppRight)
        return AppRight
    
    def Get_CanteenName(self, user_name, password):  
        Canteen_name = ""
        sql = "SELECT canteenname FROM login_table WHERE username = '" + user_name + "' AND passw = '" + password + "'"
        self.mycursor.execute(sql)
        Canteen_names = self.mycursor.fetchall()
        for Canteen in Canteen_names:
            Canteen_name = f'{Canteen_name}{Canteen[0]}'
        print("The Canteen Name is: " + Canteen_name)
        return Canteen_name
    
    def Get_FullName(self, user_name, password):
        FullName = ""
        sql = "SELECT name FROM login_table WHERE username = '" + user_name + "' AND passw = '" + password + "'"
        self.mycursor.execute(sql)
        FullNames = self.mycursor.fetchall()
        for Name in FullNames:
            FullName = f'{FullName}{Name[0]}'
        print('The Full Name is: ' + FullName)
        return FullName
    
    def Get_PendingRequests(self):
        sql = "SELECT req_username FROM request_table WHERE req_status = 'Pending'"
        self.mycursor.execute(sql)
        userNames = self.mycursor.fetchall()
        return userNames

TopTool = """

MDBoxLayout:
    orientation: "vertical"

    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_y": .95}
        user_font_size: "30sp"
        theme_text_color: "Custom"
        text_color: rgba(26, 24, 58, 255)
        on_release:
            app.root.transition.direction = "right"
            app.root.current = "bottom"

    MDLabel:
        text: "                          Scan QR"
        font_name: "Poppins"   
        font_size: "18sp"
        pos_hint: {"center_x" : .5}

    MDLabel:
        text: " "
        font_name: "Poppins"   
        font_size: "18sp"	
    MDLabel:
        text: " "
        font_name: "Poppins"   
        font_size: "18sp"
    MDLabel:
        text: " "
        font_name: "Poppins"   
        font_size: "18sp"

"""

class QrScanner(Screen):
    def __init__(self, **kwargs):
       super(QrScanner,self).__init__(**kwargs)
    #    layout=MDBoxLayout(orientation='vertical')
    #    TopBar = MDTopAppBar(title = "QRScanner", font_name= "Poppins/Poppins-SemiBold.ttf", font_size= "26sp", pos_hint= {"center_x": .5, "center_y": .1}, text_color = (0.49, 0.498, 0.498, 1), left_action_items = ([["arrow-left-circle-outline", lambda x : app.root.current = "bottom"]]))
       #, left_action_items = [["arrow-left-circle-outline", lambda *args : setattr(self.manager, "current", "third")]]
       #ViewReport = MDFlatButton(text = "View Report", on_press = self.MovetoFourScreen, pos_hint = {'center_x': 0.5, 'center_y': 0.2})
       TopTools = Builder.load_string(TopTool)
       self.add_widget(TopTools)
       self.image=Image()
       self.add_widget(self.image)
        #self.save_img_button=(MDFillRoundFlatButton(text="Detect URL",pos_hint={'center_x':0.5,'center_y':0.3},size_hint=(None,None)))
        #self.save_img_button.bind(on_press=self.take_picture)
        #layout.add_widget(self.save_img_button)
       self.capture=cv2.VideoCapture(0)
       self.detector = cv2.QRCodeDetector()
       Clock.schedule_interval(self.load_video,1.0/30.0)
       #self.add_widget(ViewReport)

    def load_video(self,*args):
        ret,frame=self.capture.read()
        for code in decode(frame):
            print(code.data.decode('utf-8'))
            time.sleep(0.5)
            connections = Db_Operations()
            values = connections.get_studentDetails()
            if code.data.decode('utf-8') in studRolls:
                global studentRollnumber
                studentRollnumber = code.data.decode('utf-8')
                val = connections.set_rollno(studentRollnumber)
                Canteen_name = self.manager.get_screen("bottom").ids.Canteen_Name.text
                self.manager.get_screen("details").ids.student_name.text = val.title()
                self.manager.get_screen("details").ids.canteen_name.text = Canteen_name
                self.MovetoFourScreen(studentRollnumber)
            else:
               self.dialog = MDDialog(
                text="Invalid QR",
                buttons=[
                    MDFlatButton(
                        text="Ok",
                        on_press = self.RemainSameScreen
                    ),
                ],)
               self.dialog.open()
        self.image_frame=frame
        buffer=cv2.flip(frame,0).tobytes()
        texture=Texture.create(size=(frame.shape[1],frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture
    
    def RemainSameScreen(self, *args):
        self.dialog.dismiss(force=True)

    def MovetoFourScreen(self, roll_no):
        self.manager.get_screen("details").ids.roll_number.text = roll_no
        self.manager.current = "details"

if __name__ == "__main__":
    LabelBase.register(name="Poppins", fn_regular="C:\\Users\\hp\\Downloads\\APK\APK\\Sample\\Sample\\Poppins\\Poppins-Black.ttf")
    LabelBase.register(name="MPoppins", fn_regular="C:\\Users\\hp\\Downloads\\APK\APK\\Sample\\Sample\\Poppins\\Poppins-Medium.ttf")
    LabelBase.register(name="SPoppins", fn_regular="C:\\Users\\hp\\Downloads\\APK\APK\\Sample\\Sample\\Poppins\\Poppins-SemiBold.ttf")
    LabelBase.register(name="BPoppins", fn_regular="C:\\Users\\hp\\Downloads\\APK\APK\\Sample\\Sample\\Poppins\\Poppins-Regular.ttf")
    LoginPage().run()