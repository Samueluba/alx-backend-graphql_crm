#!/bin/bash
# clean_inactive_customers.sh
# Deletes customers with no orders in the past year and logs the result.

# Navigate to the project root (assuming this script lives in crm/cron_jobs)
cd "$(dirname "$0")/../"

# Run Django shell command to delete inactive customers and log the output
deleted_count=$(python3 manage.py shell -c "
from django.utils import timezone
from datetime import timedelta
from crm.models import Customer

one_year_ago = timezone.now() - timedelta(days=365)
deleted, _ = Customer.objects.filter(last_order_date__lt=one_year_ago).delete()
print(deleted)
")

# Log result with timestamp
timestamp=$(date '+%Y-%m-%d %H:%M:%S')
echo \"[$timestamp] Deleted customers: $deleted_count\" >> /tmp/customer_cleanup_log.txt

