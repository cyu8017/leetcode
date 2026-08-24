// LeetCode 2590 - Design a Todo List
// https://leetcode.com/problems/design-a-todo-list/

class TodoList {
    private class Task {
        var id = 0
        var description = ""
        var dueDate = 0
        val tags = HashSet<String>()
        var done = false
        var userId = 0
    }

    private var nextID = 1
    private val tasks = HashMap<Int, Task>()
    private val users = HashMap<Int, MutableList<Int>>()

    fun addTask(userId: Int, taskDescription: String, dueDate: Int, tags: List<String>): Int {
        val id = nextID
        nextID += 1
        val tk = Task()
        tk.id = id
        tk.description = taskDescription
        tk.dueDate = dueDate
        tk.userId = userId
        tk.tags.addAll(tags)
        tasks[id] = tk
        users.getOrPut(userId) { ArrayList() }.add(id)
        return id
    }

    fun getAllTasks(userId: Int): List<String> {
        val ids = users[userId] ?: return ArrayList()
        val sorted = ids.sortedBy { tasks[it]!!.dueDate }
        val ans = ArrayList<String>()
        for (id in sorted) {
            val tk = tasks[id]!!
            if (!tk.done) ans.add(tk.description)
        }
        return ans
    }

    fun getTasksForTag(userId: Int, tag: String): List<String> {
        val ids = users[userId] ?: return ArrayList()
        val sorted = ids.sortedBy { tasks[it]!!.dueDate }
        val ans = ArrayList<String>()
        for (id in sorted) {
            val tk = tasks[id]!!
            if (!tk.done && tag in tk.tags) ans.add(tk.description)
        }
        return ans
    }

    fun completeTask(userId: Int, taskId: Int) {
        val tk = tasks[taskId] ?: return
        if (tk.userId != userId || tk.done) return
        tk.done = true
    }
}
