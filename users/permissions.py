from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit/delete it.
    Read-only permissions are allowed to any request.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only methods (GET, HEAD, OPTIONS) always allow
        if request.method in permissions.SAFE_METHODS:
            return True

        # DonorProfile case (user field)
        if hasattr(obj, "user"):
            return obj.user == request.user

        # BloodRequest case (created_by field)
        if hasattr(obj, "created_by"):
            return obj.created_by == request.user

        # Blog case (author field)
        if hasattr(obj, "author"):
            return obj.author == request.user

        return False
