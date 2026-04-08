from . test_recipe_base import RecipeTestBase
from parameterized import parameterized

from django.core.exceptions import ValidationError
 
class RecipeModelTest(RecipeTestBase):
    def setUp(self):
        self.recipe = self.make_recipe()
        return super().setUp()           
            
    def test_reicpe_title_raises_error_if_title_has_more_65_chars(self):
        self.recipe.title = "A" * 70
        
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
            
    @parameterized.expand([
        ("title", 65),
        ("description", 165),
        ("preparation_time_unit", 65),
        ("servings_unit", 65),
    ])             
    def test_recipe_fields_max_lenght(self, field, max_lenght):
        setattr(self.recipe, field, "A" * (max_lenght + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
            
    