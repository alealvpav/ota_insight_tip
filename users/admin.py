from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.db.models import Sum
from django.urls import reverse
from django.utils.html import format_html

from .models import User


class MoreThanAThousandBilled(SimpleListFilter):
    title = "billed more than 1000"
    parameter_name = "is_billed_a_thousand"

    def lookups(self, request, model_admin):
        return(
            ("yes", "Yes"),
            ("no", "No"),
        )

    def queryset(self, request, queryset):
        """
        The queryset will filter the users that have been billed (sum of all
        his related invoices amount) at least 1000 (if filter set to "yes")
        and less than 1000 if it's set to "no"
        """
        pks_above_1000 = queryset.values_list("pk", flat=True).annotate(
            total_invoiced_amount=Sum("invoice__amount")
        ).filter(total_invoiced_amount__gte=float(1000))
        if self.value() == "yes":
            return queryset.filter(pk__in=list(pks_above_1000))
        elif self.value() == "no":
            return queryset.exclude(pk__in=list(pks_above_1000))
        else:
            return queryset


class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "username", "email", "total_invoiced_amount_link", "invoice_currency")
    list_filter = (MoreThanAThousandBilled,)
    change_form_template = "admin/users/change_form.html"

    @staticmethod
    def _get_invoiced_amount_link(obj):
        base_url = reverse("admin:invoices_invoice_changelist")
        get_filter = f"?user__id__exact={obj.pk}"
        html_link = f"<a href=\"{base_url}{get_filter}\">{obj.total_invoiced_amount}</a>"
        return format_html(html_link)

    def total_invoiced_amount_link(self, obj):
        """
        Gives the content for the cell containing a link (<a> html tag) to the
        user invoices' page in the admin site while displaying the total amount
        :param obj: User obj
        :type obj: User
        :return: html safe text containing the <a> tag with the invoices link
        :rtype: str
        """
        html_link = f"<a href=\"{obj.get_invoices_admin_url()}\">{obj.total_invoiced_amount}</a>"
        return format_html(html_link)

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        """
        We need to add extra information related to the user to show it in the edit form.
        - Last 3 invoices
        - Link to see all user's invoices
        """
        extra_context = {}
        if object_id:
            user = self.get_object(request, object_id)
            last_invoices = user.invoice_set.order_by("-creation_date")[:3]
            invoices_url = user.get_invoices_admin_url()
            extra_context = {
                "last_invoices": last_invoices,
                "invoices_url": invoices_url,
            }
        return super(UserAdmin, self).changeform_view(request, object_id, form_url, extra_context)


# Register your models here.
admin.site.register(User, UserAdmin)
