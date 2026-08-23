// LeetCode 3408 - Design Task Manager
// https://leetcode.com/problems/design-task-manager/

#include <queue>
#include <unordered_map>
#include <vector>

class TaskManager {
    struct Item {
        int pri, taskId, userId;
        bool operator<(const Item& o) const {
            if (pri != o.pri) return pri < o.pri;
            return taskId < o.taskId;
        }
    };
    std::priority_queue<Item> h;
    std::unordered_map<int, int> pri;
    std::unordered_map<int, int> user;

public:
    TaskManager(std::vector<std::vector<int>>& tasks) {
        for (auto& t : tasks) add(t[0], t[1], t[2]);
    }

    void add(int userId, int taskId, int priority) {
        pri[taskId] = priority;
        user[taskId] = userId;
        h.push({priority, taskId, userId});
    }

    void edit(int taskId, int newPriority) {
        pri[taskId] = newPriority;
        h.push({newPriority, taskId, user[taskId]});
    }

    void rmv(int taskId) {
        pri.erase(taskId);
        user.erase(taskId);
    }

    int execTop() {
        while (!h.empty()) {
            Item top = h.top();
            h.pop();
            auto it = pri.find(top.taskId);
            if (it != pri.end() && it->second == top.pri && user[top.taskId] == top.userId) {
                pri.erase(top.taskId);
                int uid = user[top.taskId];
                user.erase(top.taskId);
                return uid;
            }
        }
        return -1;
    }
};
