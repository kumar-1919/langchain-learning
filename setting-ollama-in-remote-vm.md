To achieve your goal of:

1. **Autostarting the Ollama server after a reboot** on a **remote VM**,
2. **Making the Ollama server accessible to all IP addresses**, and
3. Doing it **entirely via `cmd` or PowerShell** (no GUI, suitable for automation),

Here’s a **step-by-step PowerShell-based solution** (can be run on the remote VM or automated via remote execution):

---

### ✅ Step 1: Configure Ollama to Bind to All Interfaces

By default, Ollama binds to `localhost`. To expose it to **all IPs**, you’ll need to configure the server to bind to `0.0.0.0`.

#### PowerShell Command to Set Environment Variable Persistently:

```powershell
[System.Environment]::SetEnvironmentVariable("OLLAMA_HOST", "0.0.0.0:11434", "Machine")
```

This sets `OLLAMA_HOST=0.0.0.0:11434` **system-wide** so it persists across reboots.

---

### ✅ Step 2: Create a Scheduled Task to Autostart Ollama on Reboot

We’ll create a Windows Scheduled Task that runs `ollama serve` at startup.

#### PowerShell Script to Create Task:

```powershell
$action = New-ScheduledTaskAction -Execute "ollama" -Argument "serve"
$trigger = New-ScheduledTaskTrigger -AtStartup
$principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -RunLevel Highest

Register-ScheduledTask -TaskName "StartOllamaServer" -Action $action -Trigger $trigger -Principal $principal
```

> 💡 This runs the `ollama serve` command as the SYSTEM user at system startup.

---

### ✅ Step 3: (Optional) Open Firewall Port 11434

You’ll need to allow incoming traffic on port `11434` for remote access.

#### PowerShell Command:

```powershell
New-NetFirewallRule -DisplayName "Allow Ollama Server" -Direction Inbound -LocalPort 11434 -Protocol TCP -Action Allow
```

---

### ✅ Step 4: Verify Remotely from Local Machine

Once the remote VM is rebooted, test from your **local machine**:

```bash
curl http://<remote-vm-ip>:11434
```

You should get a response from the Ollama server.

---

Let me know if you're using **Linux** instead of Windows on the VM — the commands would differ (using `systemd` instead).
