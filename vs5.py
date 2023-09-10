from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDRectangleFlatButton
from kivy.metrics import dp
from kivymd.uix.toolbar import MDTopAppBar
from kivy.clock import Clock
from kivymd.uix.snackbar import Snackbar


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Purple"
        self.layout = MDBoxLayout(orientation='vertical',padding="10dp",spacing="10dp")

        # Create text fields
        self.bar=MDTopAppBar(title="Billing app",pos_hint={'top':1},left_action_items=[["apple"]]
                             ,anchor_title="left",right_action_items=[["share-all", lambda x: self.Ariapp]])
        self.text_field1 = MDTextField(hint_text="Name",mode="rectangle",size_hint_x=.8)
        self.text_field2 = MDTextField(hint_text="Quantity",mode="rectangle",size_hint_x=.8)
        self.text_field3 = MDTextField(hint_text="Price",mode="rectangle",size_hint_x=.8)

        # Create button
        self.layout1=MDBoxLayout(orientation= 'horizontal',padding="10dp",adaptive_height= True,spacing="20dp")
        
        button =MDRectangleFlatButton(text="Insert", on_release=self.insert_data,pos_hint={'top':1})
        button1=MDRectangleFlatButton(text="delete",on_release=self.delete_checked_rows,pos_hint={'top':1})
        
        self.layout1.add_widget(button)
        self.layout1.add_widget(button1)

        # Add widgets to layout
        self.layout.add_widget(self.bar)
        self.layout.add_widget(self.text_field1)
        self.layout.add_widget(self.text_field2)
        self.layout.add_widget(self.text_field3)
        self.layout.add_widget(self.layout1)
        self.data_table = MDDataTable(
            size_hint=(0.6, 0.6),
            check=True,
            pos_hint={'center_x': 0.5,'center_y': 0.5},
            size_hint_x=0.8,
            column_data=[
                ("Name", dp(30)),
                ("Quantity", dp(20)),
                ("Price", dp(20))
            ],
            row_data=[],
            background_color_header="#3e0a63",
            background_color_cell="#d4a1d4",
        )
        self.data_table.bind(on_check_press=self.Ariapp)
        self.layout.add_widget(self.data_table)

        return self.layout

    def insert_data(self, instance):
        # Get the values from the text fields
        value1 = self.text_field1.text
        value2 = self.text_field2.text
        value3 = self.text_field3.text
        self.data_table.add_row((value1,value2,value3))
    
    def delete_checked_rows(self,*args):
       if len(self.data_table.row_data) > 0:
            self.data_table.remove_row(self.data_table.row_data[-1])
            
    def Ariapp(self,instance_table, instance_row):
          data=self.data_table.row_data
          print(data)
          
        


MyApp().run()