// LeetCode 3408 - Design Task Manager
// https://leetcode.com/problems/design-task-manager/

use std::cmp::Ordering;
use std::collections::{BinaryHeap, HashMap};

#[derive(Eq, PartialEq)]
struct Item {
    pri: i32,
    task_id: i32,
    user_id: i32,
}

impl Ord for Item {
    fn cmp(&self, other: &Self) -> Ordering {
        self.pri
            .cmp(&other.pri)
            .then(self.task_id.cmp(&other.task_id))
    }
}

impl PartialOrd for Item {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

pub struct TaskManager {
    h: BinaryHeap<Item>,
    pri: HashMap<i32, i32>,
    user: HashMap<i32, i32>,
}

impl TaskManager {
    pub fn new(tasks: Vec<Vec<i32>>) -> Self {
        let mut tm = Self {
            h: BinaryHeap::new(),
            pri: HashMap::new(),
            user: HashMap::new(),
        };
        for t in tasks {
            tm.add(t[0], t[1], t[2]);
        }
        tm
    }

    pub fn add(&mut self, user_id: i32, task_id: i32, priority: i32) {
        self.pri.insert(task_id, priority);
        self.user.insert(task_id, user_id);
        self.h.push(Item {
            pri: priority,
            task_id,
            user_id,
        });
    }

    pub fn edit(&mut self, task_id: i32, new_priority: i32) {
        self.pri.insert(task_id, new_priority);
        let user_id = self.user[&task_id];
        self.h.push(Item {
            pri: new_priority,
            task_id,
            user_id,
        });
    }

    pub fn rmv(&mut self, task_id: i32) {
        self.pri.remove(&task_id);
        self.user.remove(&task_id);
    }

    pub fn exec_top(&mut self) -> i32 {
        while let Some(top) = self.h.pop() {
            if let Some(&p) = self.pri.get(&top.task_id) {
                if p == top.pri && self.user[&top.task_id] == top.user_id {
                    self.pri.remove(&top.task_id);
                    let uid = self.user.remove(&top.task_id).unwrap();
                    return uid;
                }
            }
        }
        -1
    }
}
