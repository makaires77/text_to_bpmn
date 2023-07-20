function New-Monorepo {
    param (
        [Parameter(Mandatory=$true)]
        [string]$MonorepoName,

        [Parameter(Mandatory=$false)]
        [string[]]$Packages = "api", "app", "common", "models", "services", "utils",

        [Parameter(Mandatory=$false)]
        [string[]]$SubDirs = "src", "test", "doc"
    )

    # Cria o diretório do monorepo se ele ainda não existir.
    if (!(Test-Path -Path $MonorepoName)) {
        New-Item -ItemType Directory -Path $MonorepoName
    }

    # Cria uma pasta para cada pacote dentro do monorepo se ela ainda não existir.
    foreach ($package in $Packages) {
        if (!(Test-Path -Path "$MonorepoName/$package")) {
            New-Item -ItemType Directory -Path "$MonorepoName/$package"
        }
    }

    # Para cada pacote, cria subdiretórios se eles ainda não existirem.
    foreach ($package in $Packages) {
        foreach ($subDir in $SubDirs) {
            if (!(Test-Path -Path "$MonorepoName/$package/$subDir")) {
                New-Item -ItemType Directory -Path "$MonorepoName/$package/$subDir"
            }
        }
    }
}