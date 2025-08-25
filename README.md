# Circle of Obsession (Android/Kivy)

## Como gerar o APK via GitHub Actions
1. Crie um repositório no GitHub e suba estes arquivos.
2. Vá em **Actions** > **android-apk** > **Run workflow**.
3. Ao finalizar, baixe o artefato **apk**: contém o `*-debug.apk` instalável.

## Build local (Linux/WSL2)
```bash
sudo apt update && sudo apt install -y python3-venv python3-pip git openjdk-17-jdk zip unzip libffi-dev libssl-dev
pip install --user buildozer
python3 -m venv .venv && source .venv/bin/activate
pip install kivy
buildozer init  # já temos buildozer.spec, então ignora mudanças
buildozer -v android debug
```
APK sai em `bin/`.
