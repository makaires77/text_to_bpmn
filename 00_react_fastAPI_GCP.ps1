function Create-ReactFastAPIGCPStructure {
    $directories = @(
        'src\app',
        'src\adapters',
        'src\domain',
        'src\services\prospect_specialist',
        'src\services\patent_analysis',
        'src\services\maturity_analysis',
        'test\unit',
        'test\integration',
        'docs',
        'latex-templates',
        'pipelines'
    )

    $files = @(
        'src\app\main.go', 'src\app\main.py',
        'src\adapters\db.go', 'src\adapters\db.py', 'src\adapters\network.go', 'src\adapters\network.py', 'src\adapters\gui.go', 'src\adapters\gui.py',
        'src\domain\business_logic.go', 'src\domain\business_logic.py',
        'src\services\prospect_specialist\service.go', 'src\services\prospect_specialist\service.py',
        'src\services\patent_analysis\service.go', 'src\services\patent_analysis\service.py',
        'src\services\maturity_analysis\service.go', 'src\services\maturity_analysis\service.py',
        'test\unit\test_main.go', 'test\unit\test_main.py',
        'test\integration\test_integration.go', 'test\integration\test_integration.py',
        'docs\README.md', 'docs\CONTRIBUTING.md',
        'latex-templates\template1.tex', 'latex-templates\template2.tex', 'latex-templates\template3.tex',
        'pipelines\pipeline1.go', 'pipelines\pipeline1.py', 'pipelines\pipeline2.go', 'pipelines\pipeline2.py', 'pipelines\pipeline3.go', 'pipelines\pipeline3.py'
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

# Call the function to create directory structure
Create-ReactFastAPIGCPStructure
