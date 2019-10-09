# Tutorial RASA
[Link al tutorial ufficiale di Rasa](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/).

## 0 Set up
### 0.1 Install Rasa
Suggerimento: installa tutto su un [virtual environment](https://www.anaconda.com/distribution/). 
```
pip install rasa
pip install spacy
python -m spacy download it_core_news_sm
python -m spacy link it_core_news_sm it
```
Cos'è [it_core_news_sm](https://spacy.io/models/it) ?
### 0.2 Init
Creiamo un dummy bot per iniziare.
```
rasa init --no-prompt
```
Rasa crea il progetto (con la struttura di default) di un bot minimale ma funzionante.
## 1 Let's start
### 1.1 domain.yml
Questo file contiene la definizione degli __intent - entities__ del bot.  
Pensiamo a quali intent-entities servono al nostro bot.  
Modifichiamo il file domain.yml con i nostri intent-entities. 
Il risultato finale deve essere qualcosa di [simile a questo]('fasi/1_domain.yml').   
Possiamo già parlare con il nostro bot?
```
A
```
```
A
```