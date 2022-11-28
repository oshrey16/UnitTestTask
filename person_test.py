import unittest
from person import Person
from person import Worker
from person import Factory

class TestPerson(unittest.TestCase):
    x =0
    person = Person(0,"person1",30)
    def test_0_init(self):
        with self.subTest("Name ID"):
            self.assertEqual(self.person.id,0)
        with self.subTest("Name Test"):
            self.assertEqual(self.person.name,"person1")
        with self.subTest("Age Test"):
            self.assertEqual(self.person.age,30)
    def test_1_age_negative(self):
        person1 = Person(0,"person1",-5)
        self.assertEqual(person1.age,0)
    def test_2_birthday(self):
        self.person.birthday()  # !void fucntion! but I can check if the age is been changed
        self.assertEqual(self.person.age,31,"should be 31")

class TestWorker(unittest.TestCase):
    worker = Worker(0,"person1",20,8000)
    def test_salary(self):
        self.assertEqual(self.worker.salary,8000)

class TestFactory(unittest.TestCase):
    factory = Factory()

    def test_0_init_factory(self):
        with self.subTest("Factory workers not empty"):
            self.assertFalse(self.factory.workers)  #Empty lists evaluate to False
        with self.subTest("Factory total salary not 0"):
            self.assertEqual(self.factory.total_salary,0)
        
    def test_1_add_workers(self):
        print("Start add_workers test")
        print("Before:\n{}".format(self.factory))
        for i in range(4):
            name = "Worker" + str(i)
            worker = Worker(i,name,i,i*1000)
            self.factory.add_worker(worker)
        with self.subTest("Factory workers array not same"):
            for i in range(4):
                name = "Worker" + str(i)
                worker = Worker(i,name,i,i*1000)
                worker.set_worker_id(i)
                with self.subTest("worker"):
                    self.assertEqual(worker,self.factory.workers[i])
        with self.subTest("total_salary should be 6000"):
            self.assertEqual(self.factory.total_salary,6000)
        print("After:\n{}".format(self.factory))
    
    # Remove worker1 with salary 1000- workerID:1
    def test_2_delete_worker(self):
        print("Start delete_worker test")
        print("Before:\n{}".format(self.factory))
        deleted_worker = self.factory.workers[1]
        self.factory.remove_worker(1)
        with self.subTest("Factory workers array not same"):
            for i in range(4):
                if (i == 1):
                    pass
                else:
                    name = "Worker" + str(i)
                    worker = Worker(i,name,i,i*1000)
                    worker.set_worker_id(i)
                    with self.subTest("worker"):
                        self.assertIn(worker,self.factory.workers)
        with self.subTest("worker_deleted"):
            self.assertNotIn(deleted_worker,self.factory.workers)
        with self.subTest("total_salary not 5000"):
            self.assertEqual(self.factory.total_salary,5000)
        print("After:\n{}".format(self.factory))
    
    def test_3_add_worker_after_delete_worker1(self):
        print("Start add_worker_after_delete_middle test")
        print("Before:\n{}".format(self.factory))
        worker = Worker(123,"testPerson",40,8000)
        self.factory.add_worker(worker)
        with self.subTest():
            self.assertIn(worker,self.factory.workers)
        
        with self.subTest("total_salary not 13000"):
            self.assertEqual(self.factory.total_salary,13000)
        print("After:\n{}".format(self.factory))

if __name__ == '__main__':
    unittest.main()