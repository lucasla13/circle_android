# main.py
# Kivy app simples para "Circle of Obsession" (2 jogadores)
# Telas: Menu -> Configuração -> Jogo

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import NumericProperty, DictProperty, StringProperty
from kivy.core.window import Window
from kivy.clock import Clock

# Cores (hex Kivy aceita)
GOLD = "#d6b179"
BG_DARK = "#121212"
CARD_BG = "#1b1b1b"
RED = "#a83c3c"
BLUE = "#3da3ff"

KV = f"""
#:import dp kivy.metrics.dp

<MainMenu@Screen>:
    name: "menu"
    canvas.before:
        Color:
            rgba: (18/255.,18/255.,18/255.,1)
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: "vertical"
        padding: dp(24)
        spacing: dp(24)
        Widget:
        Label:
            text: "CIRCLE OF OBSESSION"
            font_size: "28sp"
            bold: True
            color: ({GOLD})
            size_hint_y: None
            height: self.texture_size[1]
        Widget:
        Button:
            text: "Jogar"
            font_size: "18sp"
            size_hint_y: None
            height: dp(56)
            background_normal: ""
            background_color: (214/255.,177/255.,121/255.,1)
            color: (0,0,0,1)
            on_release: app.sm.current = "config"
        Widget:

<ConfigScreen@Screen>:
    name: "config"
    canvas.before:
        Color:
            rgba: (18/255.,18/255.,18/255.,1)
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: "vertical"
        padding: dp(16)
        spacing: dp(12)

        Label:
            text: "CONFIGURAÇÃO DOS JOGADORES"
            font_size: "20sp"
            color: ({GOLD})
            bold: True
            size_hint_y: None
            height: self.texture_size[1] + dp(8)

        GridLayout:
            cols: 2
            spacing: dp(16)
            size_hint_y: None
            height: self.minimum_height

            # Coluna General 1
            BoxLayout:
                orientation: "vertical"
                padding: dp(8)
                spacing: dp(8)
                canvas.before:
                    Color:
                        rgba: (27/255.,27/255.,27/255.,1)
                    Rectangle:
                        pos: self.pos
                        size: self.size
                Label:
                    text: "GENERAL 1"
                    font_size: "16sp"
                    color: ({GOLD})
                    bold: True
                    size_hint_y: None
                    height: self.texture_size[1] + dp(6)

                Label:
                    text: "Escudo Azul"
                    font_size: "14sp"
                    color: (61/255.,163/255.,1,1)
                    size_hint_y: None
                    height: self.texture_size[1]
                TextInput:
                    id: azul1
                    text: "8"
                    multiline: False
                    halign: "center"
                    write_tab: False
                    size_hint_y: None
                    height: dp(40)
                    background_color: (.15,.15,.15,1)
                    foreground_color: (1,1,1,1)
                    cursor_color: (1,1,1,1)

                Label:
                    text: "Escudo Vermelho"
                    font_size: "14sp"
                    color: (1, 0, 0, 1)
                    size_hint_y: None
                    height: self.texture_size[1]
                TextInput:
                    id: verm1
                    text: "2"
                    multiline: False
                    halign: "center"
                    write_tab: False
                    size_hint_y: None
                    height: dp(40)
                    background_color: (.15,.15,.15,1)
                    foreground_color: (1,1,1,1)
                    cursor_color: (1,1,1,1)

            # Coluna General 2
            BoxLayout:
                orientation: "vertical"
                padding: dp(8)
                spacing: dp(8)
                canvas.before:
                    Color:
                        rgba: (27/255.,27/255.,27/255.,1)
                    Rectangle:
                        pos: self.pos
                        size: self.size
                Label:
                    text: "GENERAL 2"
                    font_size: "16sp"
                    color: ({GOLD})
                    bold: True
                    size_hint_y: None
                    height: self.texture_size[1] + dp(6)

                Label:
                    text: "Escudo Azul"
                    font_size: "14sp"
                    color: (61/255.,163/255.,1,1)
                    size_hint_y: None
                    height: self.texture_size[1]
                TextInput:
                    id: azul2
                    text: "8"
                    multiline: False
                    halign: "center"
                    write_tab: False
                    size_hint_y: None
                    height: dp(40)
                    background_color: (.15,.15,.15,1)
                    foreground_color: (1,1,1,1)
                    cursor_color: (1,1,1,1)

                Label:
                    text: "Escudo Vermelho"
                    font_size: "14sp"
                    color: (1, 0, 0, 1)
                    size_hint_y: None
                    height: self.texture_size[1]
                TextInput:
                    id: verm2
                    text: "2"
                    multiline: False
                    halign: "center"
                    write_tab: False
                    size_hint_y: None
                    height: dp(40)
                    background_color: (.15,.15,.15,1)
                    foreground_color: (1,1,1,1)
                    cursor_color: (1,1,1,1)

        BoxLayout:
            size_hint_y: None
            height: dp(56)
            spacing: dp(12)
            Button:
                text: "Voltar"
                background_normal: ""
                background_color: (.33,.33,.33,1)
                on_release: app.sm.current = "menu"
            Button:
                text: "Iniciar"
                background_normal: ""
                background_color: (214/255.,177/255.,121/255.,1)
                color: (0,0,0,1)
                on_release: app.start_game(int(azul1.text or 0), int(verm1.text or 0), int(azul2.text or 0), int(verm2.text or 0))

<GameScreen@Screen>:
    name: "game"
    canvas.before:
        Color:
            rgba: (18/255.,18/255.,18/255.,1)
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"
        padding: dp(12)
        spacing: dp(12)

        # Card do GENERAL 1 (topo)
        BoxLayout:
            orientation: "vertical"
            padding: dp(12)
            spacing: dp(8)
            size_hint_y: None
            height: self.minimum_height + dp(12)
            canvas.before:
                Color:
                    rgba: (27/255.,27/255.,27/255.,1)
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text: "GENERAL 1"
                font_size: "18sp"
                color: ({GOLD})
                bold: True
                size_hint_y: None
                height: self.texture_size[1] + dp(4)

            BoxLayout:
                spacing: dp(8)
                size_hint_y: None
                height: dp(34)
                Label:
                    id: shield1
                    text: app.shield_text(1)
                    color: (61/255.,163/255.,1,1) if app.player_data["GENERAL 1"]["escudo_atual"]>0 else (1,0,0,1)
                    bold: True
                Button:
                    id: shield_btn1
                    text: "−" if app.player_data["GENERAL 1"]["escudo_atual"]>0 else "Dano"
                    background_normal: ""
                    background_color: (61/255.,163/255.,1,1) if app.player_data["GENERAL 1"]["escudo_atual"]>0 else (168/255.,60/255.,60/255.,1)
                    color: (1,1,1,1)
                    on_release: app.on_shield_btn(1)

            BoxLayout:
                spacing: dp(8)
                size_hint_y: None
                height: dp(60)
                Button:
                    text: "−"
                    background_normal: ""
                    background_color: (168/255.,60/255.,60/255.,1)
                    color: (1,1,1,1)
                    on_release: app.damage_life(1)
                Label:
                    id: life1
                    text: str(app.player_data["GENERAL 1"]["vida"])
                    font_size: "36sp"
                    color: ({GOLD})
                    bold: True
                    size_hint_x: None
                    width: dp(80)
                Button:
                    text: "+"
                    background_normal: ""
                    background_color: (214/255.,177/255.,121/255.,1)
                    color: (0,0,0,1)
                    on_release: app.heal_life(1)

        # Card do GENERAL 2 (baixo)
        BoxLayout:
            orientation: "vertical"
            padding: dp(12)
            spacing: dp(8)
            size_hint_y: None
            height: self.minimum_height + dp(12)
            canvas.before:
                Color:
                    rgba: (27/255.,27/255.,27/255.,1)
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text: "GENERAL 2"
                font_size: "18sp"
                color: ({GOLD})
                bold: True
                size_hint_y: None
                height: self.texture_size[1] + dp(4)

            BoxLayout:
                spacing: dp(8)
                size_hint_y: None
                height: dp(34)
                Label:
                    id: shield2
                    text: app.shield_text(2)
                    color: (61/255.,163/255.,1,1) if app.player_data["GENERAL 2"]["escudo_atual"]>0 else (1,0,0,1)
                    bold: True
                Button:
                    id: shield_btn2
                    text: "−" if app.player_data["GENERAL 2"]["escudo_atual"]>0 else "Dano"
                    background_normal: ""
                    background_color: (61/255.,163/255.,1,1) if app.player_data["GENERAL 2"]["escudo_atual"]>0 else (168/255.,60/255.,60/255.,1)
                    color: (1,1,1,1)
                    on_release: app.on_shield_btn(2)

            BoxLayout:
                spacing: dp(8)
                size_hint_y: None
                height: dp(60)
                Button:
                    text: "−"
                    background_normal: ""
                    background_color: (168/255.,60/255.,60/255.,1)
                    color: (1,1,1,1)
                    on_release: app.damage_life(2)
                Label:
                    id: life2
                    text: str(app.player_data["GENERAL 2"]["vida"])
                    font_size: "36sp"
                    color: ({GOLD})
                    bold: True
                    size_hint_x: None
                    width: dp(80)
                Button:
                    text: "+"
                    background_normal: ""
                    background_color: (214/255.,177/255.,121/255.,1)
                    color: (0,0,0,1)
                    on_release: app.heal_life(2)

        BoxLayout:
            size_hint_y: None
            height: dp(56)
            spacing: dp(12)
            Button:
                text: "↻"
                background_normal: ""
                background_color: (214/255.,177/255.,121/255.,1)
                color: (0,0,0,1)
                on_release: app.restart_game()
            Button:
                text: "Config"
                background_normal: ""
                background_color: (.33,.33,.33,1)
                on_release: app.sm.current = "config"
"""

class CircleApp(App):
    sm: ScreenManager
    # Estrutura dos dados
    player_data = DictProperty({
        "GENERAL 1": {"vida": 4, "escudo_azul": 8, "escudo_vermelho": 2, "escudo_atual": 0},
        "GENERAL 2": {"vida": 4, "escudo_azul": 8, "escudo_vermelho": 2, "escudo_atual": 0},
    })

    def build(self):
        Window.clearcolor = (18/255., 18/255., 18/255., 1)
        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(Builder.load_string(KV))  # carrega telas declaradas no KV
        # Inicia na tela de menu
        self.sm.current = "menu"
        return self.sm

    # ---- Helpers UI ----
    def _ids(self):
        # Pega ids da GameScreen quando estiver ativa
        if "game" in self.sm.screen_names:
            screen = self.sm.get_screen("game")
            return screen.ids
        return {}

    def shield_text(self, idx):
        g = "GENERAL 1" if idx == 1 else "GENERAL 2"
        d = self.player_data[g]
        return str(d["escudo_atual"]) if d["escudo_atual"] > 0 else str(d["escudo_vermelho"])

    def refresh_labels(self):
        ids = self._ids()
        if not ids:  # ainda não na tela de jogo
            return
        # Atualiza textos
        ids.get("life1", None) and setattr(ids["life1"], "text", str(self.player_data["GENERAL 1"]["vida"]))
        ids.get("life2", None) and setattr(ids["life2"], "text", str(self.player_data["GENERAL 2"]["vida"]))
        ids.get("shield1", None) and setattr(ids["shield1"], "text", self.shield_text(1))
        ids.get("shield2", None) and setattr(ids["shield2"], "text", self.shield_text(2))
        # Atualiza cor e texto do botão de escudo
        for i in (1, 2):
            g = "GENERAL 1" if i == 1 else "GENERAL 2"
            has_shield = self.player_data[g]["escudo_atual"] > 0
            btn_id = "shield_btn1" if i == 1 else "shield_btn2"
            btn = ids.get(btn_id)
            if btn:
                btn.text = "−" if has_shield else "Dano"
                btn.background_color = (61/255.,163/255.,1,1) if has_shield else (168/255.,60/255.,60/255.,1)

    # ---- Fluxo ----
    def start_game(self, azul1, verm1, azul2, verm2):
        # Valida
        for v in (azul1, verm1, azul2, verm2):
            if v < 0:
                v = 0
        # Seta dados
        self.player_data["GENERAL 1"]["escudo_azul"] = int(azul1)
        self.player_data["GENERAL 1"]["escudo_vermelho"] = int(verm1)
        self.player_data["GENERAL 1"]["vida"] = 4
        self.player_data["GENERAL 1"]["escudo_atual"] = int(azul1)

        self.player_data["GENERAL 2"]["escudo_azul"] = int(azul2)
        self.player_data["GENERAL 2"]["escudo_vermelho"] = int(verm2)
        self.player_data["GENERAL 2"]["vida"] = 4
        self.player_data["GENERAL 2"]["escudo_atual"] = int(azul2)

        # Vai para tela de jogo
        if "game" not in self.sm.screen_names:
            # Garantia: KV já definiu <GameScreen@Screen>, então existe.
            pass
        self.sm.current = "game"
        # Atualiza UI no próximo frame
        Clock.schedule_once(lambda *_: self.refresh_labels(), 0)

    # ---- Regras ----
    def on_shield_btn(self, idx):
        g = "GENERAL 1" if idx == 1 else "GENERAL 2"
        if self.player_data[g]["escudo_atual"] > 0:
            self.damage_shield(idx)
        else:
            self.damage_life(idx)

    def damage_shield(self, idx):
        g = "GENERAL 1" if idx == 1 else "GENERAL 2"
        if self.player_data[g]["escudo_atual"] > 0:
            self.player_data[g]["escudo_atual"] -= 1
            if self.player_data[g]["escudo_atual"] < 0:
                self.player_data[g]["escudo_atual"] = 0
        self.refresh_labels()

    def damage_life(self, idx):
        g = "GENERAL 1" if idx == 1 else "GENERAL 2"
        # regra: se vida já é 0 e tomar "dano" de novo -> fim (aqui só zera de novo)
        if self.player_data[g]["vida"] == 0:
            # poderia mostrar popup, mas manter simples para Android
            self.refresh_labels()
            return
        self.player_data[g]["vida"] -= 1
        if self.player_data[g]["vida"] < 0:
            self.player_data[g]["vida"] = 0
        # reseta escudo azul ao tomar dano de vida
        self.player_data[g]["escudo_atual"] = max(0, self.player_data[g]["escudo_azul"])
        self.refresh_labels()

    def heal_life(self, idx):
        g = "GENERAL 1" if idx == 1 else "GENERAL 2"
        self.player_data[g]["vida"] += 1
        self.refresh_labels()

    def restart_game(self):
        for g in ("GENERAL 1", "GENERAL 2"):
            self.player_data[g]["vida"] = 4
            self.player_data[g]["escudo_atual"] = self.player_data[g]["escudo_azul"]
        self.refresh_labels()


if __name__ == "__main__":
    CircleApp().run()
