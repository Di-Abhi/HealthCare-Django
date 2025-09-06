from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners (created_by) to edit/delete it.
    """

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if hasattr(obj, 'created_by'):
            return obj.created_by == request.user
        return False