import kivy
import random 

from Chatbot import Chatbotresponse
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.image import Image, AsyncImage
from kivy.config import Config

Config.set('graphics', 'resizable', True)
Config.window_icon = "m.ico"

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

ice_breakers = ['Hey there Human', 'Yohoo', 'Hello anonymous', 'Whats up', 'Hey, How are you', 'What can I help you with', 'Today is a great day to talk to a chatbot', 'So today you did not find a human to talk to', 'hmmm you talk to computers wow you are a strange person', 'Not that many people talk to a computer', 'Hey are you feeling lonely', 'Hi, I felt like coming up to you and say hi', 'You lonely today']



#----------------------------------------------------------------------
class Chattr(App):
    
       def on_key_down(self, instance, keyboard, keycode, text, modifiers):
              if keycode == 40:
                     self.sent(None)
                     
       def build(self):
        
        main_layout = BoxLayout(padding=(10, 0), orientation="vertical")
        
        wimg = Image(source='s.png')
        wimg.allow_stretch = True
        wimg.keep_ratio = False
        wimg.size_hint_x = 1
        wimg.size_hint_y = 0.2
        
        scroll_container = BoxLayout(orientation="vertical",size_hint=(1,0.90))
        self.layout = BoxLayout(padding=(15,10),orientation="vertical", spacing=50, size_hint_y=None)
        self.layout.bind(minimum_height= self.layout.setter('height'))

        colors = [red, green, blue, purple]

        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height*0.70))
        
        root.add_widget(self.layout)
        

       

        
        bottom_layout = BoxLayout(padding=10,orientation="horizontal", size_hint=(1,0.1))
        
        self.textinput = TextInput(hint_text="Say something ", background_color=random.choice(colors), size_hint=(0.8,1))
       
        btn3 = Button(text="Send",background_color=random.choice(colors), size_hint=(0.2, 1))
        
        btn3.bind(on_press=self.sent)
        
        
        bottom_layout.add_widget(self.textinput)
        bottom_layout.add_widget(btn3)

        scroll_container.add_widget(root)
        main_layout.add_widget(wimg)
        main_layout.add_widget(scroll_container)
        main_layout.add_widget(bottom_layout)
        Window.bind(on_key_down=self.on_key_down)
        
        btn = Label(padding=(0,0),text= "Bot> " + random.choice(ice_breakers),color=(1,0,1,1),size_hint=(1.0,1.0), halign="left", valign="middle")
        btn.bind(size=btn.setter('text_size'))
        
        self.layout.add_widget(btn)
        

        return main_layout
       
       def sent(self,event):
              
        self.textinput.hint_text = ""     
        user_input = self.textinput.text
        response = Chatbotresponse(user_input)
        self.textinput.text = ""
        btn1 = Label(padding=(0,0),text=str(user_input),color=(0,1,0,1),size_hint=(1.0,1.0), halign="left", valign="middle")
        btn1.bind(size=btn1.setter('text_size'))
        self.layout.add_widget(btn1)
        btn = Label(padding=(0,0),text="Bot> " + str(response),color=(1,0,1,1),size_hint=(1.0,1.0), halign="left", valign="middle")
        btn.bind(size=btn.setter('text_size'))
        self.layout.add_widget(btn)
       
       
        

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = Chattr()
    app.run()
