# Define o caminho da pasta raiz do projeto
$currentScriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$rootFolderPath = Join-Path -Path $currentScriptPath -ChildPath "..\TEXT_TO_BPMN"

# Verifica se a pasta 'api' já existe
$apiFolder = Join-Path -Path $rootFolderPath -ChildPath "api"
if (-Not (Test-Path $apiFolder)) {
    # Cria a pasta 'api' caso não exista
    New-Item -ItemType Directory -Path $apiFolder | Out-Null

    # Verifica se a pasta 'adapters' já existe
    $adaptersFolder = Join-Path -Path $apiFolder -ChildPath "adapters"
    if (-Not (Test-Path $adaptersFolder)) {
        # Cria a pasta 'adapters' caso não exista
        New-Item -ItemType Directory -Path $adaptersFolder | Out-Null

        # Cria o arquivo 'orm_adapter.py' dentro da pasta 'adapters'
        $ormAdapterFile = Join-Path -Path $adaptersFolder -ChildPath "orm_adapter.py"
        if (-Not (Test-Path $ormAdapterFile)) {
            @"
            # Coloque aqui o conteúdo do arquivo orm_adapter.py
            "@ | Out-File -Encoding UTF8 -FilePath $ormAdapterFile
        } else {
            Write-Host "O arquivo 'orm_adapter.py' já existe e não será sobrescrito."
        }
    } else {
        Write-Host "A pasta 'adapters' já existe e não será sobrescrita."
    }

    # Verifica se a pasta 'domain' já existe
    $domainFolder = Join-Path -Path $apiFolder -ChildPath "domain"
    if (-Not (Test-Path $domainFolder)) {
        # Cria a pasta 'domain' caso não exista
        New-Item -ItemType Directory -Path $domainFolder | Out-Null

        # Cria o arquivo 'models.py' dentro da pasta 'domain'
        $modelsFile = Join-Path -Path $domainFolder -ChildPath "models.py"
        if (-Not (Test-Path $modelsFile)) {
            @"
            # Coloque aqui o conteúdo do arquivo models.py
            "@ | Out-File -Encoding UTF8 -FilePath $modelsFile
        } else {
            Write-Host "O arquivo 'models.py' já existe e não será sobrescrito."
        }

        # Cria o arquivo 'services.py' dentro da pasta 'domain'
        $servicesFile = Join-Path -Path $domainFolder -ChildPath "services.py"
        if (-Not (Test-Path $servicesFile)) {
            @"
            # Coloque aqui o conteúdo do arquivo services.py
            "@ | Out-File -Encoding UTF8 -FilePath $servicesFile
        } else {
            Write-Host "O arquivo 'services.py' já existe e não será sobrescrito."
        }
    } else {
        Write-Host "A pasta 'domain' já existe e não será sobrescrita."
    }
} else {
    Write-Host "A pasta 'api' já existe e não será sobrescrita."
}
