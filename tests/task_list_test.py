from unittest import TestCase, main
import requests


class TaskListTest(TestCase):
    def test_get_returns_json_200(self):
        r = requests.get('http://localhost:5000/api/v1/tasks')
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertEqual(r.status_code, requests.codes.ok)

    def test_create_returns_json_201(self):
        r = requests.post('http://localhost:5000/api/v1/tasks', data={'content': 'new task'})
        creation_date = r.json()['creation_date']
        id_ = r.json()['id']

        self.assertEqual(r.status_code, requests.codes.created)
        self.assertEqual(r.json(), {'content': 'new task',
                                    'completed': False,
                                    'id': id_,
                                    'creation_date': creation_date,
                                    'uri': '/api/v1/task/' + str(id_)})


if __name__ == '__main__':
    main()
