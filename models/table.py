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
        
db.define_table('Recipe',
	Field('title'),
	Field('picture','upload',default=''),
	Field('rating','int'),
	Field('Ingredients','text')
	Field('get_ingredients','boolean',default=False))
	
db.define_table('ShopList',
	Field('created_on', 'date', default=request.now),
	Field('user_email', default=get_email()),
	Field('author', default=get_name()),
	Field('list', 'text'),
	Field('finished','boolean',default=False)) 