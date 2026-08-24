// LeetCode 2590 - Design a Todo List
// https://leetcode.com/problems/design-a-todo-list/

class TodoList {
    private class Task {
        let id: Int
        let description: String
        let dueDate: Int
        var tags: Set<String>
        var done = false
        let userId: Int
        init(_ id: Int, _ description: String, _ dueDate: Int, _ tags: [String], _ userId: Int) {
            self.id = id
            self.description = description
            self.dueDate = dueDate
            self.tags = Set(tags)
            self.userId = userId
        }
    }

    private var nextID = 1
    private var tasks = [Int: Task]()
    private var users = [Int: [Int]]()

    init() {}

    func addTask(_ userId: Int, _ taskDescription: String, _ dueDate: Int, _ tags: [String]) -> Int {
        let id = nextID
        nextID += 1
        tasks[id] = Task(id, taskDescription, dueDate, tags, userId)
        users[userId, default: []].append(id)
        return id
    }

    func getAllTasks(_ userId: Int) -> [String] {
        guard var ids = users[userId] else { return [] }
        ids.sort { tasks[$0]!.dueDate < tasks[$1]!.dueDate }
        return ids.compactMap { id in
            let tk = tasks[id]!
            return tk.done ? nil : tk.description
        }
    }

    func getTasksForTag(_ userId: Int, _ tag: String) -> [String] {
        guard var ids = users[userId] else { return [] }
        ids.sort { tasks[$0]!.dueDate < tasks[$1]!.dueDate }
        return ids.compactMap { id in
            let tk = tasks[id]!
            return (!tk.done && tk.tags.contains(tag)) ? tk.description : nil
        }
    }

    func completeTask(_ userId: Int, _ taskId: Int) {
        guard let tk = tasks[taskId], tk.userId == userId, !tk.done else { return }
        tk.done = true
    }
}
