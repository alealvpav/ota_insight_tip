from django.contrib import admin
from .models import Invoice


class InvoiceAdmin(admin.ModelAdmin):
    exclude = ("visible",)
    list_display = ("pk", "number", "user", "amount", "currency")
    list_filter = ("user",)

    def has_delete_permission(self, request, obj=None):
        """
        Override to prevent admin panel users to delete invoices. This will
        make the delete button not to appear ever.
        :return: False
        :rtype: bool
        """
        return False

    def currency(self, obj):
        return obj.user.invoice_currency.code

    currency.short_desctiption = "Currency of the invoiced User"


# Register your models here.
admin.site.register(Invoice, InvoiceAdmin)
