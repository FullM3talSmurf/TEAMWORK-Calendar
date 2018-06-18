from src.common.Database import Database
from src.Tasks.TaskConstants import COLLECTION


class Task(object):
    def __init__(self, task_id, start_date, due_date, description, content, project_name, project_id, todo_list_name,
                 creator_lastname, creator_firstname, estimated_minutes, has_dependencies, priority, progress,
                 last_changed_on):
        self.task_id = task_id
        self.start_date = start_date
        self.due_date = due_date
        self.description = description
        self.content = content
        self.project_name = project_name
        self.project_id = project_id
        self.todo_list_name = todo_list_name
        self.creator_lastname = creator_lastname
        self.creator_firstname = creator_firstname
        self.estimated_minutes = estimated_minutes
        self.has_dependencies = has_dependencies
        self.priority = priority
        self.progress = progress
        self.last_changed_on = last_changed_on

    def json(self):
        return {
            "_id": self.task_id,
            "start_date": self.start_date,
            "due_date": self.due_date,
            "description": self.description,
            "content": self.content,
            "project_name": self.project_name,
            "project_id": self.project_id,
            "todo_list_name": self.todo_list_name,
            "creator_lastname": self.creator_lastname,
            "creator_firstname": self.creator_firstname,
            "estimated_minutes": self.estimated_minutes,
            "has_dependencies": self.has_dependencies,
            "priority": self.priority,
            "progress": self.progress,
            "last_changed_on": self.last_changed_on
            }

    def save_to_db(self):
        Database.insert(COLLECTION, self.json())


