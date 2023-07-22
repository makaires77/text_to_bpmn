function Create-ProspectSpecialistStructure {
    $directories = @(
        'src\domain',
        'src\services\prospect_specialist',
        'src\adapters',
        'test\unit',
        'test\integration',
        'pipelines'
    )

    $files = @(
        'src\domain\prospect_specialist.py', 'src\domain\prospect_specialist.go', 'src\domain\repository_interface.py', 'src\domain\repository_interface.go', 'src\domain\service_interface.py', 'src\domain\service_interface.go',
        'src\services\prospect_specialist\service.py', 'src\services\prospect_specialist\service.go',
        'src\adapters\repository.py', 'src\adapters\repository.go', 'src\adapters\lattes_service.py', 'src\adapters\lattes_service.go',
        'test\unit\prospect_specialist_test.py', 'test\unit\prospect_specialist_test.go',
        'test\integration\prospect_specialist_integration_test.py', 'test\integration\prospect_specialist_integration_test.go',
        'pipelines\prospect_specialist_pipeline.py', 'pipelines\prospect_specialist_pipeline.go'
    )

    foreach ($directory in $directories) {
        if (!(Test-Path -Path $directory)) {
            New-Item -ItemType Directory -Path $directory -Force | Out-Null
        }
    }

    foreach ($file in $files) {
        if (!(Test-Path -Path $file)) {
            New-Item -ItemType File -Path $file -Force | Out-Null
        }
    }
}

# Call the function to create the structure for the "Prospect Specialist" use case
Create-ProspectSpecialistStructure
