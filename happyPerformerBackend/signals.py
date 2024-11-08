from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from .models import *   
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Company)
def create_default_leave_types(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Creating default leave types for company ID {instance.c_id}")
        Leavetype = apps.get_model('happyPerformerBackend', 'Leavetype')
        leave_types = [
            {'LeaveType': 'Casual Leave', 'Description': 'Casual Leave Description', 'Limit': 15},
            {'LeaveType': 'Medical Leave', 'Description': 'Medical Leave Description', 'Limit': 15},
            {'LeaveType': 'Earned Leave', 'Description': 'Earned Leave Description', 'Limit': 20},
            {'LeaveType': 'LOP Leave', 'Description': 'LOP Leave Description', 'Limit': 20},
        ]
        
        for leave in leave_types:
            if not Leavetype.objects.filter(LeaveType=leave['LeaveType'], company=instance).exists():
                Leavetype.objects.create(
                    LeaveType=leave['LeaveType'],
                    company=instance,
                    Description=leave['Description'],
                    Limit=leave['Limit']
                )
                logger.info(f"Leave type '{leave['LeaveType']}' created for company ID {instance.c_id}.")
            else:
                logger.info(f"Leave type '{leave['LeaveType']}' already exists for company ID {instance.c_id}.")
