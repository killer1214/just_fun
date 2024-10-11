import threading
from remind import Remind

class CicularTask(Remind):
    def __init__(self):
        super().__init__()
        self.base_name = "间断任务"
        self.__task_dict = dict()

    def catch_tasks(self):
        self.__task_dict = dict()
        task_section = self.catch_ini_info(self.ini, "间断任务")

        for task in task_section:
            self.__task_dict[task] = self.trans_time(task_section[task])
        
        # return self.__task_dict

    # def create_task(self, task_name, sleep_time):
    #     # time.sleep(sleep_time)
    #     return self.new_wins(task_name, f"{self.base_name}任务", sleep_time)

    def main_process(self):
        # 获取任务
        self.catch_tasks()
        # 解析任务并创建线程
        for key, value in self.__task_dict.items():
            thread = threading.Thread(target=self.circular_remind, args=(key, self.base_name, value))
            thread.start()


if __name__ == "__main__":
    a = CicularTask()
    a.main_process()