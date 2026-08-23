// LeetCode 2590 - Design a Todo List
// https://leetcode.com/problems/design-a-todo-list/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class TodoList {
    private static class Task {
        int id;
        String description;
        int dueDate;
        Set<String> tags = new HashSet<>();
        boolean done;
        int userId;
    }

    private int nextID = 1;
    private Map<Integer, Task> tasks = new HashMap<>();
    private Map<Integer, List<Integer>> users = new HashMap<>();

    public TodoList() {}

    public int addTask(int userId, String taskDescription, int dueDate, List<String> tags) {
        int id = nextID++;
        Task tk = new Task();
        tk.id = id;
        tk.description = taskDescription;
        tk.dueDate = dueDate;
        tk.userId = userId;
        tk.tags.addAll(tags);
        tasks.put(id, tk);
        users.computeIfAbsent(userId, k -> new ArrayList<>()).add(id);
        return id;
    }

    public List<String> getAllTasks(int userId) {
        if (!users.containsKey(userId)) return new ArrayList<>();
        List<Integer> ids = new ArrayList<>(users.get(userId));
        ids.sort((a, b) -> Integer.compare(tasks.get(a).dueDate, tasks.get(b).dueDate));
        List<String> ans = new ArrayList<>();
        for (int id : ids) {
            if (!tasks.get(id).done) ans.add(tasks.get(id).description);
        }
        return ans;
    }

    public List<String> getTasksForTag(int userId, String tag) {
        if (!users.containsKey(userId)) return new ArrayList<>();
        List<Integer> ids = new ArrayList<>(users.get(userId));
        ids.sort((a, b) -> Integer.compare(tasks.get(a).dueDate, tasks.get(b).dueDate));
        List<String> ans = new ArrayList<>();
        for (int id : ids) {
            Task tk = tasks.get(id);
            if (!tk.done && tk.tags.contains(tag)) ans.add(tk.description);
        }
        return ans;
    }

    public void completeTask(int userId, int taskId) {
        Task tk = tasks.get(taskId);
        if (tk == null || tk.userId != userId || tk.done) return;
        tk.done = true;
    }
}
