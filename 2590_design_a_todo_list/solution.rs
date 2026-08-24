// LeetCode 2590 - Design a Todo List
// https://leetcode.com/problems/design-a-todo-list/

use std::collections::{HashMap, HashSet};

struct Task {
    id: i32,
    description: String,
    due_date: i32,
    tags: HashSet<String>,
    done: bool,
    user_id: i32,
}

pub struct TodoList {
    next_id: i32,
    tasks: HashMap<i32, Task>,
    users: HashMap<i32, Vec<i32>>,
}

impl TodoList {
    pub fn new() -> Self {
        Self {
            next_id: 1,
            tasks: HashMap::new(),
            users: HashMap::new(),
        }
    }

    pub fn add_task(
        &mut self,
        user_id: i32,
        task_description: String,
        due_date: i32,
        tags: Vec<String>,
    ) -> i32 {
        let id = self.next_id;
        self.next_id += 1;
        let tk = Task {
            id,
            description: task_description,
            due_date,
            tags: tags.into_iter().collect(),
            done: false,
            user_id,
        };
        self.tasks.insert(id, tk);
        self.users.entry(user_id).or_default().push(id);
        id
    }

    pub fn get_all_tasks(&self, user_id: i32) -> Vec<String> {
        let mut ids = self.users.get(&user_id).cloned().unwrap_or_default();
        ids.sort_by_key(|id| self.tasks[id].due_date);
        ids.into_iter()
            .filter(|id| !self.tasks[id].done)
            .map(|id| self.tasks[&id].description.clone())
            .collect()
    }

    pub fn get_tasks_for_tag(&self, user_id: i32, tag: String) -> Vec<String> {
        let mut ids = self.users.get(&user_id).cloned().unwrap_or_default();
        ids.sort_by_key(|id| self.tasks[id].due_date);
        ids.into_iter()
            .filter(|id| {
                let tk = &self.tasks[id];
                !tk.done && tk.tags.contains(&tag)
            })
            .map(|id| self.tasks[&id].description.clone())
            .collect()
    }

    pub fn complete_task(&mut self, user_id: i32, task_id: i32) {
        if let Some(tk) = self.tasks.get_mut(&task_id) {
            if tk.user_id == user_id && !tk.done {
                tk.done = true;
            }
        }
    }
}
