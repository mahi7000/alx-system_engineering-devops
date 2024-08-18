Postmortem (Web stack debugging #1)

Issue Summary
Duration: July 8, 2024 6:00 AM to July 12, 2024 6:00 AM (EAT).
Impact: The Nginx server was incorrectly configured to listen on port 80, which caused conflicts with other services.
Root Cause: The misconfiguration of the Nginx configuration file that was directing it to listen to port 80.
Timeline
July 8, 2024 6:00 AM: The issue was first detected because of a monitoring alert.
Actions Taken: I investigated the problem, focusing on the Nginx configuration files and network settings to identify the root cause.
Misleading Investigation: I thought it was a network connectivity issue rather than a misconfiguration in the Nginx server, at first.
July 12, 2024 6:00 AM: The issue was resolved using the following commands
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo service nginx restart
Root Cause and Resolution
Root Cause: The misconfiguration of the Nginx server was directing it to listen on port 80, conflicting with other services and causing the outage.
Resolution: The issue was resolved by creating a symbolic link for the default Nginx configuration file and restarting the Nginx service, ensuring it listened on the correct port.
Corrective and Preventative Measures
Enhance configuration management processes to avoid similar misconfigurations in the future.
Implement automated monitoring and alerts for critical services to promptly detect and address issues.
Conduct regular audits of server configurations to prevent potential conflicts and maintain system integrity.
Conduct a comprehensive review of all server configurations to identify and rectify any lingering misconfigurations that could potentially impact service availability.
Implement version control for configuration files to track changes and facilitate easy rollback in case of misconfigurations.
Enhance documentation practices to ensure clear and up-to-date records of server configurations, making it easier for team members to understand and troubleshoot issues.
Schedule regular training sessions for the operations team to stay updated on best practices for server configuration and management.
Establish a strict change control process that includes peer reviews and testing before implementing any configuration changes in production environments.
Implement a robust disaster recovery plan that includes regular backups and testing to ensure rapid recovery in the event of system failures.

