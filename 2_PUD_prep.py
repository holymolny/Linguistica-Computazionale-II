import os
import pandas as pd

# Funzione per creare i file .txt da ciascuna frase del dataset
def create_text_files_from_dataset(input_file):
    try:
        # Leggi il dataset
        df = pd.read_csv(input_file, sep=';')  
        
        # Determina il nome della cartella e il prefisso del file in base al nome del file di input
        if 'Training' in input_file:
            output_folder = 'PUD_training'
            file_prefix = 'training_f'
        elif 'TestT' in input_file:
            output_folder = 'PUD_test'
            file_prefix = 'test_T_f'
        elif 'TestJ' in input_file:
            output_folder = 'PUD_test'
            file_prefix = 'test_J_f'
        else:
            raise ValueError("Il nome del file di input non contiene 'Training', 'TestT' o 'TestJ'.")
        
        # Crea la cartella se non esiste
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"Cartella '{output_folder}' creata.")
        else:
            print(f"Cartella '{output_folder}' già esistente.")
        
        # Per ogni frase nel dataset, crea un file .txt
        for index, row in df.iterrows():
            # Nome del file: file_prefix{index+1}.txt (esempio: training_f1.txt o test_T_f1.txt)
            file_name = f"{file_prefix}{index + 1}.txt"
            file_path = os.path.join(output_folder, file_name)
            
            # Estraggo la frase dalla seconda colonna del dataset
            sentence = row[1]
            
            # Scrivo la frase nel file .txt
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(sentence)
                
            print(f"File creato: {file_name}")
    
    except FileNotFoundError:
        print(f"Errore: il file {input_file} non è stato trovato.")
    except Exception as e:
        print(f"Errore durante la creazione dei file: {e}")

# Percorsi dei file di input
training_file = 'Training_clean.csv'
testT_file = 'TestT_clean.csv'
testJ_file = 'TestJ_clean.csv'

# Chiamata alla funzione per creare i file .txt per ciascun dataset
create_text_files_from_dataset(training_file)  
create_text_files_from_dataset(testT_file)     
create_text_files_from_dataset(testJ_file)    
