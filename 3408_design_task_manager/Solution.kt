// LeetCode 3408 - Design Task Manager
// https://leetcode.com/problems/design-task-manager/

class TaskManager(tasks: List<List<Int>>) {
    private class Item(val pri: Int, val taskId: Int, val userId: Int)

    private val h = PriorityQueue<Item> { a, b ->
        if (a.pri != b.pri) b.pri.compareTo(a.pri) else b.taskId.compareTo(a.taskId)
    }
    private val pri = HashMap<Int, Int>()
    private val user = HashMap<Int, Int>()

    init {
        for (t in tasks) add(t[0], t[1], t[2])
    }

    fun add(userId: Int, taskId: Int, priority: Int) {
        pri[taskId] = priority
        user[taskId] = userId
        h.offer(Item(priority, taskId, userId))
    }

    fun edit(taskId: Int, newPriority: Int) {
        pri[taskId] = newPriority
        h.offer(Item(newPriority, taskId, user[taskId]!!))
    }

    fun rmv(taskId: Int) {
        pri.remove(taskId)
        user.remove(taskId)
    }

    fun execTop(): Int {
        while (!h.isEmpty()) {
            val top = h.poll()
            val p = pri[top.taskId]
            if (p != null && p == top.pri && user[top.taskId] == top.userId) {
                pri.remove(top.taskId)
                return user.remove(top.taskId)!!
            }
        }
        return -1
    }
}
