# Tutorial RASA
[Link al tutorial ufficiale di Rasa](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/).

## Pizza bot
In questo tutorial costruiamo un bot che ci aiuti nella nostra pizzeria immaginaria.  
Passo a passo vediamo quali file bisogna modificare per costruire il bot e quali funzionalità possiamo aggiungere.

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
### 0.3 Italiano
Settiamo come lingua del bot italiano modificando il [file config.yml](config.yml): "language: __it__"
## 1 Let's start
### 1.1 domain.yml
Questo file contiene la definizione degli __intent - entities__ del bot.  
Pensiamo a quali intent-entities servono al nostro bot (slide esempio conversazione).  
Modifichiamo il file domain.yml con i nostri intent-entities.  
Il risultato finale deve essere [simile a questo](my_files/fasi/1_domain.yml).   
Possiamo già parlare con il nostro bot?

### 1.2 data/nlu.dm
Questo file contiene tutti gli esempi per il train degli entity.  
Aggiungiamo il nuovo intent ("read_menu") ed esempi di come gli utenti possono chiedere quali pizze siano presenti nel menù.  
Il risultato finale deve essere [simile a questo](my_files/fasi/1_2_nlu.md).  
Partendo da questi facciamo il train del nlu.
```
rasa train nlu
```
Il modello viene salvato, ora vediamo se il bot capisce cosa gli diciamo:
```
rasa shell nlu
```
Il bot capisce gli intent di cui gli abbiamo fornito gli esempi, cosa manca per una conversazione?
### 1.3 data/stories.md
Questo file contiene le "stories" cioè i presunti flussi del discorso fra utente e bot.   
Scriviamo la nostra prima storia immaginando un dialogo semplice dove l'utente saluta e chiede di poter vedere le pizze presenti nel menù, dall'altro lato il bot risponde al saluto e mostra il menù all'utente.  
Il risultato finale deve essere [simile a questo](my_files/fasi/1_3_stories.md).  
Ora possiamo fare il train completo (nlu + core).
```
rasa nlu
```
Finalmente possiamo avere una conversazione con pizza bot!
```
rasa shell
```
## 2 Facciamolo più intelligente
Se ti sei perso qualche passaggio scarica la soluzione fino ad'ora costruita:
```

```
### 2.1 Entities - ordiniamo una pizza
Link alla documentazione ufficiale [entities di Rasa](https://rasa.com/docs/rasa/nlu/training-data-format/#training-data-format).  
Aggiungiamo il nuovo intent "order_pizza" al file domain.yml


