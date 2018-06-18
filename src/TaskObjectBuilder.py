import urllib3
from src.common import Utils
from src.Tasks.Task import Task
from src import TaskListHolder
from src.common.Database import Database

# this will eventually go into app
Database.initialize()
http = urllib3.PoolManager()

company = "wltc"
key = "twp_VJ8lmPZG8cdnAmW1UEYPqbHPzldj"
action = "tasks.json"

url = "https://{0}.teamwork.com/{1}".format(company, action)
headers = urllib3.util.make_headers(basic_auth=key + ":xxx")
request = http.request('GET', url, headers=headers)

response = request.status
data = request.data

dic = Utils.bytes_to_json(data)

tasks = dic["todo-items"]

for task in tasks:
    _id = task["id"]
    start_date = task["start-date"]
    due_date = task["due-date"]
    description = task["description"]
    content = task["content"]
    project_name = task["project-name"]
    project_id = task["project-id"]
    todo_list_name = task["todo-list-name"]
    creator_lastname = task["creator-lastname"]
    creator_firstname = task["creator-firstname"]
    estimated_minutes = task["estimated-minutes"]
    has_dependencies = task["has-dependencies"]
    priority = task["priority"]
    progress = task["progress"]
    last_changed_on = task["last-changed-on"]

    tsk = Task(_id, start_date, due_date, description, content, project_name, project_id, todo_list_name,
               creator_lastname, creator_firstname, estimated_minutes, has_dependencies, priority, progress,
               last_changed_on)

    TaskListHolder.append_task(tsk)
    # this is to be sent to a to the TaskListHolder
    # that class is to hold the sorting methods and contain an append_task() method to add a task to an ArrayList<Task>
    # append needs to be a static method.

    # TaskListHolder.append_task(tsk)

