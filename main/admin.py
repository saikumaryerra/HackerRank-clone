from django.contrib import admin
from .models import Room, RoomMember, InterviewList


class InterviewListAdmin(admin.ModelAdmin):
    list_display = ('interviewer', 'candidate', 'score', 'active')


admin.site.register(InterviewList, InterviewListAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('roomname', 'users')


admin.site.register(Room, RoomAdmin)


class RoomMemberAdmin(admin.ModelAdmin):
    list_display = ('room', 'name')


admin.site.register(RoomMember, RoomMemberAdmin)
