// LeetCode 2590 - Design a Todo List
// https://leetcode.com/problems/design-a-todo-list/

using System;
using System.Collections.Generic;
using System.Linq;

public class TodoList {
    class Task {
        public int Id;
        public string Description;
        public int DueDate;
        public HashSet<string> Tags = new HashSet<string>();
        public bool Done;
        public int UserId;
    }

    int nextID = 1;
    Dictionary<int, Task> tasks = new Dictionary<int, Task>();
    Dictionary<int, List<int>> users = new Dictionary<int, List<int>>();

    public TodoList() {}

    public int AddTask(int userId, string taskDescription, int dueDate, IList<string> tags) {
        int id = nextID++;
        var tk = new Task {
            Id = id,
            Description = taskDescription,
            DueDate = dueDate,
            UserId = userId
        };
        foreach (var x in tags) tk.Tags.Add(x);
        tasks[id] = tk;
        if (!users.ContainsKey(userId)) users[userId] = new List<int>();
        users[userId].Add(id);
        return id;
    }

    public IList<string> GetAllTasks(int userId) {
        if (!users.ContainsKey(userId)) return new List<string>();
        var ids = users[userId].ToList();
        ids.Sort((a, b) => tasks[a].DueDate.CompareTo(tasks[b].DueDate));
        var ans = new List<string>();
        foreach (int id in ids) {
            if (!tasks[id].Done) ans.Add(tasks[id].Description);
        }
        return ans;
    }

    public IList<string> GetTasksForTag(int userId, string tag) {
        if (!users.ContainsKey(userId)) return new List<string>();
        var ids = users[userId].ToList();
        ids.Sort((a, b) => tasks[a].DueDate.CompareTo(tasks[b].DueDate));
        var ans = new List<string>();
        foreach (int id in ids) {
            var tk = tasks[id];
            if (!tk.Done && tk.Tags.Contains(tag)) ans.Add(tk.Description);
        }
        return ans;
    }

    public void CompleteTask(int userId, int taskId) {
        if (!tasks.TryGetValue(taskId, out var tk) || tk.UserId != userId || tk.Done) return;
        tk.Done = true;
    }
}
