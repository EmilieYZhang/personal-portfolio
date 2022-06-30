import unittest
from peewee import *
from app import TimelinePost

# To run test: python -m unittest -v tests.test_db

MODELS = [TimelinePost]

# use an in-memory SQLite for tests
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # bind model classes to test db. Don't need to recursively
        # bind dependencies since we have a complete list of all models
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # not strictly necessary since SQLite in-memory databases live
        # only for duration of connection and connection will be closed
        # in the next step, but still good practice!
        test_db.drop_tables(MODELS)

        # close connection to database
        test_db.close()

    # test that POST results in the expected id
    def test_timeline_post(self):
        # create two timeline posts
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1 # check that first post has id of 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2 # check that first post has id of 2

    # test that GET results in id of previously created posts
    def test_timeline_get(self):
        # create two timeline posts
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')

        posts = TimelinePost.select() # get all posts
        id_count = 1
        for post in posts:
            assert post.id == id_count # check that post id is correct
            id_count += 1 # increases by one each time