# -*- encoding: utf-8 -*-
import datetime

from django.contrib import admin
from django.core.urlresolvers import reverse
from django import forms
from django.http import HttpResponseRedirect

from project.encefal.forms import LivreVendreForm, VendeurForm
from project.encefal.models import (
                                    Vendeur, Session,
                                    Livre, Facture,
                                    ETAT_LIVRE_CHOICES,
                                    Exemplaire, Reception,
                                    Vente
                                   )

class LivreFormInline(admin.TabularInline):
    exclude = ['facture', 'actif', 'etat', 'livre']
    model = Exemplaire
    form = LivreVendreForm
    fields = ['isbn', 'titre', 'auteur', 'prix']
    extra = 1

class SessionAdmin(admin.ModelAdmin):
    exclude = ('actif',)
    list_display = ('nom', 'date_debut', 'date_fin',)

class ReceptionAdmin(admin.ModelAdmin):
    model = Reception
    exclude = ('actif',)
    inlines = [ LivreFormInline, ]

class VenteAdmin(admin.ModelAdmin):
    model = Vente
    readonly_fields = ('last_name','email','first_name')
    fields = ('last_name','email','first_name')

class LivreAdmin(admin.ModelAdmin):
    fields = ('isbn', 'titre', 'auteur', 'edition')
    list_display = ('isbn', 'titre', 'auteur', 'edition')
    search_fields = ['titre', 'auteur', 'isbn']

admin.site.register(Vendeur)
admin.site.register(Reception, ReceptionAdmin)
admin.site.register(Vente, VenteAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Livre, LivreAdmin)
admin.site.register(Facture)
admin.site.register(Exemplaire)
