// LeetCode 3408 - Design Task Manager
// https://leetcode.com/problems/design-task-manager/

class TaskManager(tasks: List[List[Int]]) {
  private case class Item(pri: Int, taskId: Int, userId: Int)
  private val h = new java.util.PriorityQueue[Item]((a: Item, b: Item) => {
    if (a.pri != b.pri) java.lang.Integer.compare(b.pri, a.pri)
    else java.lang.Integer.compare(b.taskId, a.taskId)
  })
  private val pri = scala.collection.mutable.Map.empty[Int, Int]
  private val user = scala.collection.mutable.Map.empty[Int, Int]

  tasks.foreach { t => add(t(0), t(1), t(2)) }

  def add(userId: Int, taskId: Int, priority: Int): Unit = {
    pri(taskId) = priority
    user(taskId) = userId
    h.offer(Item(priority, taskId, userId))
  }

  def edit(taskId: Int, newPriority: Int): Unit = {
    pri(taskId) = newPriority
    h.offer(Item(newPriority, taskId, user(taskId)))
  }

  def rmv(taskId: Int): Unit = {
    pri.remove(taskId)
    user.remove(taskId)
  }

  def execTop(): Int = {
    while (!h.isEmpty) {
      val top = h.poll()
      val p = pri.get(top.taskId)
      if (p.isDefined && p.get == top.pri && user.get(top.taskId).contains(top.userId)) {
        pri.remove(top.taskId)
        val uid = user.remove(top.taskId).get
        return uid
      }
    }
    -1
  }
}
