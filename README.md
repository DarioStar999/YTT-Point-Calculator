
# 🏆 YTT Point Calculator

Script Python per elaborare i dati statistici estratti da `scrap_coral_stats.js` e calcolare i punteggi dei team o giocatori in base a parametri personalizzabili.

---

## 🚀 Come usarlo

1. **Estrai i dati**  
   Esegui lo script `scrap_coral_stats.js` nella console del browser (Chrome o altro).  
   Copia il JSON che appare nella console.

2. **Salva i dati**  
   Incolla il JSON copiato in un file chiamato `stats.json` nella stessa cartella dello script Python.

3. **Configura lo script Python**  
   - `instaP = True` → mostra solo i punteggi totali per giocatore  
   - `instaP = False` → mostra le statistiche dettagliate (kill, letti rotti, final kill)  
   - `jsonExtract = True` → salva i punteggi in `extracted.json`  
   - `jsonExtract = False` → non salva file extra  
   - Modifica i pesi di punteggio:  
     ```python
     killP = 5
     bedP = 40
     FinalKillP = 25
     ```

4. **Esegui lo script**  
   ```bash
   python main.py
   ```

---

## 📂 Struttura file

```
progetto/
├── main.py              # Script Python per calcolare i punteggi
├── scrap_coral_stats.js # Script per estrarre dati dal browser
├── stats.json           # File JSON con dati estratti
└── extracted.json       # (Opzionale) File JSON con punteggi estratti
```

---

## 📝 Esempi di output

### `instaP = True`
```
Player1, Player2: 450
Player3, Player4: 370
```

### `instaP = False`
```
Team 1: kill = 10, bed = 2, Fkill = 5
Players: Player1, Player2, punti: 450
```

---

## ⚙️ Requisiti

- Python 3.x  
- Nessuna libreria esterna necessaria (usa solo `json`)

---

## 💡 Suggerimenti

- Ideale per calcolare punteggi in tornei o partite competitive.  
- Puoi personalizzare i pesi per adattare il calcolo alle tue esigenze.  
- Assicurati che il formato JSON estratto da `scrap_coral_stats.js` sia corretto e compatibile.

---
