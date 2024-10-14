import time
import easygui
from common_ini import Base

class Remind(Base):
    def __init__(self):
        super().__init__()
        # 按钮默认字段
        self.button_str = ["继续提醒", "结束"]
        
    def __create_button(self, task, wins):
        """创建buttonbox

        :param task: 任务名称
        :type task: str
        :param wins: 窗口名称
        :type wins: str
        :return: 窗口
        :rtype: buttonbox
        """
        return easygui.buttonbox(task, wins, self.button_str)

    def circular_remind(self, task_name, window_name, sleep_time):
        """间隔一定时间提醒的任务窗口

        :param task_name: 任务名称
        :type task_name: str
        :param window_name: 窗口名称
        :type window_name: str
        :param sleep_time: 间隔时间
        :type sleep_time: int(second)
        """
        button = self.__create_button(task_name, window_name)
        if button == self.button_str[0]:
            print(f"{task_name} 进入后台执行...")
            time.sleep(sleep_time)
            # button = self.__create_button(window_name, task_name)
            self.circular_remind(task_name, window_name, sleep_time)
        else:
            print(f"{task_name} 执行结束...")
            return