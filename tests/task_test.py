from unittest import TestCase, main
import requests


class TaskTest(TestCase):
    def test_get_returns_200(self):
        r = requests.get('http://localhost:5000/todo/api/v1.0/task/1')
        self.assertEqual(r.status_code, requests.codes.ok)

    def test_get_returns_abort_message_404(self):
        r = requests.get('http://localhost:5000/todo/api/v1.0/task/0')
        self.assertEqual(r.status_code, requests.codes.not_found)
        self.assertEqual(r.json()["content"], "Task 0 doesn't exist")

    def test_delete_returns_204(self):
        r = requests.delete('http://localhost:5000/todo/api/v1.0/task/2')
        self.assertEqual(r.status_code, requests.codes.no_content)

    def test_delete_returns_abort_message_404(self):
        r = requests.delete('http://localhost:5000/todo/api/v1.0/task/0')
        self.assertEqual(r.status_code, requests.codes.not_found)
        self.assertEqual(r.json()["content"], "Task 0 doesn't exist")

    def test_update_returns_200(self):
        data = {'completed': True}
        r = requests.patch('http://localhost:5000/todo/api/v1.0/task/1', data=data)
        self.assertEqual(r.status_code, requests.codes.ok)
        self.assertTrue(r.json()['completed'])


if __name__ == '__main__':
    main()
