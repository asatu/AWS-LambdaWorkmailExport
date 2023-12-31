# AWS-LambdaWorkmailExport - Riccardo Scudieri
Esportare Caselle di Posta da Amazon WorkMail a Amazon S3 tramite Lambda


## Passo 1: Creare una policy IAM

1. Accedi alla Console AWS e vai alla sezione IAM (Identity and Access Management).
2. Nella barra laterale sinistra, seleziona "Policies" e poi clicca su "Create policy".
3. Specifica i permessi tramite JSON editor.
4. Aggiungi la policy incollando il contenuto del file "AWSLambdaBasicExecutionRole.json" e dandogli un nome.
5. Dopo aver creato la policy, prendi nota del nome per il passo successivo.
   
## Passo 2: Creare un ruolo IAM

1. Accedi alla Console AWS e vai alla sezione IAM (Identity and Access Management).
2. Nella barra laterale sinistra, seleziona "Roles" e poi clicca su "Create role".
3. Scegli il servizio Lambda come entità che utilizzerà questo ruolo.
4. Aggiungi la policy precedentemente creata al ruolo per fornire le autorizzazioni necessarie.
5. Dopo aver creato il ruolo, modifica la Trust Relationships incollando il contenuto del file "TrustRelationships.json"
6. Prendi nota dell'ARN del ruolo.

## Passo 2: Creare una chiave KMS per il Bucket S3

1. Vai alla sezione KMS (Key Management Service) nella Console AWS.
2. Clicca su "Create key".
3. Seleziona "Symmetric" come tipo di chiave e scegli un alias e una descrizione (opzionale).
4. Scegli il ruolo IAM creato nel Passo 2 come "Key Users" e clicca su "Next".
5. Configura le autorizzazioni come necessario e clicca su "Next".
6. Rivedi le impostazioni e clicca su "Finish" per creare la chiave.

## Passo 3: Creare un bucket S3

1. Vai alla sezione S3 della Console AWS.
2. Clicca su "Create bucket" e segui le istruzioni per creare un nuovo bucket S3.
3. Assicurati di prendere nota del nome e dell'arn del bucket creato.

## Passo 4: Creare una funzione Lambda

1. Vai alla sezione Lambda della Console AWS.
2. Clicca su "Create function" e seleziona "Author from scratch".
3. Assegna un nome alla funzione e seleziona il runtime Python 3.x.
4. Seleziona il ruolo IAM creato nel Passo 1 dalla lista "Existing role".
5. Clicca su "Create function".
6. Assicurati che il ruolo sia attaccato correttamente.
7. Prolunga il tempo di esecuzione della funzione al massimo (15min)

## Passo 5: Scrivere e caricare il codice Lambda

1. Nella pagina della funzione Lambda, vai alla sezione "Function code".
2. Incolla il codice Python incollando il contenuto del file "lambda_function.py".
3. Modificare tutti i parametri generici con i nomi e le arn delle risorse che hai creato.
4. Clicca su "Deploy" per salvare il codice.

## Passo 6: Configurare gli eventi di Lambda

1. Nella stessa pagina della funzione Lambda, vai alla sezione "Function overview".
2. Clicca su "Add trigger" e seleziona "EventBridge".
3. Clicca su "Create a new rule".
4. Scegli un nome e inserisci una espressione Cron per schedulare l'intervallo temporale.
5. Configura l'evento EventBridge per attivare la funzione Lambda a intervalli regolari.

## Passo 7: Testare la funzione Lambda

1. Nella pagina della funzione Lambda, clicca su "Test".
2. Seleziona o crea un nuovo evento di test e clicca su "Test" per eseguire la funzione.
3. Se tutto va a buon fine, vedrai "COMPLETATED" nei log del test e nel Bucket 2 nuovi file: .zip e .log.
4. ATTENZIONE: l'export della casella di posta può essere eseguita solo una volta al giorno.

## Passo 8: Monitorare e risolvere i problemi

1. Monitora l'esecuzione della tua funzione Lambda nella console CloudWatch.
2. Se incontri problemi, controlla i log della funzione Lambda per individuare eventuali errori o problemi di esecuzione.
