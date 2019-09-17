# Ping list of machines 

$machineNames = ".\machines.csv" #csv with column of machine names
$outputFile = ".\output.txt"

Get-Content $machineNames | ForEach {

    # Use the Test-Connection cmdlet to determine if the machine is responding
    $pinged = Test-Connection -ComputerName $_ -Count 1 -Quiet
    # Use an If statement to determine if the machine responded or not and output accordingly
    If ($pinged) { Write-Host "$_ - OK" -foreground "red"
        Add-content $outputFile -value $_
        }
    Else {Write-Host "$_ - No Reply"}
    }
