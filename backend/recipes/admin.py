from django.contrib import admin
from recipes.models import AmountIngredient, Favorites, Ingredient, Recipe, Tag, Cart


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Отображает ингредиенты в панели администратора."""
    list_display = ('name', 'measurement_unit')
    search_fields = ('name', 'measurement_unit')
    list_filter = ('name', 'measurement_unit')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Отображает теги в панели администратора."""
    list_display = ('name', 'slug', 'color')
    search_fields = ('name',)


class IngredientLnline(admin.TabularInline):
    model = AmountIngredient
    extra = 10


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Отображает рецепты в панели администратора."""
    list_display = ('author', 'name', 'cooking_time')
    search_fields = ('name', 'author', 'tags')
    list_filter = ('author', 'name', 'tags')
    inlines = (IngredientLnline,)

    def count_favorites(self, obj):
        return obj.favorites.count()


@admin.register(Favorites)
class FavoriteAdmin(admin.ModelAdmin):
    """Отображает подписки на авторов в панели администратора."""
    list_display = ('user', 'recipe')
    search_fields = ('user',)
    list_filter = ('user',)


@admin.register(Cart)
class FavoriteAdmin(admin.ModelAdmin):
    """Отображает корзину в панели администратора."""
    list_display = ('user', 'recipe')
    search_fields = ('user',)
    list_filter = ('user',)
