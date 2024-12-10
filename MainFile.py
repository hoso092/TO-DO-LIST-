
class Task :
    def __init__(self, TaskDescription, Due_Date ,Priority) :
        self.TaskDescription = TaskDescription
        self.Due_Date = Due_Date
        self.Priority = Priority
        self.tasklist=[]

    def file_handling(self,data):
        with open('Tasks' ,'a') as fileobject:
            for ListItem in data :
                fileobject.write(str(ListItem)+':')
            fileobject.write('\n')
        return


    def addTask(self):
        #convert the input into list
        self.tasklist.append(self.TaskDescription)
        self.tasklist.append(self.Due_Date)
        self.tasklist.append(self.Priority)
        self.file_handling(self.tasklist)
        print("task added successfully")
        return
    def listAll(self):
        with open('Tasks' ,'r') as fileobject:
            data=fileobject.readlines()
            for line in data:
                print(line, end='')
            return

    def deleteTask(self):
        choice='task 3'#input("Please Enter Task Name : ")
        with open('Tasks' ,'r') as fileobject:
            data=fileobject.readlines()
            for line in data:
                item=line.split(':',3)
                if item[0] == choice:
                    data.remove(line)
                    Task.file_handling(self,data)
                    print("task deleted successfully")
                    break
            print("task Not Found")
    # def UpdateTask(self):
    #     choice='task 9'#input("Please Enter Task Name : ")
    #     with open('Tasks' ,'r') as fileobject:
    #         data=fileobject.readlines()
    #         for line in data:
    #             item=line.split(':',3)
    #             if item[0] == choice:
    #                 data.remove(line)
    #                 ToDoList.file_handling(self,data)
    #                 break






for num in range(1,11):
    task1 = Task(f'task {num}',num,num)
    Task.addTask(task1)


Task.listAll(task1)
# task1 = Task("task 3",6,6)
# Task.deleteTask(task1)










