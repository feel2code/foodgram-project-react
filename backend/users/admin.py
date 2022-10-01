from users.models import Follow, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Отображает пользователей в панели администратора."""
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('email', 'username', )


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    """Отображает подписки на авторов в панели администратора."""
    list_display = ('user', 'author')
    search_fields = ('user',)
    list_filter = ('user', )
