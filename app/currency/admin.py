from django.contrib import admin
from currency.models import Rate




class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale', 'buy', 'cread', 'source', 'type')
    list_filter = ('type', 'source', ('cread'))
    search_fields = ('type', 'source')
    readonly_fields = ('sale', 'buy')

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(Rate, RateAdmin)
