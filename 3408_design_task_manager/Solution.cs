// LeetCode 3408 - Design Task Manager
// https://leetcode.com/problems/design-task-manager/

using System.Collections.Generic;

public class TaskManager {
    readonly PriorityQueue<(int pri, int taskId, int userId), (int, int)> h = new();
    readonly Dictionary<int, int> pri = new();
    readonly Dictionary<int, int> user = new();

    public TaskManager(IList<IList<int>> tasks) {
        foreach (var t in tasks) Add(t[0], t[1], t[2]);
    }

    public void Add(int userId, int taskId, int priority) {
        pri[taskId] = priority;
        user[taskId] = userId;
        h.Enqueue((priority, taskId, userId), (-priority, -taskId));
    }

    public void Edit(int taskId, int newPriority) {
        pri[taskId] = newPriority;
        h.Enqueue((newPriority, taskId, user[taskId]), (-newPriority, -taskId));
    }

    public void Rmv(int taskId) {
        pri.Remove(taskId);
        user.Remove(taskId);
    }

    public int ExecTop() {
        while (h.Count > 0) {
            var top = h.Dequeue();
            if (pri.TryGetValue(top.taskId, out int p) && p == top.pri && user[top.taskId] == top.userId) {
                pri.Remove(top.taskId);
                int uid = user[top.taskId];
                user.Remove(top.taskId);
                return uid;
            }
        }
        return -1;
    }
}
