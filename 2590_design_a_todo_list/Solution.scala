// LeetCode 2590 - Design a Todo List
// https://leetcode.com/problems/design-a-todo-list/

class TodoList() {
  private class Task {
    var id: Int = 0
    var description: String = ""
    var dueDate: Int = 0
    val tags = scala.collection.mutable.Set.empty[String]
    var done: Boolean = false
    var userId: Int = 0
  }

  private var nextID = 1
  private val tasks = scala.collection.mutable.Map.empty[Int, Task]
  private val users = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]

  def addTask(userId: Int, taskDescription: String, dueDate: Int, tags: List[String]): Int = {
    val id = nextID
    nextID += 1
    val tk = new Task
    tk.id = id
    tk.description = taskDescription
    tk.dueDate = dueDate
    tk.userId = userId
    tags.foreach(tk.tags += _)
    tasks(id) = tk
    users.getOrElseUpdate(userId, scala.collection.mutable.ArrayBuffer.empty[Int]) += id
    id
  }

  def getAllTasks(userId: Int): List[String] = {
    if (!users.contains(userId)) return List.empty
    val ids = users(userId).toList.sortBy(id => tasks(id).dueDate)
    ids.flatMap { id =>
      if (!tasks(id).done) Some(tasks(id).description) else None
    }
  }

  def getTasksForTag(userId: Int, tag: String): List[String] = {
    if (!users.contains(userId)) return List.empty
    val ids = users(userId).toList.sortBy(id => tasks(id).dueDate)
    ids.flatMap { id =>
      val tk = tasks(id)
      if (!tk.done && tk.tags.contains(tag)) Some(tk.description) else None
    }
  }

  def completeTask(userId: Int, taskId: Int): Unit = {
    tasks.get(taskId) match {
      case Some(tk) if tk.userId == userId && !tk.done => tk.done = true
      case _ =>
    }
  }
}
