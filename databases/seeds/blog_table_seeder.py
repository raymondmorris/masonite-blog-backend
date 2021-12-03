"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog

class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({"title": "Post1", "body": "Lorem ipsum dolor sit amet. In ipsa repellat qui totam tempora et quae consequatur aut sint quas ex quibusdam fuga ut placeat distinctio At voluptas dolore. Sed iusto facere in dolorum quia ex numquam porro non laboriosam repellendus ex odit saepe aut sequi debitis. Eum optio nihil sed reiciendis doloremque eum dolores deserunt quo quisquam dicta cum modi voluptatem rem recusandae rerum ut laboriosam quia."})
        Blog.create({"title": "Post2", "body": "Lorem ipsum dolor sit amet. In ipsa repellat qui totam tempora et quae consequatur aut sint quas ex quibusdam fuga ut placeat distinctio At voluptas dolore. Sed iusto facere in dolorum quia ex numquam porro non laboriosam repellendus ex odit saepe aut sequi debitis. Eum optio nihil sed reiciendis doloremque eum dolores deserunt quo quisquam dicta cum modi voluptatem rem recusandae rerum ut laboriosam quia."})
        Blog.create({"title": "Post3", "body": "Lorem ipsum dolor sit amet. In ipsa repellat qui totam tempora et quae consequatur aut sint quas ex quibusdam fuga ut placeat distinctio At voluptas dolore. Sed iusto facere in dolorum quia ex numquam porro non laboriosam repellendus ex odit saepe aut sequi debitis. Eum optio nihil sed reiciendis doloremque eum dolores deserunt quo quisquam dicta cum modi voluptatem rem recusandae rerum ut laboriosam quia."})
        Blog.create({"title": "Post4", "body": "Lorem ipsum dolor sit amet. In ipsa repellat qui totam tempora et quae consequatur aut sint quas ex quibusdam fuga ut placeat distinctio At voluptas dolore. Sed iusto facere in dolorum quia ex numquam porro non laboriosam repellendus ex odit saepe aut sequi debitis. Eum optio nihil sed reiciendis doloremque eum dolores deserunt quo quisquam dicta cum modi voluptatem rem recusandae rerum ut laboriosam quia."})