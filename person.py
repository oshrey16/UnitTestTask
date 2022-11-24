class Person:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        if(age>0):
            self.age = age
        else:
            self.age= 0
    def __str__(self):
        return ("ID: {} ,name: {} , age: {}").format(self.id, self.name,self.age)
    # bitrhday -> age+1
    def birthday(self):
        self.age += 1
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.id == other.id and self.name == other.name and self.age == other.age

class Worker:
    def __init__(self,id,name,age,salary):
        self.person = Person(id,name,age)
        self.salary = salary
        self.worker_id = None
    def __str__(self):
        return ("Worker- {} ,Salary: {} , WorkerID: {}").format(self.person,self.salary,self.worker_id)
    def __repr__(self):
        return str(self)
    def __eq__(self, other):
        if isinstance(other, Worker):
            return self.person == other.person and self.salary == other.salary and self.worker_id == other.worker_id
        return False
    
    def set_worker_id(self,worker_id):
        self.worker_id = worker_id
    def remove_worker_id(self):
        self.worker_id = None

class Factory:
    def __init__(self):
        self.workers = []
        self.total_salary = 0
    def __str__(self):
        s = ""
        s += "Total salary: {}\n".format(self.total_salary)
        for worker in self.workers:
            s += ("{}\n").format(worker)
        return (s)
    
    def add_worker(self, worker1:Worker):
        id_worker = len(self.workers)
        self.workers.sort(key=lambda x: x.worker_id)
        for i in range(len(self.workers)):
            if i != self.workers[i].worker_id:
                id_worker = i
                break
        worker1.set_worker_id(id_worker)
        self.workers.append(worker1)
        self.workers.sort(key=lambda x: x.worker_id)
        self.total_salary += worker1.salary
        print("Worker ID: {}".format(worker1.worker_id))
    
    def remove_worker(self,worker_id):
        self.total_salary -= self.workers[worker_id].salary
        self.workers.pop(worker_id)

f = Factory()
f.add_worker(Worker(1,"2",20,3000))
f.add_worker(Worker(2,"2222",20,3000))
f.add_worker(Worker(1,"333",20,3000))