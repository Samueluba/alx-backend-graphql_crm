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

#!/bin/bash

# Path to your Django project
PROJECT_DIR="/full/path/to/alx-backend-graphql_crm"

# Log file
LOG_FILE="/tmp/customer_cleanup_log.txt"

# Run Django shell command
DELETED_COUNT=$(cd $PROJECT_DIR && python manage.py shell -c "
from datetime import datetime, timedelta
from crm.models import Customer, Order

one_year_ago = datetime.now() - timedelta(days=365)
inactive_customers = Customer.objects.filter(order__date__lt=one_year_ago).distinct()
count = inactive_customers.count()
inactive_customers.delete()
print(count)
")

# Log the deletion with timestamp
echo \"\$(date '+%Y-%m-%d %H:%M:%S') - Deleted \$DELETED_COUNT inactive customers\" >> $LOG_FILE
