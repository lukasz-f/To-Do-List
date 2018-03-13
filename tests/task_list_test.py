from unittest import TestCase, main
import requests


class TaskListTest(TestCase):
    def test_get_returns_json_200(self):
        r = requests.get('http://localhost:5000/api/tasks')
        self.assertEqual(r.headers['Content-Type'], 'application/json')
        self.assertTrue(r.status_code == requests.codes.ok)

    def test_post_status(self):
        r = requests.post('http://localhost:5000/api/tasks', data={'content': 'zadanie'})
        self.assertTrue(r.status_code == requests.codes.created)

    def test_post_increases_task_number(self):
        r = requests.get('http://localhost:5000/api/tasks')
        task_number = len(r.json())

        requests.post('http://localhost:5000/api/tasks', data={'content': 'zadanie 2'})

        r = requests.get('http://localhost:5000/api/tasks')
        new_task_number = len(r.json())
        self.assertGreater(new_task_number, task_number)


if __name__ == '__main__':
    main()
