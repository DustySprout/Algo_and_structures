import unittest

from avl_priority_queue import PriorityJobQueue


class TaskNode:
    def __init__(self, task_name, task_priority):
        self.left_child = None
        self.right_child = None
        self.task_name = task_name
        self.task_priority = task_priority


class TestPriorityJobQueue(unittest.TestCase):
    def test_add_job(self):
        job_queue = PriorityJobQueue()
        job_queue.add_job("feed a cat", 3)
        job_queue.add_job("to do a CS course", 7)
        job_queue.add_job("to do a homework", 2)
        job_queue.add_job("Go to the chess tournament", 4)

        self.assertEqual(job_queue.head.task_name, "feed a cat")
        self.assertEqual(job_queue.head.left_child.task_name, "to do a homework")
        self.assertEqual(job_queue.head.right_child.task_name, "to do a CS course")
        self.assertEqual(job_queue.head.right_child.left_child.task_name, "Go to the chess tournament")

    def test_get_priority_task(self):
        job_queue = PriorityJobQueue()
        job_queue.add_job("feed a cat", 3)
        job_queue.add_job("to do a CS course", 7)
        job_queue.add_job("to do a homework", 2)
        job_queue.add_job("Go to the chess tournament", 4)

        highest_priority_task = job_queue.get_priority_task()
        self.assertEqual(highest_priority_task, "to do a CS course")

    def test_list_tasks(self):
        job_queue = PriorityJobQueue()
        job_queue.add_job("feed a cat", 3)
        job_queue.add_job("to do a CS course", 7)
        job_queue.add_job("to do a homework", 2)
        job_queue.add_job("Go to the chess tournament", 4)

        tasks = job_queue.list_tasks()
        expected_tasks = [
            ("to do a homework", 2),
            ("feed a cat", 3),
            ("Go to the chess tournament", 4),
            ("to do a CS course", 7)
        ]
        self.assertEqual(tasks, expected_tasks)


if __name__ == "__main__":
    unittest.main()
