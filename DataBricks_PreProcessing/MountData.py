client_id = ""  # Application (client) ID
tenant_id = ""  # Directory (tenant) ID
client_secret = ""  # Client secret

configs = {
    "fs.azure.account.auth.type": "OAuth",
    "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id": client_id,
    "fs.azure.account.oauth2.client.secret": client_secret,
    "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
}

# Mount the ADLS Gen2 filesystem using the service principal credentials
dbutils.fs.mount(
    source = f"abfss://raw-data@stressdetectionstorage.dfs.core.windows.net/",
    mount_point = "/mnt/stressdata",
    extra_configs = configs
)

# Verify the mount
display(dbutils.fs.ls("/mnt/stressdata"))




client_id = ""  # Application (client) ID
tenant_id = ""  # Directory (tenant) ID
client_secret = ""  # Client secret

configs = {
    "fs.azure.account.auth.type": "OAuth",
    "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id": client_id,
    "fs.azure.account.oauth2.client.secret": client_secret,
    "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
}

# Mount the ADLS Gen2 filesystem for processed-data using the service principal credentials
dbutils.fs.mount(
    source = f"abfss://processed-data@stressdetectionstorage.dfs.core.windows.net/",  # Change to the processed-data container
    mount_point = "/mnt/processedstressdata",  # New mount point for processed data
    extra_configs = configs
)
