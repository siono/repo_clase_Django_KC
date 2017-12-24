from django.contrib import admin
from django.utils.safestring import mark_safe

from movies.models import Category, Movie

#poner la cabecera en el administrador
admin.site.site_header = "IPDB Backoffice"
admin.site.site_title = admin.site.site_header


admin.site.register(Category)
#admin.site.register(Movie)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = ('title', 'release_date', 'rating', 'user_full_name', 'category')
    list_filter = ('category','user','release_date')
    search_fields = ('title','director_name','sumary')

    def user_full_name(self, movie):
        return "{0} {1}".format(movie.user.first_name,movie.user.last_name)
    user_full_name.short_description = "Movie owner" #para renombrar la columna del administrador
    user_full_name.admin_order_field = "user__first_name" #se poner doble _ en first_name ya que user es una foreng_key en la tabla movie

    def get_image_html(self, movie):
        return mark_safe('<img src="{0}" alt="{1}" height="100">'.format(movie.image, movie.title))

    get_image_html.short_description = "Movie poster"

    readonly_fields = ('created_at', 'modified_at','get_image_html')
    #Phython no sabe interpretar tublas con un solo elemento por eso ponemos una coma (,) al final
    #Campos que mostramos en detalle de peliculas
    fieldsets = (
        (None, {
            'fields': ('title', 'sumary')
        }),
        ("Category & Rating", {
            'fields': ('category', 'rating')
        }),
        ("Additional info", {
            'fields': ('director_name', 'release_date', 'get_image_html', 'image', 'user')
        }),
        ("Creation & modification dates", {
            'fields': ('created_at', 'modified_at'),
            'classes': ('collapse',),
            'description': 'This fields are auto-generated'
        })
    )
