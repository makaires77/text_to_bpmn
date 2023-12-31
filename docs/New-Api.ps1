# New-Api.ps1

# Define the root directory
$rootDir = ".\"

# Define the directories to be created
$dirs = @(
    "api",
    "api\adapters",
    "api\domain"
)

# Create each directory
$dirs | ForEach-Object {
    $dirPath = Join-Path -Path $rootDir -ChildPath $_
    if(!(Test-Path -Path $dirPath)) {
        New-Item -ItemType Directory -Force -Path $dirPath
    }
}

# Define the files to be created
$files = @(
    "api\app.py",
    "api\adapters\__init__.py",
    "api\adapters\orm_adapter.py",
    "api\domain\__init__.py",
    "api\domain\models.py",
    "api\domain\services.py"
)

# Create each file
$files | ForEach-Object {
    $filePath = Join-Path -Path $rootDir -ChildPath $_
    if(!(Test-Path -Path $filePath)) {
        New-Item -ItemType File -Force -Path $filePath
    }
}