from django.contrib import admin
from .models import Invoice


class InvoiceAdmin(admin.ModelAdmin):
    exclude = ('visible',)

    def has_delete_permission(self, request, obj=None):
        """
        Override to prevent admin panel users to delete invoices. This will
        make the delete button not to appear ever.
        :return: False
        :rtype: bool
        """
        return False


# Register your models here.
admin.site.register(Invoice, InvoiceAdmin)
