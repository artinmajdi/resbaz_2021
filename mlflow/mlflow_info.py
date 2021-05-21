
def load():

    postgres_connection_type = { 'direct':    ('5432', 'data7-db1.cyverse.org'),
                                 'ssh-tunnel': ('5000', 'localhost') 
                                 }

    port, host = postgres_connection_type['ssh-tunnel']


    username = "artinmajdi"
    password = '1234'
    database_name = 'resbaz2021'
    dialect_driver = 'postgresql'
    server = f'{dialect_driver}://{username}:{password}@{host}:{port}/{database_name}'


    """ Setting up the artifact server """ 
    artifact_server = 'data7_db1'

    Artifacts = {
        'local':      "file:/<path-to-artifact-store>",
        'hpc':        'sftp://<user>:{password}@filexfer.hpc.arizona.edu:<path-to-artifact-store>',
        'atmosphere': 'sftp://<user>:{password}@<ip-address>:<path-to-artifact-store>',
        'cyverse':    'file:/<path-to-artifact-store>',
        'data7_db1':  'sftp://artinmajdi:temp2_data7_b@data7-db1.cyverse.org:/home/artinmajdi/mlflow_data/artifact_store'}
    
    return server, Artifacts[artifact_server]