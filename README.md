# *PHARMACY*


![N|Solid](https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/copertina_progettoingsoft.png)


Il progetto si propone di modellare un sistema informatico per la gestione di una farmacia.
L’ipotesi di modellazione alla quale il progetto aderirà sarà quella di una farmacia rurale, il cui personale è composto unicamente dal Direttore Responsabile, addetto alla vendita di farmaci e all’esecuzione di tamponi. 

Il sistema garantirà all’Amministratore l’accesso a funzionalità che consentono la gestione di una serie di operazioni quali:
- Gestione dell'area tamponi (prenotazione ed effettuazione )
- Gestione magazzino ( compresa la creazione di ordini verso il fornitore)
- Gestione vendite al banco
- Gestione degli archivi


# Installation

Il software è stato sviluppato in Python con l'ausilio di PyCharm. 

![Build Status](https://i.stack.imgur.com/wJqaA.png)


Per installare installare il progetto su PyCharm:
- Dal menu principale, scegli Git | Clone. Se il menu Git non è disponibile, scegli VCS | Ottieni da Controllo versione.
- Nella finestra di dialogo Ottieni da controllo versione, scegli GitHub a sinistra.
- Accedi a GitHub effettuando una delle seguenti operazioni:
- Se disponi di un token, fai clic su Usa token, quindi incolla il token nel campo Token e fai clic su Accedi.
- Altrimenti, fai clic su Accedi tramite GitHub.
- Inserisci le tue credenziali GitHub nella finestra del browser che si apre. Se hai abilitato l'autenticazione a due fattori, ti verrà chiesto di inserire un codice che ti verrà inviato tramite SMS o tramite l'applicazione mobile.
- Seleziona la repository da GitHub associati 
- Nel campo Directory, inserisci il percorso della cartella in cui verrà creato il tuo repository Git locale.
- Fare clic su Clona.


# Features
## Gestione Farmacia -  LOGIN
<p align="center">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/login.png">
</p>

**CREDENZIALI:** <br>
*nome utente:* FarmaciaAncona <br>
*password:* tachitachi

La schermata di `Login` consente all'Amministratore di accedere al menù. In caso di problematiche è garantita la possibilità di contattare l'assistenza.
## Gestione Farmacia - FUNZIONALITA'
<p align="center">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/mainmenu.png">
</p>

In seguito al login si accede al `menu delle funzionalità` attraverso il quale è possibile selezionare a quale schermata accedere e quali operazioni effettuare. 
## Gestione Farmacia - TAMPONI
<p align="center">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/calendar.png">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/appointmentform.png">
</p>

La `Gestione Tamponi` consente di:
- **Visualizzare gli appuntamenti:** cliccando sulla data dell'appuntamento sul calendario nella tabella compariranno le relative informazioni. In alternativa è possibile filtrare tramite *Ricerca per* ottenendo o solo gli appuntamenti *conclusi* (ossia con esito) o solo quelli *non conclusi* (ossia senza esito).
- **Aggiungere un nuovo appuntamento:** cliccando *Nuovo Appuntamento* si aprirà un modulo da compilare attraverso il quale, dopo aver premuto *Prenota*, l'appuntamento verrà creato e aggiunto al calendari. Per visualizzare la nuova aggiunta sarà necessario cliccare sulla data del calendario o filtrare per "Non conclusi".
- **Chiudere l'appuntamento**: cliccando *Chiudi appuntamento* il sistema inserirà l'esito e concluderà l'appuntamento. Per visualizzare il nuovo stato sarà necessario ricliccare sulla data del calendario o filtrare per "Conclusi".
- **Eliminare un appuntamento:** selezionando l'appuntamento è possbile procedere alla sua eliminazione.


## Gestione Farmacia - MENU MAGAZZINO
<p align="center">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/warehouse.png">
 </p>


La `Gestione Magazzino` consente di:
- **Ricercare un prodotto:** scrivendo nella barra di ricerca sarà possibile cercare prodotti.
- **Effettuare Ordine:** cliccando *Nuovo ordine* si accede al menu della scelta fornitori.
- **Visualizzare Scadezario:** cliccando *Scadenzario* si visualizzano i prodotti in scadenza nel breve periodo.



### Gestione Farmacia - MENU MAGAZZINO - EFFETTUA ORDINE
<p align="center">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/suppliermenu.png">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/supplierscreen.png">
</p>

Il `menu consente di selezionare il fornitore per l'ordine e poi accedere alla schermata di acquisto.

Nella schermata di acquisto sarà possibile: 
- **Visualizzare la lista dei prodotti acquistabili**
- **Ricercare prodotti**
- **Definire la quantità di ciascun prodotto**
- **Aggiungere un prodotto nel carrello dopo averlo selezionato**
- **Acquistare i prodotti** 

### Gestione Farmacia - MENU MAGAZZINO - SCADENZARIO
<p align="center">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/expirationdates.png">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/expirationdates_chart.png">
</p>

Il `menu consente di visualizzare i prodotti in scadenza e ottenere statistiche.

Nella schermata sarà possibile: 
- **Visualizzare la lista dei prodotti filtratata secondo la scadenza**
- **Ricercare prodotti**
- **Visualizzare statistiche:** premendo l'apposito bottone sarà possibile visualizzare il grafico a torta delle scadenze.


## Gestione Farmacia - CASSA 
<p align="center">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/cashregister.png">
 </p>

La sezione `Cassa` consente di:
- **Visualizzare la lista dei prodotti vendibili**
- **Ricercare prodotti**
- **Definire la quantità di ciascun prodotto**
- **Aggiungere un prodotto nel carrello dopo averlo selezionato***
- **Chiudere la vendita** 

## Gestione Farmacia - ARCHIVI
<p align="center">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/archivemenu.png">
 </p>


La `Gestione Archivi` consente di:
- **Visualizzare Archivi:** è possibile visualizzare i `clienti`, gli `esiti dei tamponi`, gli `ordini effettuati` e le `vendite effettuate`.

### Gestione Farmacia - ARCHIVI - VENDITE
<p align="center">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/salesarchive.png">
</p>


L'`Archivio Vendite` consente di:
- **Visualizzare vendite effettuate**
- **Ricercare:** scrivendo nella barra di ricerca sarà possibile effettuare la ricerca di specifiche vendite.

### Gestione Farmacia - ARCHIVI - CLIENTI
<p align="center">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/clientsarchive.png">
 </p>


L'`Archivio Clienti` consente di:
- **Visualizzare i clienti registrati**
- **Ricercare:** scrivendo nella barra di ricerca sarà possibile effettuare la ricerca di specifici clienti.

### Gestione Farmacia - ARCHIVI - ESITI
<p align="center">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/resultsarchive.png">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/resultschart.png">

</p>


L'`Archivio Esiti` consente di:
- **Visualizzare esiti**
- **Ricercare:** scrivendo nella barra di ricerca sarà possibile effettuare la ricerca di specifici esiti.
- **Visualizzare statistiche:** premendo l'apposito bottone sarà possibile visualizzare il grafico a torta degli esiti.


### Gestione Farmacia - ARCHIVI - ORDINI
<p align="center">
  <img  src="https://github.com/Ezekias01/DrugStore/blob/master/immagini_readme/ordersarchive.png">
 </p>


L'`Archivio Vendite` consente di:
- **Visualizzare ordini effettuati**
- **Ricercare:** scrivendo nella barra di ricerca sarà possibile effettuare la ricerca di specifici ordini .




# Autori

- Ezekias Wasingya Mastaki - [@Ezekias01](https://github.com/Ezekias01)
- Marco Spina - [@MarcoSpina01](https://github.com/MarcoSpina01)
- Michelangelo Marconi - [@MikiMarconi](https://github.com/MikiMarconi)
