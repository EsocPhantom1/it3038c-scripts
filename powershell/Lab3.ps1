$IPAddress = (get-netipaddress).ipv4address | Select-String "192*" 
$CurrentUser = $env:USERNAME
$HostName = $env:COMPUTERNAME
$PowerShellVersion = $HOST.Version.Major
$CurrentDate =  Get-Date -Format "dddd, MMMM dd, yyyy"
$BODY = "This machine's IP address is $IPAddress. User is $CurrentUser. Hostname is $Hostname. Powershell Version $PowerShellVersion. Today's Date is $CurrentDate."
Send-MailMessage -To "leonardf@ucmail.uc.edu" -From "faissame2001@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential) 