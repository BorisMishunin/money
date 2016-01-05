from rest_framework import permissions

class UserPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print('author', request)
        return obj.author == request.user