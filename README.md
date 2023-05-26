# *GESTIONE FARMACIA*


![N|Solid](https://www.boomerangcard.it/it/uploads/esercente/54/logo.png)


Il progetto si propone di modellare un sistema informatico per la gestione di una farmacia.
L’ipotesi di modellazione alla quale il progetto aderirà sarà quella di una farmacia rurale, il cui personale è composto unicamente dal Direttore Responsabile, addetto alla vendita di farmaci e all’esecuzione di tamponi. 

Il sistema garantirà all’Amministratore l’accesso a funzionalità che consentono la gestione di una serie di operazioni quali:
- Registrazione delle vendite al banco
- Gestione magazzino ( compresa la creazione di ordini verso il fornitore)
- Gestione degli archivi
- Gestione dell'area tamponi (prenotazione ed effettuazione )

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
  <img  src="https://github.com/MarcoSpina01/Farmacia/blob/main/immagini_readme/immagini_readme/login.png">
</p>

**CREDENZIALI:** <br>
*nome utente:* username <br>
*password:* password

La schermata di `Login` consente all'Amministratore di accedere al menù. In caso di problematiche è garantita la possibilità di contattare l'assistenza.
## Gestione Farmacia - FUNZIONALITA'
<p align="center">
  <img  src="https://github.com/MarcoSpina01/Farmacia/blob/main/immagini_readme/immagini_readme/funzionalita.png">
</p>

In seguito al login si accede al `menu delle funzionalità` attraverso il quale è possibile selezionare a quale schermata accedere e quali operazioni effettuare. 
## Gestione Farmacia - TAMPONI
<p align="center">
  <img  src="https://github.com/MarcoSpina01/Farmacia/blob/main/immagini_readme/immagini_readme/calendario.png">
  <img  src="https://github.com/MarcoSpina01/Farmacia/blob/main/immagini_readme/immagini_readme/moduloregistrazione.png">
</p>

La `Gestione Tamponi` consente di:
- **Visualizzare gli appuntamenti:** cliccando sulla data dell'appuntamento sul calendario nella tabella compariranno le relative informazioni. In alternativa è possibile filtrare tramite *Ricerca per* ottenendo o solo gli appuntamenti *conclusi* (ossia con esito) o solo quelli *non conclusi* (ossia senza esito).
- **Aggiungere un nuovo appuntamento:** cliccando *Nuovo Appuntamento* si aprirà un modulo da compilare attraverso il quale, dopo aver premuto *Registrati*, l'appuntamento verrà creato e aggiunto al calendari. Per visualizzare la nuova aggiunta sarà necessario cliccare sulla data del calendario o filtrare per "Non coclusi".
- **Chiudere l'appuntamento**: cliccando *Chiudi appuntamento* il sistema inserirà l'esito e concluderà l'appuntamento. Per visualizzare il nuovo stato sarà necessario ricliccare sulla data del calendario o filtrare per "Conclusi".
- **Eliminare un appuntamento:** selezionando l'appuntamento è possbile procedere alla sua eliminazione.
- **Visualizzare statische:** premendo il bottone *visualizza statistiche esiti* è possibile vedere la percentuale di tamponi positivi e negativi

## Gestione Farmacia - MENU MAGAZZINO
<p align="center">
  <img  src="https://github.com/MarcoSpina01/Farmacia/blob/main/immagini_readme/immagini_readme/magazzino.png">
 </p>

Il `menu Magazzino` consente di:
- **Visualizzare il magazzino:** cliccando *Visualizza magazzino* si accede al magazzino.
- **Effettuare Ordine:** cliccando *Effettua ordine* si accede al menu della scelta fornitori.

### Gestione Farmacia - MENU MAGAZZINO - VISUALIZZA MAGAZZINO
<p align="center">
  <img  src="https://github.com/MarcoSpina01/Farmacia/blob/main/immagini_readme/immagini_readme/visualmagazzino.png">
 </p>


La `Gestione Magazzino` consente di:
- **Ricercare un prodotto:** scrivendo nella barra di ricerca sarà possibile cercare prodotti.

### Gestione Farmacia - MENU MAGAZZINO - SELEZIONE FORNITORI 
<p align="center">
  <img  src="https://github.com/MarcoSpina01/Farmacia/blob/main/immagini_readme/immagini_readme/fornitori.png">
 </p>


Il `menu di selezione fornitori` consente di selezionare il fornitore per l'ordine.

### Gestione Farmacia - MENU MAGAZZINO - EFFETTUA ORDINE
<p align="center">
  <img  src="https://github.com/MarcoSpina01/Farmacia/blob/main/immagini_readme/immagini_readme/pfizer.png">
 </p>


La sezione `Effettua Ordine` consente di:
- **Visualizzare la lista dei prodotti**
- **Ricercare prodotti**
- **Definire la quantità di ciascun prodotto dato il suo codice**
- **Aggiungere un prodotto nel carrello**
- **Acquistare i prodotti** 

### Gestione Farmacia - CASSA 
<p align="center">
  <img  src="https://github.com/MarcoSpina01/Farmacia/blob/main/immagini_readme/immagini_readme/cassa.png">
 </p>


La sezione `Cassa` consente di:
- **Visualizzare la lista dei prodotti**
- **Ricercare prodotti**
- **Definire la quantità di ciascun prodotto dato il suo codice**
- **Aggiungere un prodotto nel carrello**
- **Acquistare i prodotti** 

## Gestione Farmacia - ARCHIVI
<p align="center">
  <img  src="https://github.com/MarcoSpina01/Farmacia/blob/main/immagini_readme/immagini_readme/archivi.png">
 </p>


La `Gestione Archivi` consente di:
- **Visualizzare Archivi:** è possibile visualizzare i clienti, gli esiti dei tamponi, gli ordini effettuati e le vendite effettuate.
- **Ricercare:** scrivendo nella barra di ricerca corrispondente all'archivio di interesse sarà possibile effettuare la ricerca .

# Autori

- Marco Spina - [@MarcoSpina01](https://github.com/MarcoSpina01)
- Michelangelo Marconi - [@MikiMarconi](https://github.com/MikiMarconi)
- Ezekias Wasingya Mastaki - [@Ezekias01](https://github.com/Ezekias01)
