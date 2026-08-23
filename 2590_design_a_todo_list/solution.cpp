// LeetCode 2590 - Design a Todo List
// https://leetcode.com/problems/design-a-todo-list/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class TodoList {
    struct Task {
        int id = 0;
        std::string description;
        int dueDate = 0;
        std::unordered_set<std::string> tags;
        bool done = false;
        int userId = 0;
    };
    int nextID = 1;
    std::unordered_map<int, Task> tasks;
    std::unordered_map<int, std::vector<int>> users;

public:
    TodoList() {}

    int addTask(int userId, std::string taskDescription, int dueDate, std::vector<std::string> tags) {
        int id = nextID++;
        Task tk;
        tk.id = id;
        tk.description = taskDescription;
        tk.dueDate = dueDate;
        tk.userId = userId;
        for (auto& x : tags) tk.tags.insert(x);
        tasks[id] = std::move(tk);
        users[userId].push_back(id);
        return id;
    }

    std::vector<std::string> getAllTasks(int userId) {
        std::vector<int> ids = users[userId];
        std::sort(ids.begin(), ids.end(), [&](int a, int b) {
            return tasks[a].dueDate < tasks[b].dueDate;
        });
        std::vector<std::string> ans;
        for (int id : ids) {
            if (!tasks[id].done) ans.push_back(tasks[id].description);
        }
        return ans;
    }

    std::vector<std::string> getTasksForTag(int userId, std::string tag) {
        std::vector<int> ids = users[userId];
        std::sort(ids.begin(), ids.end(), [&](int a, int b) {
            return tasks[a].dueDate < tasks[b].dueDate;
        });
        std::vector<std::string> ans;
        for (int id : ids) {
            auto& tk = tasks[id];
            if (!tk.done && tk.tags.count(tag)) ans.push_back(tk.description);
        }
        return ans;
    }

    void completeTask(int userId, int taskId) {
        auto it = tasks.find(taskId);
        if (it == tasks.end() || it->second.userId != userId || it->second.done) return;
        it->second.done = true;
    }
};
