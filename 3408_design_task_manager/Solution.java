// LeetCode 3408 - Design Task Manager
// https://leetcode.com/problems/design-task-manager/

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

class TaskManager {
    private static class Item {
        int pri, taskId, userId;
        Item(int pri, int taskId, int userId) {
            this.pri = pri;
            this.taskId = taskId;
            this.userId = userId;
        }
    }

    private final PriorityQueue<Item> h = new PriorityQueue<>((a, b) -> {
        if (a.pri != b.pri) return Integer.compare(b.pri, a.pri);
        return Integer.compare(b.taskId, a.taskId);
    });
    private final Map<Integer, Integer> pri = new HashMap<>();
    private final Map<Integer, Integer> user = new HashMap<>();

    public TaskManager(List<List<Integer>> tasks) {
        for (List<Integer> t : tasks) add(t.get(0), t.get(1), t.get(2));
    }

    public void add(int userId, int taskId, int priority) {
        pri.put(taskId, priority);
        user.put(taskId, userId);
        h.offer(new Item(priority, taskId, userId));
    }

    public void edit(int taskId, int newPriority) {
        pri.put(taskId, newPriority);
        h.offer(new Item(newPriority, taskId, user.get(taskId)));
    }

    public void rmv(int taskId) {
        pri.remove(taskId);
        user.remove(taskId);
    }

    public int execTop() {
        while (!h.isEmpty()) {
            Item top = h.poll();
            Integer p = pri.get(top.taskId);
            if (p != null && p == top.pri && user.get(top.taskId) == top.userId) {
                pri.remove(top.taskId);
                int uid = user.remove(top.taskId);
                return uid;
            }
        }
        return -1;
    }
}
