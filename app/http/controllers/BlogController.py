""" A BlogController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Blog import Blog

class BlogController(Controller):
    """Class Docstring Description
    """
    
    def __init__(self, request: Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", BlogController)
        """
        id = self.request.param("id")
        return Blog.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", BlogController)
        """
        return Blog.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", BlogController)
        """
        title = self.request.input("title")
        body = self.request.input("body")
        post = Blog.create({"title": title, "body": body})
        return post

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", BlogController)
        """
        title = self.request.input("title")
        body = self.request.input("body")
        id = self.request.param("id")
        Blog.where("id", id).update({"title": title, "body": body})
        return Blog.where("id", id).get()

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", BlogController)
        """
        id = self.request.param("id")
        post = Blog.where("id", id).get()
        Blog.where("id", id).delete()
        return post