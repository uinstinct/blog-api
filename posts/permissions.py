from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """Results in a 403 Forbidden if current permissions are not enough.
        GET request methods can be allowed and not other methods like POST, PUT, DELETE which can change the resource.
        Otherwise if the user is the author, then the user can make changes else not."""
        if request.method in permissions.SAFE_METHODS \
           or obj.author == request.user:
            return True

        else:
            return False
