from django.contrib import admin
from .models import Recipe, Ingredient, Cuisine, RecipeItem, InstructionStep


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ('name',)


class RecipeItemInline(admin.TabularInline):
    model = RecipeItem
    extra = 1


class InstructionStepInline(admin.TabularInline):
    model = InstructionStep
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'ready_time', 'servings')
    list_filter = ('cuisines',)
    search_fields = ('title', 'description')
    filter_horizontal = ('cuisines',)
    inlines = [RecipeItemInline, InstructionStepInline, ]

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'cover', 'ready_time', 'servings', 'cuisines')
        }),
    )
