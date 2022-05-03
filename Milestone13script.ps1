Get-VM | Get-VMNetworkAdapter | ft VMName, IPAddresses, status

Get-VM | ft Name, uptime, CPUUsage, MemoryAssigned, VirtualMachineSubType, ComputerName

Write-Host "[1] Shutdown VM"
Write-Host "[2] Start VM"
Write-Host "[3] Snapshot VM"
Write-Host "[4] Change Netork of VM"
Write-Host "[5] Restore Snapshot"
Write-Host "[6] Change VM Memory"

$menu = Read-Host "Please make a selection"

if ($menu -match 1) {
$vmName = Read-Host -Prompt "VM to shutdown"
Stop-VM -Name $vmName
}

elseif ($menu -match 2) {
$vmName = Read-Host -Prompt "VM to start"
Start-VM -Name $vmName
}
elseif ($menu -match 3) {

$vmName = Read-Host -Prompt "VM to snapshot"

Stop-VM -Name $vmName

Checkpoint-VM -Name $vmName -SnapshotName snapshot1

Start-VM -Name $vmName
}
elseif ($menu -match 4) {
$vmName = Read-Host -Prompt "VM to change network of"
$vmNetwork = Read-Host -Prompt "Network to put VM on"
Get-VMNetworkAdapter -VMName $vmName | Connect-VMNetworkAdapter -SwitchName $vmNetwork
}
elseif ($menu -match 5) {
Restore-VMCheckpoint -Name 'snapshot1' -VMName sonofubuntu
}
elseif ($menu -match 6) {
$vmName1 = Read-Host "Which VM do you want to add memory too? "
Stop-VM -Name $vmName1
Set-VMMemory $vmName1 -StartupBytes 10GB
Start-VM -Name $vmName1
}

