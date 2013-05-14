import unittest
from flaskext.jsonify import jsonify
from datetime import datetime
from json import JSONEncoder


class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        else:
            return super(CustomEncoder, self).default(obj)


class JsonifyTests(unittest.TestCase):

    def setUp(self):
        self.easy_object = {
            'name': 'Chris',
            'age': 23,
            'friend': {
                'name': 'Alex'
            },
            'is_male': True
        }

        self.hard_object = {
            'name': 'Chris',
            'age': 23,
            'friend': {
                'name': 'Alex'
            },
            'is_male': True,
            'date': datetime.now()
        }

    # ----- Test Cases ----------------------------------------------

    # Serializing an object without a custom class that should
    # be serializable with the default class should not raise an exception

    @jsonify
    def easy_obj_no_custom_class(self):
        return self.easy_object

    def test_easy_obj_no_decorator(self):
        self.easy_obj_no_custom_class()

    # Serializing an object with a custom class that should
    # be serializable with the default class should also not raise an exception

    @jsonify(cls=CustomEncoder)
    def easy_obj_with_custom_class(self):
        return self.easy_object

    def test_easy_obj_with_decorator(self):
        self.easy_obj_with_custom_class()

    # Serializing an object without a custom class that is not
    # serializable with the default class should raise an exception

    @jsonify
    def hard_obj_no_custom_class(self):
        return self.hard_object

    def test_hard_obj_no_decorator(self):
        try:
            self.hard_obj_no_custom_class()
            self.fail("Uh oh, this case should fail and it doesn't")
        except:
            pass

    # Serializing an object with a custom class that is not
    # serializable with the default class should succeed

    @jsonify(cls=CustomEncoder)
    def hard_obj_with_custom_class(self):
        return self.hard_object

    def test_hard_obj_with_decorator(self):
        self.hard_obj_with_custom_class()

if __name__ == '__main__':
    unittest.main()