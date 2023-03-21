from django.contrib import admin

from .models import Club, ClubMember


class ClubMemberInline(admin.TabularInline):
    model = ClubMember
    extra = 1


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ["name", "is_free", "entry_fee", "created_at"]
    inlines = [ClubMemberInline]


@admin.register(ClubMember)
class ClubMemberAdmin(admin.ModelAdmin):
    list_display = ["club", "user", "role", "designation", "created_at"]
    list_filter = ["club"]
