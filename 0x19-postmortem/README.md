Postmortem Report

Incident Date: August 17, 2024

Incident Title: SSH Access Timeout Due to Misconfigured UFW Firewall Rules

Incident Summary: On August 17, 2024, at approximately 15:00 GMT+1, access to the server via SSH became unavailable, resulting in a "Connection timed out" error. This issue persisted for over an hour, hindering remote server management and leading to delayed operations. The root cause was identified as an improperly configured UFW (Uncomplicated Firewall) that blocked incoming SSH connections.


Timestamp:
15:00 GMT+1: First attempt to access the server via SSH failed with a "Connection timed out" error. Initial troubleshooting began, focusing on network connectivity and SSH service status.
15:15 GMT+1: Verified that the SSH service was running on the server. An Nmap scan was conducted to check the status of port 22 (SSH), which revealed that the port was filtered.
15:30 GMT+1: Investigated UFW firewall settings, suspecting that it might be the cause of the blocked SSH access.
15:45 GMT+1: Confirmed that UFW was enabled but did not have an explicit rule to allow SSH traffic. The default UFW configuration blocks all incoming traffic unless specified.
16:00 GMT+1: Applied the necessary firewall rule to allow SSH connections: 
sudo ufw allow ssh.
16:05 GMT+1: Verified that SSH access was restored successfully. Further checks confirmed no other services were affected.


Root Cause: The incident was caused by a misconfiguration in the UFW firewall settings. After enabling UFW, the default rules did not include an allowance for incoming SSH traffic, causing the firewall to block all attempts to connect via SSH.


Resolution: To resolve the issue, the following command was executed to modify the UFW ruleset:
sudo ufw allow ssh
This command allows incoming traffic on port 22, restoring SSH access to the server. After applying the rule, UFW was reloaded, and SSH access was tested and confirmed to be functional.


Impact:
Users Affected: Internal team members were unable to access the server remotely.
Duration: Approximately 1 hour and 15 minutes.
Business Impact: Delayed server management tasks, including configuration and deployment activities. No direct impact on end-user services


Lessons Learned:
Firewall Configuration Best Practices: It is crucial to verify firewall rules immediately after enabling UFW or similar security measures. Critical services like SSH must be explicitly allowed.
Automation and Scripting: To avoid manual errors, consider using automated scripts for initial server setup, including firewall configuration. These scripts should include all necessary rules to ensure essential services remain accessible.
Monitoring and Alerts: Implement real-time monitoring and alerting for SSH access issues. Early detection could have reduced the time to resolution.


Action Items:
Immediate:
Audit all servers to ensure UFW or other firewalls are correctly configured with rules that allow critical services like SSH, HTTP, and HTTPS.
Update server setup documentation to include steps for verifying firewall rules post-setup.

Short-Term:
Develop a standard configuration script for server initialization that includes firewall rule settings to allow SSH and other essential services.
Conduct a team-wide review and training on best practices for firewall management.

Long-Term:
Implement automated monitoring solutions that trigger alerts when SSH access fails multiple times within a short period.
Explore the use of configuration management tools like Ansible or Terraform to standardize and automate server and firewall configurations across environments.


Prepared by: Ohwoka Emmanuel
Date: August 17, 2024

