from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an post to edit it.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        return request.method in permissions.SAFE_METHODS

class PostPermission(permissions.BasePermission):
    """
    Разрешение, позволяющее только авторам поста и администраторам получить доступ к изменению и удалению поста
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the post.
        return request.user == obj.author or request.user.is_staff

class CommentPermission(permissions.BasePermission):
    """
    Разрешение, позволяющее только авторам комментария и администраторам получить доступ к изменению и удалению комментария
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the post and admin.
        return request.user == obj.post.author or request.user.is_staff

class IsAdminOrReadOnly(permissions.IsAdminUser):
    """
    Разрешение, позволяющее только авторам администраторам получить доступ к изменению и удалению сущности
    """

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin