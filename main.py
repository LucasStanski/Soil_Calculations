from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
KV='''
<PrimeiraJanela>:
    name: "PrimeiraJanela"
    
    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "cyan"
        text_color_active: "cyan"

        MDBottomNavigationItem:
            name: 'HOME'
            text: 'Início'
            icon: 'home'
            
            MDFillRoundFlatButton:
                text: "  Soma De Bases"
                text_color: "black"
                font_size: 20
                size_hint_y:0.0
                size_hint_x:0.5
                font_style:'H6'
                line_color: 0, 0, 0, 0               
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release: 
                    root.manager.current = 'Soma De Bases'
                    root.manager.transition.direction='left'
                    
            MDFillRoundFlatButton:
                text: "  Capacidade de Troca Catiônica"
                text_color: "black"
                font_size: 20
                size_hint_y:0.0
                size_hint_x:0.5
                font_style:'H6'
                line_color: 0, 0, 0, 0                
                pos_hint: {"center_x": .5, "center_y": .6}
                on_release: 
                    root.manager.current = 'Capacidade de troca catiônica'
                    root.manager.transition.direction='left'
            MDFillRoundFlatButton:
                text: "  Saturação de Bases"
                text_color: "black"
                font_size: 20
                size_hint_y:0.0
                size_hint_x:0.5
                font_style:'H6'
                line_color: 0, 0, 0, 0
                pos_hint: {"center_x": .5, "center_y": .7}
                on_release: 
                    root.manager.current = 'Saturação de Bases'
                    root.manager.transition.direction='left'
                    
            MDFillRoundFlatButton:
                text: "  Necessidade de Calcário"
                text_color: "black"
                font_size: 20
                size_hint_y:0.0
                size_hint_x:0.5
                font_style:'H6'
                line_color: 0, 0, 0, 0
                pos_hint: {"center_x": 0.5, "center_y": 0.4}
                on_release: 
                    root.manager.current = 'Necessidade de calcário'
                    root.manager.transition.direction='left'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Informações'
            icon: 'twitter'
            

<SegundaJanela>:  
    name:"Soma De Bases" 
    MDBottomAppBar:
        MDTopAppBar:
            title: "Title"
            icon: "undo"
            type: "bottom"
            mode: "end"
            on_action_button:
                app.root.current='PrimeiraJanela'
                root.manager.transition.direction='right'
    MDTextField:
        id:dois_calcio
        hint_text: "Calcio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .7}
        
    MDTextField:
        id:dois_magnesio
        hint_text: "Magnésio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .6}
        
    MDTextField:
        id:dois_potassio
        hint_text: "Potassio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .5}
        
    MDTextField:
        id:dois_sodio
        hint_text: "Sódio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .4}
    
    MDLabel:
        id:dois_res
        text: ""
        halign: "center"
        font_size:30
        pos_hint: {"center_x": .7, "center_y": .3}
    MDRectangleFlatButton:
        text: "Resultado"
        theme_text_color: "Custom"
        text_color: "white"
        line_color: "cyan"
        pos_hint: {"center_x": .3, "center_y": .3}
        on_press:root.sb()
        
<TerceiraJanela>:
    name:"Capacidade de troca catiônica"
    MDBottomAppBar:
        MDTopAppBar:
            title: "Title"
            icon: "undo"
            type: "bottom"
            mode: "end"
            on_action_button:
                app.root.current='PrimeiraJanela'
                root.manager.transition.direction='right'
    MDTextField:
        id:tres_calcio
        hint_text: "Calcio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .8}
        
    MDTextField:
        id:tres_magnesio
        hint_text: "Magnésio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .7}
        
    MDTextField:
        id:tres_potassio
        hint_text: "Potassio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .6}
        
    MDTextField:
        id:tres_sodio
        hint_text: "Sódio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .5}
        
    MDTextField:
        id:tres_hal
        hint_text: "Hidrogénio+Alumínio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .4}
    MDLabel:
        id:tres_resposta
        text: ""
        halign: "center"
        font_size:30
        pos_hint: {"center_x": .7, "center_y": .3}
    MDRectangleFlatButton:
        text: "Resultado"
        theme_text_color: "Custom"
        text_color: "white"
        line_color: "cyan"
        pos_hint: {"center_x": .3, "center_y": .3}
        on_press:root.ctc()

<QuartaJanela>:
    name:"Saturação de Bases"
    MDBottomAppBar:
        MDTopAppBar:
            title: "Title"
            icon: "undo"
            type: "bottom"
            mode: "end"
            on_action_button:
                app.root.current='PrimeiraJanela'
                root.manager.transition.direction='right'
    MDTextField:
        id:quatro_calcio
        hint_text: "Calcio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .8}
        
    MDTextField:
        id:quatro_magnesio
        hint_text: "Magnésio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .7}
        
    MDTextField:
        id:quatro_potassio
        hint_text: "Potassio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .6}
        
    MDTextField:
        id:quatro_sodio
        hint_text: "Sódio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .5}
        
    MDTextField:
        id:quatro_hal
        hint_text: "Hidrogénio+Alumínio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .4}
    MDLabel:
        id:quatro_resposta
        text: ""
        halign: "center"
        font_size:30
        pos_hint: {"center_x": .7, "center_y": .3}
    MDRectangleFlatButton:
        text: "Resultado"
        theme_text_color: "Custom"
        text_color: "white"
        line_color: "cyan"
        pos_hint: {"center_x": .3, "center_y": .3}
        on_press:root.sdb()

<QuintaJanela>:
    name:"Necessidade de calcário" 
    MDBottomAppBar:
        MDTopAppBar:
            title: "Title"
            icon: "undo"
            type: "bottom"
            mode: "end"
            on_action_button:
                app.root.current='PrimeiraJanela'
                root.manager.transition.direction='right'
    MDTextField:
        id:cinco_calcio
        hint_text: "Calcio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .9}
        
    MDTextField:
        id:cinco_magnesio
        hint_text: "Magnésio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .8}
        
    MDTextField:
        id:cinco_potassio
        hint_text: "Potassio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .7}
        
    MDTextField:
        id:cinco_sodio
        hint_text: "Sódio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .6}
        
    MDTextField:
        id:cinco_hal
        hint_text: "Hidrogénio+Alumínio"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .5}
    MDTextField:
        id:cinco_calcario
        hint_text: "% do Calcario"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .4}
    MDTextField:
        id:cinco_v_cultura
        hint_text: "V% da Cultura"
        mode: "rectangle"
        line_color: "black"
        text_color: "black"
        font_size: 13
        icon_size:30
        size_hint_y: .09
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .3}
    MDLabel:
        id:cinco_resposta
        text: ""
        halign: "center"
        font_size:30
        pos_hint: {"center_x": .7, "center_y": .2}
    MDRectangleFlatButton:
        text: "Resultado"
        theme_text_color: "Custom"
        text_color: "white"
        line_color: "cyan"
        pos_hint: {"center_x": .3, "center_y": .2}
        on_press:root.nc()
'''

class PrimeiraJanela(MDScreen):
    pass
class SegundaJanela(MDScreen):
    def sb(self):
        ca=float(self.ids.dois_calcio.text)
        mg=float(self.ids.dois_magnesio.text)
        k=float(self.ids.dois_potassio.text)
        na=float(self.ids.dois_sodio.text)
        sb=ca+mg+k+na
        self.ids.dois_res.text="{:0.2f}".format(sb)
        
class TerceiraJanela(MDScreen):
    def ctc(self):
        ca=float(self.ids.tres_calcio.text)
        mg=float(self.ids.tres_magnesio.text)
        k=float(self.ids.tres_potassio.text)
        na=float(self.ids.tres_sodio.text)
        hal=float(self.ids.tres_hal.text)
        sb=ca+mg+k+na
        ctc=sb+hal
        self.ids.tres_resposta.text="{:0.2f}".format(ctc)
        
class QuartaJanela(MDScreen):
    def sdb(self):
        ca=float(self.ids.quatro_calcio.text)
        mg=float(self.ids.quatro_magnesio.text)
        k=float(self.ids.quatro_potassio.text)
        na=float(self.ids.quatro_sodio.text)
        hal=float(self.ids.quatro_hal.text)
        sb=ca+mg+k+na
        ctc=sb+hal
        v1=sb*100/ctc
        self.ids.quatro_resposta.text="{:0.2f}".format(v1)+"%"
        
class QuintaJanela(MDScreen):
    def nc(self):
        ca=float(self.ids.cinco_calcio.text)
        mg=float(self.ids.cinco_magnesio.text)
        k=float(self.ids.cinco_potassio.text)
        na=float(self.ids.cinco_sodio.text)
        hal=float(self.ids.cinco_hal.text)
        calc=float(self.ids.cinco_calcario.text)
        v2=float(self.ids.cinco_v_cultura.text)
        sb=ca+mg+k+na
        ctc=sb+hal
        v1=sb*100/ctc
        nc=(v2-v1)*ctc/calc
        self.ids.cinco_resposta.text="{:0.1f}".format(nc)+" t/ha"
    
class ContentNavigationDrawer(MDBoxLayout):
    pass

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        Builder.load_string(KV)
        sm=MDScreenManager()
        sm.add_widget(PrimeiraJanela())
        sm.add_widget(SegundaJanela())
        sm.add_widget(TerceiraJanela())
        sm.add_widget(QuartaJanela())
        sm.add_widget(QuintaJanela())
        return sm

MyApp().run()            