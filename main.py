from kivy.app import App
from kivy.lang import Builder
from kivy.properties import DictProperty, BooleanProperty, ObjectProperty, StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button

GOLD = "#d6b179"
BG_DARK = "#121212"
CARD_BG = "#1b1b1b"
RED = "#a83c3c"
BLUE = "#3da3ff"

KV = r"""
#:set GOLD "#d6b179"
#:set BG_DARK "#121212"
#:set CARD_BG "#1b1b1b"
#:set RED "#a83c3c"
#:set BLUE "#3da3ff"

<Title@Label>:
    bold: True
    color: (214/255, 177/255, 121/255, 1)
    font_size: '22sp'

<Sub@Label>:
    color: (1,1,1,1)
    font_size: '16sp'

<Btn@Button>:
    background_normal: ''
    background_color: (214/255, 177/255, 121/255, 1)
    color: (0,0,0,1)
    bold: True
    padding: 12, 12
    size_hint_y: None
    height: '44dp'
    canvas.before:
        Color:
            rgba: self.background_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10,]

<SmallBtn@Button>:
    background_normal: ''
    background_color: (0.24,0.64,1,1)
    color: (1,1,1,1)
    bold: True
    size_hint: None, None
    height: '36dp'
    width: '72dp'
    canvas.before:
        Color:
            rgba: self.background_color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [8,]

<PlayerCard>:
    orientation: 'vertical'
    spacing: '10dp'
    padding: '12dp'
    size_hint_y: None
    height: self.minimum_height + dp(8)
    canvas.before:
        Color:
            rgba: (27/255,27/255,27/255,1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [12,]
    BoxLayout:
        size_hint_y: None
        height: '32dp'
        Label:
            text: root.general_name
            color: (214/255, 177/255, 121/255, 1)
            bold: True
            font_size: '18sp'
    BoxLayout:
        size_hint_y: None
        height: '36dp'
        spacing: '8dp'
        Label:
            text: "🛡"
            color: (61/255, 163/255, 1, 1)
            size_hint_x: None
            width: '24dp'
            font_size: '18sp'
        Label:
            id: lbl_shield
            text: root.shield_text
            color: root.shield_color
            font_size: '16sp'
            bold: True
        SmallBtn:
            id: btn_shield
            text: root.shield_btn_text
            background_color: root.shield_btn_bg
            on_release: root.on_shield_btn()
    BoxLayout:
        size_hint_y: None
        height: '64dp'
        spacing: '12dp'
        SmallBtn:
            id: btn_minus
            text: "−"
            background_color: (168/255, 60/255, 60/255, 1)
            width: '56dp'
            on_release: root.damage_life()
        Label:
            id: lbl_life
            text: str(root.vida)
            font_size: '36sp'
            color: (214/255, 177/255, 121/255, 1)
            bold: True
        SmallBtn:
            id: btn_plus
            text: "+"
            background_color: (214/255, 177/255, 121/255, 1)
            color: (0,0,0,1)
            width: '56dp'
            on_release: root.heal_life()

<MainScreen@BoxLayout>:
    app_ref: app
    orientation: 'vertical'
    spacing: '12dp'
    padding: '16dp'
    canvas.before:
        Color:
            rgba: (18/255,18/255,18/255,1)
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        size_hint_y: None
        height: '72dp'
        Title:
            text: "CIRCLE OF OBSESSION"
    Widget:
    Btn:
        text: "Jogar"
        on_release: app.show_config()
    Widget:

<ConfigScreen@BoxLayout>:
    app_ref: app
    orientation: 'vertical'
    spacing: '10dp'
    padding: '16dp'
    canvas.before:
        Color:
            rgba: (18/255,18/255,18/255,1)
        Rectangle:
            pos: self.pos
            size: self.size
    Title:
        text: "CONFIGURAÇÃO DOS JOGADORES"
        size_hint_y: None
        height: '40dp'
    BoxLayout:
        spacing: '20dp'
        size_hint_y: None
        height: '160dp'
        BoxLayout:
            orientation: 'vertical'
            spacing: '6dp'
            Sub:
                text: "GENERAL 1"
            Sub:
                text: "Escudo Azul"
                color: (61/255,163/255,1,1)
            TextInput:
                id: azul1
                text: str(app.player_data["GENERAL 1"]["escudo_azul"])
                multiline: False
                input_filter: 'int'
                size_hint_y: None
                height: '40dp'
                background_color: (0.18,0.18,0.18,1)
                foreground_color: (1,1,1,1)
            Sub:
                text: "Escudo Vermelho"
                color: (1,0.2,0.2,1)
            TextInput:
                id: verm1
                text: str(app.player_data["GENERAL 1"]["escudo_vermelho"])
                multiline: False
                input_filter: 'int'
                size_hint_y: None
                height: '40dp'
                background_color: (0.18,0.18,0.18,1)
                foreground_color: (1,1,1,1)
        BoxLayout:
            orientation: 'vertical'
            spacing: '6dp'
            Sub:
                text: "GENERAL 2"
            Sub:
                text: "Escudo Azul"
                color: (61/255,163/255,1,1)
            TextInput:
                id: azul2
                text: str(app.player_data["GENERAL 2"]["escudo_azul"])
                multiline: False
                input_filter: 'int'
                size_hint_y: None
                height: '40dp'
                background_color: (0.18,0.18,0.18,1)
                foreground_color: (1,1,1,1)
            Sub:
                text: "Escudo Vermelho"
                color: (1,0.2,0.2,1)
            TextInput:
                id: verm2
                text: str(app.player_data["GENERAL 2"]["escudo_vermelho"])
                multiline: False
                input_filter: 'int'
                size_hint_y: None
                height: '40dp'
                background_color: (0.18,0.18,0.18,1)
                foreground_color: (1,1,1,1)
    BoxLayout:
        size_hint_y: None
        height: '48dp'
        spacing: '10dp'
        Btn:
            text: "Iniciar"
            on_release: app.start_game(
                int(azul1.text or 0), int(verm1.text or 0),
                int(azul2.text or 0), int(verm2.text or 0)
            )
        Button:
            text: "Voltar"
            background_normal: ''
            background_color: (0.33,0.33,0.33,1)
            color: (1,1,1,1)
            on_release: app.show_main()

<GameScreen@BoxLayout>:
    app_ref: app
    orientation: 'vertical'
    spacing: '10dp'
    padding: '16dp'
    canvas.before:
        Color:
            rgba: (18/255,18/255,18/255,1)
        Rectangle:
            pos: self.pos
            size: self.size
    Scatter:
        size_hint_y: None
        height: top_card.height + dp(12)
        do_translation: False
        do_rotation: False
        do_scale: False
        rotation: 180
        PlayerCard:
            id: top_card
            general_name: "GENERAL 1"
            app_ref: app
            rotated: True
    PlayerCard:
        id: bottom_card
        general_name: "GENERAL 2"
        app_ref: app
        rotated: False
    BoxLayout:
        size_hint_y: None
        height: '48dp'
        spacing: '10dp'
        Btn:
            text: "↻"
            on_release: app.restart_game()
        Button:
            text: "Voltar"
            background_normal: ''
            background_color: (0.33,0.33,0.33,1)
            color: (1,1,1,1)
            on_release: app.show_config()
"""

class PlayerCard(BoxLayout):
    app_ref = ObjectProperty(None)
    general_name = StringProperty("GENERAL")
    rotated = BooleanProperty(False)

    vida = NumericProperty(4)
    escudo_azul = NumericProperty(8)
    escudo_vermelho = NumericProperty(2)
    escudo_atual = NumericProperty(0)

    shield_text = StringProperty("0")
    shield_color = ObjectProperty((61/255,163/255,1,1))
    shield_btn_text = StringProperty("−")
    shield_btn_bg = ObjectProperty((61/255,163/255,1,1))

    def on_kv_post(self, base_widget):
        self.sync_from_app()

    def sync_from_app(self):
        d = self.app_ref.player_data[self.general_name]
        self.vida = d["vida"]
        self.escudo_azul = d["escudo_azul"]
        self.escudo_vermelho = d["escudo_vermelho"]
        self.escudo_atual = d["escudo_atual"]
        self.refresh()

    def refresh(self):
        if self.escudo_atual > 0:
            self.shield_text = str(self.escudo_atual)
            self.shield_color = (61/255,163/255,1,1)
            self.shield_btn_text = "−"
            self.shield_btn_bg = (61/255,163/255,1,1)
        else:
            self.shield_text = str(self.escudo_vermelho)
            self.shield_color = (1,0.2,0.2,1)
            self.shield_btn_text = "Dano"
            self.shield_btn_bg = (168/255, 60/255, 60/255, 1)

    def _announce_winner(self, loser):
        if self.app_ref.game_over:
            return
        self.app_ref.game_over = True
        winner = "GENERAL 1" if loser == "GENERAL 2" else "GENERAL 2"
        content = BoxLayout(orientation='vertical', padding=12, spacing=10)
        content.add_widget(Label(text=f"[b]{winner} venceu a partida![/b]", markup=True))
        btn = Button(text="OK", size_hint=(1,None), height="40dp")
        popup = Popup(title="Fim de jogo", content=content, size_hint=(.7,.35))
        btn.bind(on_release=lambda *_: popup.dismiss())
        content.add_widget(btn)
        popup.open()

    def on_shield_btn(self):
        if self.escudo_atual > 0:
            self.escudo_atual = max(0, self.escudo_atual - 1)
            self._persist()
            self.refresh()
        else:
            self.damage_life()

    def damage_life(self):
        if self.app_ref.game_over:
            return
        if self.vida == 0:
            self._announce_winner(self.general_name)
            return
        self.vida = max(0, self.vida - 1)
        self.escudo_atual = max(0, self.escudo_azul)
        self._persist()
        self.refresh()

    def heal_life(self):
        if self.app_ref.game_over:
            return
        self.vida += 1
        self._persist()
        self.refresh()

    def _persist(self):
        d = self.app_ref.player_data[self.general_name]
        d["vida"] = int(self.vida)
        d["escudo_azul"] = int(self.escudo_azul)
        d["escudo_vermelho"] = int(self.escudo_vermelho)
        d["escudo_atual"] = int(self.escudo_atual)

class CircleOfObsessionApp(App):
    player_data = DictProperty({
        "GENERAL 1": {"vida": 4, "escudo_azul": 8, "escudo_vermelho": 2, "escudo_atual": 0},
        "GENERAL 2": {"vida": 4, "escudo_azul": 8, "escudo_vermelho": 2, "escudo_atual": 0},
    })
    game_over = BooleanProperty(False)

    def build(self):
        return Builder.load_string(KV).children[0]

    def on_start(self):
        self.show_main()

    def _set_root(self, widget):
        from kivy.core.window import Window
        Window.clearcolor = (18/255,18/255,18/255,1)
        self.root.clear_widgets()
        self.root.add_widget(widget)

    def show_main(self):
        self._set_root(Builder.template('MainScreen', app_ref=self))

    def show_config(self):
        self._set_root(Builder.template('ConfigScreen', app_ref=self))

    def show_game(self):
        self._set_root(Builder.template('GameScreen', app_ref=self))
        scr = self.root.children[0] if self.root.children else self.root
        try:
            scr.ids.top_card.sync_from_app()
            scr.ids.bottom_card.sync_from_app()
        except Exception:
            pass

    def start_game(self, azul1, verm1, azul2, verm2):
        for name, (azul, verm) in {
            "GENERAL 1": (azul1, verm1),
            "GENERAL 2": (azul2, verm2),
        }.items():
            if azul < 0 or verm < 0:
                return
            self.player_data[name]["escudo_azul"] = int(azul)
            self.player_data[name]["escudo_vermelho"] = int(verm)
            self.player_data[name]["escudo_atual"] = int(azul)
            self.player_data[name]["vida"] = 4
        self.game_over = False
        self.show_game()

    def restart_game(self):
        self.game_over = False
        for g in self.player_data:
            self.player_data[g]["vida"] = 4
            self.player_data[g]["escudo_atual"] = self.player_data[g]["escudo_azul"]
        self.show_game()

if __name__ == "__main__":
    CircleOfObsessionApp().run()
