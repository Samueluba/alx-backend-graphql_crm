#!/bin/bash

0 2 * * 0 /home/ubuntu/alx-backend-graphql_crm/

Objective
Set up a GraphQL endpoint and define your first schema and query.

Instructions
1. Create a Shell Script: * Create a shell script clean_inactive_customers.sh in the crm/cron_jobs directory. * The script should:

Use Django’s manage.py shell to execute a Python command that deletes customers with no orders since a year ago.
Log the number of deleted customers to a /tmp/customer_cleanup_log.txt with a timestamp.
Include a shebang (#!/bin/bash) and ensure the script is executable (chmod +x).
2. Create a Crontab Entry:

Create a filecrm/cron_jobs/customer_cleanup_crontab.txt with a single line specifying the cron job to run the script every Sunday at 2:00 AM.
Ensure no extra newlines in the file.
Repo:

GitHub repository: alx-backend-graphql_crm
File: clean_inactive_customers.sh, customer_cleanup_crontab.txt
