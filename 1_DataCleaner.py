import pandas as pd
import re

# Funzione per pulire il testo 
def clean_text(text):
    # Elimina i @user
    text = re.sub(r'@\w+', '', text)
    # Elimina gli URL
    text = re.sub(r'URL', '', text)
    # Elimino gli #
    text = re.sub(r'#', '', text) 
    # Rimuove i caratteri non validi (compresi i caratteri di controllo)
    text = re.sub(r'[^\x20-\x7E]+', '', text)  # Mantiene solo i caratteri ASCII visibili
    # Elimina i caratteri speciali specificati: +, *, |, \, &, -, =
    text = re.sub(r'[+*|\\&-=]', '', text)
    # Riduce gli spazi multipli a uno solo
    text = re.sub(r'\s+', ' ', text)
    # Rimuove spazi all'inizio e alla fine della stringa
    text = text.strip()
    # Trasforma tutto il testo in minuscolo
    text = text.lower()
    
    return text

# COLONNA B
def clean_dataset(file_path, output_file):
    try:
        # Leggi il file CSV
        df = pd.read_csv(file_path, sep=';') 
        # Applico clean_text 
        df.iloc[:, 1] = df.iloc[:, 1].apply(clean_text)
        # Elimina le righe dove la lunghezza del testo nella seconda colonna è inferiore a 5 caratteri
        df = df[df.iloc[:, 1].str.len() >= 5]
        # Scrivi il dataset pulito su un nuovo file CSV
        df.to_csv(output_file, index=False, sep=';')  
        print(f"Dataset pulito salvato come: {output_file}")
    
    except FileNotFoundError:
        print(f"Errore: il file {file_path} non è stato trovato.")
    except Exception as e:
        print(f"Errore durante la pulizia del dataset: {e}")

# FIle Input
training_file = 'TrainingSet.csv' 
test_file1 = 'TestSet1.csv'  
test_file2 = 'TestSet2.csv'  

# File di output
output_training = 'Training_clean.csv'
output_test1 = 'TestJ_clean.csv'
output_test2 = 'TestT_clean.csv'

# Pulizia dei file
clean_dataset(training_file, output_training)  
clean_dataset(test_file1, output_test1)        
clean_dataset(test_file2, output_test2)        



