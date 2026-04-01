from rest_framework.permissions import BasePermission, SAFE_METHODS


def _is_librarian(user):
    return bool(user and user.is_authenticated and (user.is_staff or getattr(user, 'role', '') == 'librarian'))


class IsLibrarianOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return _is_librarian(request.user)


class IsLibrarian(BasePermission):
    def has_permission(self, request, view):
        return _is_librarian(request.user)