// LeetCode 1600 - Throne Inheritance
// https://leetcode.com/problems/throne-inheritance/

use std::collections::{HashMap, HashSet};

pub struct ThroneInheritance {
    king: String,
    children: HashMap<String, Vec<String>>,
    dead: HashSet<String>,
}

impl ThroneInheritance {
    pub fn new(king_name: String) -> Self {
        Self {
            king: king_name,
            children: HashMap::new(),
            dead: HashSet::new(),
        }
    }

    pub fn birth(&mut self, parent_name: String, child_name: String) {
        self.children.entry(parent_name).or_default().push(child_name);
    }

    pub fn death(&mut self, name: String) {
        self.dead.insert(name);
    }

    pub fn get_inheritance_order(&self) -> Vec<String> {
        let mut order = Vec::new();
        self.visit(&self.king, &mut order);
        order
    }

    fn visit(&self, name: &str, order: &mut Vec<String>) {
        if !self.dead.contains(name) {
            order.push(name.to_string());
        }
        if let Some(kids) = self.children.get(name) {
            for child in kids {
                self.visit(child, order);
            }
        }
    }
}
