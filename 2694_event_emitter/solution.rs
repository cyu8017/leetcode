// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;

pub struct EventEmitter {
    handlers: Rc<RefCell<HashMap<String, Vec<Option<Box<dyn Fn(&Vec<i32>)>>>>>>,
}

impl EventEmitter {
    pub fn new() -> Self {
        Self {
            handlers: Rc::new(RefCell::new(HashMap::new())),
        }
    }

    pub fn subscribe(
        &self,
        event_name: String,
        callback: Box<dyn Fn(&Vec<i32>)>,
    ) -> impl Fn() {
        let mut h = self.handlers.borrow_mut();
        let v = h.entry(event_name.clone()).or_default();
        v.push(Some(callback));
        let idx = v.len() - 1;
        let handlers = self.handlers.clone();
        move || {
            if let Some(list) = handlers.borrow_mut().get_mut(&event_name) {
                if idx < list.len() {
                    list[idx] = None;
                }
            }
        }
    }

    pub fn emit(&self, event_name: String, args: Vec<i32>) -> Vec<i32> {
        let h = self.handlers.borrow();
        let mut res = Vec::new();
        if let Some(list) = h.get(&event_name) {
            for cb in list.iter().flatten() {
                cb(&args);
                res.push(0);
            }
        }
        res
    }
}

impl Solution {
    pub fn create_emitter() -> EventEmitter {
        EventEmitter::new()
    }
}
