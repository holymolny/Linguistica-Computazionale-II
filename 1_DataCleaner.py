import pandas as pd
import re

# Funzione per pulire il testo in base ai criteri specificati
def clean_text(text):
    # Elimina i @user
    text = re.sub(r'@\w+', '', text)
    # Elimina gli URL
    text = re.sub(r'URL', '', text)
    # Elimino gli #
    text = re.sub(r'#', '', text)
    
    # Elimina le emoticon (usando un pattern per le emoji Unicode)
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # Emoticons
        u"\U0001F300-\U0001F5FF"  # Simboli & Pittogrammi
        u"\U0001F680-\U0001F6FF"  # Trasporti & Simboli mappa
        u"\U0001F700-\U0001F77F"  # Simboli aggiuntivi
        u"\U0001F780-\U0001F7FF"  # Simboli geometrici aggiuntivi
        u"\U0001F800-\U0001F8FF"  # Simboli supplementari
        u"\U0001F900-\U0001F9FF"  # Emoticon facce
        u"\U0001FA00-\U0001FA6F"  # Simboli ulteriori
        "]+", flags=re.UNICODE
    )
    text = emoji_pattern.sub(r'', text)
    
    # Rimuove i caratteri non validi (compresi i caratteri di controllo)
    text = re.sub(r'[^\x20-\x7E]+', '', text)  # Mantiene solo i caratteri ASCII visibili
    # Elimina i caratteri speciali specificati: +, *, |, \, &, -
    text = re.sub(r'[+*|\\&-]', '', text)
    # Riduce gli spazi multipli a uno solo
    text = re.sub(r'\s+', ' ', text)
    # Rimuove spazi all'inizio e alla fine della stringa
    text = text.strip()
    # Trasforma tutto il testo in minuscolo
    text = text.lower()
    
    return text

# Funzione per aprire il file CSV, pulire i dati nella seconda colonna (colonna B) e salvare il dataset pulito
def clean_dataset(file_path, output_file):
    try:
        # Leggi il file CSV
        df = pd.read_csv(file_path, sep=';')  # Usa sep=',' se il delimitatore è la virgola
        
        # Applica la funzione di pulizia sulla seconda colonna (indice 1)
        df.iloc[:, 1] = df.iloc[:, 1].apply(clean_text)
        
        # Elimina le righe dove la lunghezza del testo nella seconda colonna è inferiore a 5 caratteri
        df = df[df.iloc[:, 1].str.len() >= 5]
        
        # Scrivi il dataset pulito su un nuovo file CSV
        df.to_csv(output_file, index=False, sep=';')  # Mantiene il separatore originale
        
        print(f"Dataset pulito salvato come: {output_file}")
    
    except FileNotFoundError:
        print(f"Errore: il file {file_path} non è stato trovato.")
    except Exception as e:
        print(f"Errore durante la pulizia del dataset: {e}")


# Esempio di utilizzo
file_path = 'TrainingSet.csv'  # Sostituisci con il percorso del file di input
output_file = 'dataset_pulito.csv'  # Nome del file di output
clean_dataset(file_path, output_file)


