db = DAL('sqlite://storage.sqlite')

def get_name():
    if auth.user:
        return auth.user.first_name
    else:
        return 'None'

def get_email():
    if auth.user :
        return auth.user.email
    else:
        return 'None'
        
"""Database of ingredients:
    - Derive specific ingredients from one of the food groups"""
    
db.define_table('ingredients',
    Field('dairy'),
    Field('grains'),
    Field('vegetables'),
    Field('fruits'),
    Field('meat'),
    Field('fish'),
    Field('bread'),
    Field('cereals'),
    Field('fats'),
    Field('measurement'), 
    Field('ingredient_id'))

db.define_table('dairy',
    Field('measurement'), 
    Field('id'))

db.define_table('grains',
    Field('measurement'), 
    Field('id'))

db.define_table('vegetables',
    Field('measurement'), 
    Field('id'))

db.define_table('fruits',
    Field('measurement'), 
    Field('id'))

db.define_table('meat',
    Field('measurement'), 
    Field('id'))

db.define_table('fish',
    Field('measurement'), 
    Field('id'))

db.define_table('bread',
    Field('measurement'), 
    Field('id'))

db.define_table('cereals',
    Field('measurement'), 
    Field('id'))

db.define_table('fats',
    Field('measurement'), 
    Field('id'))


db.define_table('recipe',
	Field('title'),
	Field('Author', default=get_name()), 
	Field('Instructions','text')
	Field('Email', default=get_email()),
	Field('Ingredients', 'text'),
	Field('Comments', 'text'))

"""Database of Recipes:
    - Sort recipes based on country of origin
       - else, throw it in Other
    - Country list of food/recipes: http://www.foodbycountry.com/"""
       
db.define_table('recipe_choices',
    Field('Algeria'),
    Field('Argentina'),
    Field('Australia'),
    Field('Brazil'),
    Field('Cameroon'),
    Field('Canada'),
    Field('Chile'),
    Field('China'),
    Field('Cote_dIvoire'),
    Field('Cuba'),
    Field('Czech_Republic'),
    Field('Egypt'),
    Field('Ethiopia'),
    Field('France'),
    Field('Germany'),
    Field('Ghana'),
    Field('Guatemala'),
    Field('Haiti'),
    Field('Hungary'),
    Field('India'),
    Field('Indonesia'),
    Field('Iran'),
    Field('Iraq'),
    Field('Ireland'),
    Field('Islands_of_the_Pacific'),
    Field('Israel'),
    Field('Italy'),
    Field('Jamaica'),
    Field('Japan'),
    Field('Kazakhstan'),
    Field('Kenya'),
    Field('Korea'),
    Field('Lebanon'),
    Field('Liberia'),
    Field('Mexico'),
    Field('Morocco'),
    Field('Mozambique'),
    Field('Nigeria'),
    Field('Pakistan'),
    Field('Peru'),
    Field('Philippines'),
    Field('Poland'),
    Field('Russia'),
    Field('Saudi_Arabia'),
    Field('Slovenia'),
    Field('South_Africa'),
    Field('Spain'),
    Field('Sweden'),
    Field('Tanzania'),
    Field('Thailand'),
    Field('Turkey'),
    Field('Ukraine'),
    Field('United_Kingdom'),
    Field('United_States'),
    Field('Vietnam'),
    Field('Zimbabwe'),
    Field('Other'),
    Field('recipe_id'))	

"""Mini database to link recipes and ingredients"""
db.define_table('RecipeNeeds',
    Field('recipe_id'),
    Field('ingredient_id'))

"""Database to combine everything into becoming the user's final shoplist """
db.define_table('ShopList',
	Field('created_on', 'date', default=request.now),
	Field('user_email', default=get_email()),
	Field('author', default=get_name()),
	Field('recipes', 'list:string'),
	Field('finished','boolean',default=False)) 
