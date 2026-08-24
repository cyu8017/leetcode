// LeetCode 3885 - Design Event Manager
// https://leetcode.com/problems/design-event-manager/

use std::collections::{BTreeSet, HashMap};

pub struct EventManager {
    sl: BTreeSet<(i32, i32)>,
    d: HashMap<i32, i32>,
}

impl EventManager {
    pub fn new(events: Vec<Vec<i32>>) -> Self {
        let mut sl = BTreeSet::new();
        let mut d = HashMap::new();
        for e in events {
            let event_id = e[0];
            let priority = e[1];
            sl.insert((-priority, event_id));
            d.insert(event_id, priority);
        }
        Self { sl, d }
    }

    pub fn update_priority(&mut self, event_id: i32, new_priority: i32) {
        let old = self.d[&event_id];
        self.sl.remove(&(-old, event_id));
        self.sl.insert((-new_priority, event_id));
        self.d.insert(event_id, new_priority);
    }

    pub fn poll_highest(&mut self) -> i32 {
        let Some(&(neg_p, event_id)) = self.sl.iter().next() else {
            return -1;
        };
        self.sl.remove(&(neg_p, event_id));
        self.d.remove(&event_id);
        event_id
    }
}
