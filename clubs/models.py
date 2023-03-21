from django.db import models

from accounts.models import User


class Club(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    eligibility = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_free = models.BooleanField(default=False)
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "clubs"

    def __str__(self) -> str:
        return self.name
    

class ClubMember(models.Model):
    class Role(models.TextChoices):
        ADMIN = ("admin", "Admin")
        MEMBER = ("member", "Member")

    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=Role.choices, default="member")
    designation = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "club_members"

    def __str__(self) -> str:
        return str(self.id)