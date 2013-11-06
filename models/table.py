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
        

db.define_table('Ingredients',
	Field('name'),
	Field('measurement'))	
        
db.define_table('Recipe',
	Field('title'),
	Field('Author', default=get_name()), 
	Field('Instructions','text'))
	
db.define_table('RecipeNeeds',
	Field('recipe_id')
	Field('ingredient_id'))
	
	
db.define_table('ShopList',
	Field('created_on', 'date', default=request.now),
	Field('user_email', default=get_email()),
	Field('author', default=get_name()),
	Field('recipes', 'list:string'),
	Field('finished','boolean',default=False)) 