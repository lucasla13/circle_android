# main.py
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import get_color_from_hex as HEX

GOLD = HEX("#d6b179")
BG_DARK = HEX("#121212")
CARD_BG = HEX("#1b1b1b")
RED = HEX("#a83c3c")
BLUE = HEX("#3da3ff")
WHITE = HEX("#ffffff")
BLACK = HEX("#000000")

KV = f"""
#:import dp kivy.metrics.dp

<PrimaryButton@Button>:
    bold: True
    background_normal: ''
    background_color: {GOLD}
    color: 0,0,0,1
    size_hint_y: None
    height: dp(48)
    canvas.before:
        Color:
            rgba: {GOLD}
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [12,]

<SecondaryButton@Button>:
    background_normal: ''
    background_color: .33,.33,.33,1
    color: 1,1,1,1
    size_hint_y: None
    height: dp(42)
    canvas.before:
        Color:
            rgba: .33,.33,.33,1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10,]

<PlayerPanel@BoxLayout>:
    orientation: "vertical"
    padding: dp(12)
    spacing: dp(8)
    size_hint_y: None
    height: self.minimum_height
    canvas.before:
        Color:
            rgba: {CARD_BG}
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [12,]
    # props que o app seta
    title: ""
    vida: 0
    escudo_atual: 0
    escudo_azul: 0
    escudo_vermelho: 0
    name: ""
    # header
    BoxLayout:
        size_hint_y: None
        height: dp(36)
        Label:
            text: root.name
            bold: True
            color: {GOLD}
            font_size: "18sp"
            halign: "center"
            valign: "middle"
    # linha do escudo
    BoxLayout:
        size_hint_y: None
        height: dp(36)
        spacing: dp(8)
        Label:
            text: "🛡"
            color: {BLUE}
            size_hint_x: None
            width: dp(28)
            font_size: "16sp"
        Label:
            id: lbl_shield
            text: str(root.escudo_atual) if root.escudo_atual>0 else str(root.escudo_vermelho)
            color: {BLUE} if root.escudo_atual>0 else (1,0,0,1)
            bold: True
            font_size: "16sp"
            size_hint_x: None
            width: dp(40)
        SecondaryButton:
            id: btn_dano
            text: "−" if root.escudo_atual>0 else "Dano"
            background_color: {BLUE} if root.escudo_atual>0 else {RED}
            on_release: app.shield_or_damage(root.name)
    # vida
    BoxLayout:
        size_hint_y: None
        height: dp(64)
        spacing: dp(10)
        SecondaryButton:
            text: "−"
            background_color: {RED}
            on_release: app.damage_life(root.name)
            size_hint_x: None
            width: dp(64)
        Label:
            id: lbl_vida
            text: str(root.vida)
            color: {GOLD}
            bold: True
            font_size: "40sp"
        SecondaryButton:
            text: "+"
            background_color: {GOLD}
            color: 0,0,0,1
            on_release: app.heal_life(root.name)
            size_hint_x: None
            width: dp(64)

<MainScreen>:
    name: "main"
    BoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(20)
        canvas.before:
            Color:
                rgba: {BG_DARK}
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "CIRCLE OF OBSESSION"
            color: {GOLD}
            bold: True
            font_size: "24sp"
            size_hint_y: None
            height: dp(60)
        PrimaryButton:
            text: "Jogar"
            on_release: app.root.current="config"

<ConfigScreen>:
    name: "config"
    BoxLayout:
        orientation: "vertical"
        padding: dp(16)
        spacing: dp(12)
        canvas.before:
            Color:
                rgba: {BG_DARK}
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "CONFIGURAÇÃO DOS JOGADORES"
            color: {GOLD}
            bold: True
            font_size: "20sp"
            size_hint_y: None
            height: dp(50)
        BoxLayout:
            spacing: dp(24)
            size_hint_y: None
            height: dp(160)
            # Coluna 1
            BoxLayout:
                orientation: "vertical"
                spacing: dp(6)
                Label:
                    text: "GENERAL 1"
                    color: {GOLD}
                    bold: True
                Label:
                    text: "Escudo Azul"
                    color: {BLUE}
                TextInput:
                    id: azul1
                    text: "8"
                    input_filter: "int"
                    halign: "center"
                    size_hint_y: None
                    height: dp(40)
                Label:
                    text: "Escudo Vermelho"
                    color: 1,0,0,1
                TextInput:
                    id: verm1
                    text: "2"
                    input_filter: "int"
                    halign: "center"
                    size_hint_y: None
                    height: dp(40)
            # Coluna 2
            BoxLayout:
                orientation: "vertical"
                spacing: dp(6)
                Label:
                    text: "GENERAL 2"
                    color: {GOLD}
                    bold: True
                Label:
                    text: "Escudo Azul"
                    color: {BLUE}
                TextInput:
                    id: azul2
                    text: "8"
                    input_filter: "int"
                    halign: "center"
                    size_hint_y: None
                    height: dp(40)
                Label:
                    text: "Escudo Vermelho"
                    color: 1,0,0,1
                TextInput:
                    id: verm2
                    text: "2"
                    input_filter: "int"
                    halign: "center"
                    size_hint_y: None
                    height: dp(40)
        PrimaryButton:
            text: "Iniciar"
            on_release: app.start_game(int(azul1.text or 0), int(verm1.text or 0), int(azul2.text or 0), int(verm2.text or 0))
        SecondaryButton:
            text: "Voltar"
            on_release: app.root.current="main"

<GameScreen>:
    name: "game"
    BoxLayout:
        orientation: "vertical"
        padding: dp(12)
        spacing: dp(10)
        canvas.before:
            Color:
                rgba: {BG_DARK}
            Rectangle:
                pos: self.pos
                size: self.size
        PlayerPanel:
            name: "GENERAL 1"
            vida: app.player_data["GENERAL 1"]["vida"]
            escudo_atual: app.player_data["GENERAL 1"]["escudo_atual"]
            escudo_azul: app.player_data["GENERAL 1"]["escudo_azul"]
            escudo_vermelho: app.player_data["GENERAL 1"]["escudo_vermelho"]
        PlayerPanel:
            name: "GENERAL 2"
            vida: app.player_data["GENERAL 2"]["vida"]
            escudo_atual: app.player_data["GENERAL 2"]["escudo_atual"]
            escudo_azul: app.player_data["GENERAL 2"]["escudo_azul"]
            escudo_vermelho: app.player_data["GENERAL 2"]["escudo_vermelho"]
        BoxLayout:
            size_hint_y: None
            height: dp(52)
            spacing: dp(10)
            PrimaryButton:
                text: "↻"
                on_release: app.restart_game()
            SecondaryButton:
                text: "Config"
                on_release: app.root.current="config"
"""

class MainScreen(Screen):
    pass

class ConfigScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class Root(ScreenManager):
    pass

class CircleApp(App):
    player_data = {
        "GENERAL 1": {"vida": 4, "escudo_azul": 8, "escudo_vermelho": 2, "escudo_atual": 8},
        "GENERAL 2": {"vida": 4, "escudo_azul": 8, "escudo_vermelho": 2, "escudo_atual": 8},
    }

    def build(self):
        self.title = "Circle of Obsession - Life Counter"
        return Builder.load_string(KV)

    # ações
    def start_game(self, azul1, verm1, azul2, verm2):
        if azul1 < 0 or verm1 < 0 or azul2 < 0 or verm2 < 0:
            return
        self.player_data["GENERAL 1"].update(vida=4, escudo_azul=azul1, escudo_vermelho=verm1, escudo_atual=azul1)
        self.player_data["GENERAL 2"].update(vida=4, escudo_azul=azul2, escudo_vermelho=verm2, escudo_atual=azul2)
        self.root.current = "game"
        self._refresh_game_screen()

    def _refresh_game_screen(self):
        gs = self.root.get_screen("game")
        # Reconsulta propriedades exibidas
        for child in gs.children:
            pass  # os bindings do KV pegam direto de app.player_data
        # Força relayout
        gs.canvas.ask_update()

    def shield_or_damage(self, name):
        d = self.player_data[name]
        if d["escudo_atual"] > 0:
            d["escudo_atual"] -= 1
        else:
            self.damage_life(name)

        self._refresh_game_screen()

    def damage_life(self, name):
        d = self.player_data[name]
        if d["vida"] == 0:
            # terminou – não fecha app; só ignore
            return
        d["vida"] -= 1
        d["escudo_atual"] = max(0, d["escudo_azul"])
        self._refresh_game_screen()

    def heal_life(self, name):
        d = self.player_data[name]
        d["vida"] += 1
        self._refresh_game_screen()

    def restart_game(self):
        for g in self.player_data:
            self.player_data[g]["vida"] = 4
            self.player_data[g]["escudo_atual"] = self.player_data[g]["escudo_azul"]
        self._refresh_game_screen()

if __name__ == "__main__":
    CircleApp().run()
