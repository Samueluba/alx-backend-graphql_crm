INSTALLED_APPS = [
    # ... other installed apps
    'django_crontab',
]

CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.log_crm_heartbeat'),
]

