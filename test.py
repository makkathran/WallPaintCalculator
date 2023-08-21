from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.popup import Popup
osz_ablak = 0
osz_ablak2 = 0

class Tab(MDFloatLayout, MDTabsBase):
    pass


class Tab1(MDFloatLayout, MDTabsBase):
    pass


class P(MDFloatLayout):
    pass


class TestApp(MDApp):

    def ablak_create_text_fields(self):
        number_of_text_fields = int(self.root.ids.number_input.text)
        self.root.ids.text_field_container.clear_widgets()
        for i in range(number_of_text_fields):
            self.root.ids.text_field_container.add_widget(
                MDTextField(hint_text="{}. Ablak szélessége [cm]".format(i + 1), id=f"ablakszelessege_{i}"))
            self.root.ids.text_field_container.add_widget(
                MDTextField(hint_text="{}. Ablak magassága [cm]".format(i + 1), id=f"ablakmagassaga_{i}"))
            # print(f"ablakszelessege_{i}")
            # print(f"ablakmagassaga_{i}")
        return number_of_text_fields

    def ajto_create_text_fields(self):
        number_of_text_fields_2 = int(self.root.ids.number_input2.text)
        self.root.ids.text_field_container2.clear_widgets()
        for i in range(number_of_text_fields_2):
            self.root.ids.text_field_container2.add_widget(
                MDTextField(hint_text="{}. Ajtó szélessége [cm]".format(i + 1), id=f"ajtoszelessege_{i}"))
            self.root.ids.text_field_container2.add_widget(
                MDTextField(hint_text="{}. Ajtó magassága [cm]".format(i + 1), id=f"ajtomagassaga_{i}"))
            # print(ablakszelessege_0)
            # print(f"ablakmagassaga_{i}")

    def build(self):
        return Builder.load_file("test.kv")

    def idmeghat(self):
        # ezzel tudom kiiratni az id értékeket
        text_field_value = self.root.ids.text_field_container.children[0].text
        print(text_field_value)
        my_list = []
        ism = int(self.root.ids.number_input.text)
        for i in range(ism*2):
            my_list.append(self.root.ids.text_field_container.children[i].text)
        my_list.reverse()
        print(my_list)
        my_list_szel = my_list[::2]
        my_list_mag = my_list[1::2]
        my_list_osz = []
        for i in range(ism):
            my_list_osz.append(int(my_list_szel[i])*int(my_list_mag[i]))
        print(my_list_osz)
        global osz_ablak
        osz_ablak = (sum(my_list_osz))

    def idmeghat2(self):
        text_field_value2 = self.root.ids.text_field_container2.children[-1].text
        print(text_field_value2)
        my_list2 = []
        ism = int(self.root.ids.number_input2.text)
        for i in range(ism*2):
            my_list2.append(self.root.ids.text_field_container2.children[i].text)
        my_list2.reverse()
        print(my_list2)
        my_list_szel2 = my_list2[::2]
        my_list_mag2 = my_list2[1::2]
        my_list_osz2 = []
        for i in range(ism):
            my_list_osz2.append(int(my_list_szel2[i])*int(my_list_mag2[i]))
        print(my_list_osz2)
        global osz_ablak2
        osz_ablak2 = (sum(my_list_osz2))

    def information(self):
        show = P()
        print("Hello")
        popupWindow = Popup(title="Information", title_color=(0, 0, 0), content=show, size_hint=(0.8, 0.8),
                            auto_dismiss=True,
                            separator_color="#9B817C",
                            background_color=(255, 255, 255))
        popupWindow.open()

    def falszamitas(self):
        q = int(self.root.ids.Aszel.text)
        w = int(self.root.ids.Amag.text)
        e = int(self.root.ids.Bszel.text)
        r = int(self.root.ids.Bmag.text)
        t = int(self.root.ids.Cszel.text)
        z = int(self.root.ids.Cmag.text)
        u = int(self.root.ids.Dszel.text)
        i = int(self.root.ids.Dmag.text)

        t2 = ((q*w)+(e*r)+(t*z)+(u*i)-(osz_ablak)-(osz_ablak2))/10000
        t22 = t2/10
        print(osz_ablak)
        self.root.ids.container1.text = "{} nm\u00b2".format(t2)
        self.root.ids.container123.text = "{} l".format(t22)

    def plafonszamitas(self):
        q = int(self.root.ids.Aszel.text)
        e = int(self.root.ids.Bszel.text)
        t3 = (q * e)/10000
        t33 = t3/10
        self.root.ids.container12.text = "{} nm\u00b2".format(t3)
        self.root.ids.container1234.text = "{} l".format(t33)
    print(osz_ablak)
TestApp().run()
