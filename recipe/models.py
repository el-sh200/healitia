from django.db import models

# Create your models here.
from django.db import models

from django.utils.translation import gettext_lazy as _

from account.models import User
from utils.models import AbstractDateTimeModel


class Ingredient(AbstractDateTimeModel):
    name = models.CharField(
        _('name'),
        max_length=100,
    )
    cover = models.ImageField(
        upload_to='ingredient/cover/',
        null=True,
        blank=True,
        verbose_name=_('cover')
    )

    class Meta:
        verbose_name = _('ingredient')
        verbose_name_plural = _('ingredients')

    def __str__(self):
        return self.name


class Cuisine(AbstractDateTimeModel):
    name = models.CharField(
        _('name'),
        max_length=50,
    )

    class Meta:
        verbose_name = _('cuisine')
        verbose_name_plural = _('cuisine')

    def __str__(self):
        return self.name


class Recipe(AbstractDateTimeModel):
    title = models.CharField(
        _('title'),
        max_length=200,
    )
    description = models.TextField(
        verbose_name=_('description')
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeItem',
        verbose_name=_('ingredients')
    )
    cuisines = models.ManyToManyField(
        'Cuisine',
        blank=True,
        verbose_name=_('cuisines')
    )
    cover = models.ImageField(
        upload_to='recipe/cover/',
        null=True,
        blank=True,
        verbose_name=_('cover')
    )
    ready_time = models.PositiveIntegerField(
        verbose_name=_('ready_time')
    )
    servings = models.PositiveIntegerField(
        verbose_name=_('servings')
    )

    class Meta:
        verbose_name = _('recipe')
        verbose_name_plural = _('recipes')

    def __str__(self):
        return self.title


class RecipeItem(AbstractDateTimeModel):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name=_('recipe')
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name=_('ingredient')
    )
    quantity = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name=_('quantity')
    )
    unit = models.CharField(
        max_length=20,
        verbose_name=_('unit')
    )

    class Meta:
        verbose_name = _('recipe item')
        verbose_name_plural = _('recipe item')

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.ingredient.name} in {self.recipe.title}"


class InstructionStep(AbstractDateTimeModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')
    order = models.PositiveIntegerField()
    description = models.TextField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Step {self.order} for {self.recipe.title}"


class FavoriteRecipe(AbstractDateTimeModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name=_('recipe'),
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('timestamp')
    )

    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"{self.user.email}'s favorite - {self.recipe.title}"
