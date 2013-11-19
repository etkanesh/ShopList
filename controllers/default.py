# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def index():       
    return dict()

def myRecipes():
    q = db.recipe
    grid = SQLFORM.grid((db.recipe.Email==auth.user.email ),
        searchable=True,
        fields=[db.recipe.title, db.recipe.Author, db.recipe.Email],
        csv=True, 
        details=False, create=False, editable=False, deletable=True,
        links=[
            dict(header=T('View'), 
                 body = lambda r: A('View', _class='btn', 
                                    _href=URL('default', 'viewRecipes',
                                              args=[r.id])),
            ),
            dict(header=T('Edit'), 
                 body = lambda r: A('Edit', _class='btn', 
                                    _href=URL('default', 'editRecipes',
                                              args=[r.id])),
            )
            ],
        )
    return dict(grid=grid)

def addRecipes():
    page = request.vars.page
    form = SQLFORM(db.recipe, fields=['title', 'Ingredients', 'Instructions'])
    if form.process().accepted:
        my_record = db(db.recipe.id > 0).select().last()
        redirect(URL('default', 'recipes'))
    return dict(form=form)    
    
def editRecipes():
    my_record = db.recipe(request.args(0))
    form = SQLFORM(db.recipe, record=my_record, fields=['title', 'Author', 'Ingredients', 'Instructions'])
    if form.process().accepted:
        redirect(URL('default', 'recipes'))
    return dict(form=form)    

def viewRecipes():
    my_record = db.recipe(request.args(0))
    form = SQLFORM(db.recipe, record=my_record, readonly=True,
                   fields=['title', 'Author', 'Ingredients', 'Instructions', 'Comments'])
    if form.process().accepted:
        redirect(URL('default', 'viewRecipes', args=[r.id]))
    return dict(form=form)
    
def recipes():
    q = db.recipe
    grid = SQLFORM.grid(q,
        searchable=True,
        fields=[db.recipe.title, db.recipe.Author, db.recipe.Email],
        csv=True, 
        details=False, create=False, editable=False, deletable=True,
        links=[
            dict(header=T('View'), 
                 body = lambda r: A('View', _class='btn', 
                                    _href=URL('default', 'viewRecipes', args=[r.id]
                                              )),
            ),
            ],
        )
    return dict(grid=grid)
    


def addIngredients():
    return dict()

def ingredients():
    return dict()

def shoplist():
    return dict()

def support():
    return dict()

def user():
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
