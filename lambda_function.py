import boto3
import time

# Funzione per creare una cartella S3
def create_s3_folder(bucket_name, folder_name):
    s3 = boto3.client('s3')
    try:
        # Verifica se la cartella esiste già
        s3.head_object(Bucket=bucket_name, Key=(folder_name + '/'))
        print("Cartella " + folder_name + " già esistente!")
    except:
        # Crea la cartella se non esiste
        s3.put_object(Bucket=bucket_name, Key=(folder_name + '/'))
        print("Cartella " + folder_name + " creata!")

# Funzione per esportare la casella di posta
def export_mailbox(user_id, s3_prefix):
    organization_id = 'Inserisci_ID_OrganizzazioneWorkmail'
    kms_key_arn = 'Inserisci_KMS_Key_ARN'
    s3_bucket = 'Inserisci_Nome_Bucket_S3'
    
    # Creazione della cartella se non esiste
    print("Creazione cartella:")
    create_s3_folder(s3_bucket, s3_prefix)

    workmail = boto3.client('workmail')

    # Avvio il lavoro di esportazione della casella di posta
    workmail_response = workmail.start_mailbox_export_job(
        OrganizationId=organization_id,
        EntityId=user_id,
        Description=f'Export {user_id} mailbox',
        RoleArn='Inserisci_Role_ARN_della_Lambda',
        KmsKeyArn=kms_key_arn,
        S3BucketName=s3_bucket,
        S3Prefix=s3_prefix
    )

    job_id = workmail_response['JobId']
    print("Avvio esportazione:")

    # Aspetta che il lavoro di esportazione sia completato
    while True:
        response = workmail.describe_mailbox_export_job(OrganizationId=organization_id, JobId=job_id)
        if 'State' in response:
            job_state = response['State']
            print(job_state)
            print(response)
            if job_state in ['COMPLETE', 'FAILED', 'CANCELLED']:
                break
        time.sleep(10)

def lambda_handler(event, context):

    # Dati per il primo utente
    user_id_1 = 'Inserisci_ID_Utente_1'
    s3_prefix_1 = 'Inserisci_Prefix_1'
    export_mailbox(user_id_1, s3_prefix_1)

    # Dati per il secondo utente
    user_id_2 = 'Inserisci_ID_Utente_2'
    s3_prefix_2 = 'Inserisci_Prefix_2'
    export_mailbox(user_id_2, s3_prefix_2)

    return {
        'statusCode': 200,
        'body': 'Lavoro di esportazione terminato con successo'
    }
