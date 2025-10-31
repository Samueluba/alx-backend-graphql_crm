#!/bin/bash
# clean_inactive_customers.sh
# Deletes customers with no orders since a year ago and logs results

LOG_FILE="/tmp/customer_cleanup_log.txt"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Run Django shell command to delete inactive customers
DELETED_COUNT=$(python manage.py shell <<'END'
from datetime import datetime, timedelta
from crm.models import Customer

one_year_ago = datetime.now() - timedelta(days=365)
inactive_customers = Customer.objects.filter(last_order_date__lt=one_year_ago)
count = inactive_customers.count()
inactive_customers.delete()
print(count)
END
)

# Log results
echo "$TIMESTAMP - Deleted $DELETED_COUNT inactive customers" >> "$LOG_FILE"
