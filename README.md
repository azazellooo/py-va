# Simple GUI app to get some info from wolfram-alpha or wiki (or from both of them).


To run the app install python version 3.8.5 and higher, wolfram alpha account to get API key (wolfram-alpha: https://www.wolframalpha.com)

additional installations:

```bash
sudo apt install libespeak1
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0

```

Clone the repository:
```bash
git clone https://github.com/azazellooo/py-va.git
```

After cloning, go to the cloned folder and create virtual environment:
```bash
python3 -m virtualenv -p python3 venv
```
Create .env file and fill in as shown in the example .

Activate the virtual environment
```bash
source venv/bin/activate

```
Install dependencies:
```bash
pip install -r requirements.txt
```

Go to "src" folder and run the app:


```bash
python3 main.py
```




