Stop-VM -Name sonofubuntu

Checkpoint-VM -Name sonofubuntu -SnapshotName snapshot1

Start-VM -Name sonofubuntu

Get-VMNetworkAdapter -VMName sonofubuntu | Connect-VMNetworkAdapter -SwitchName LAN-Internal