// LeetCode 2408 - Design SQL
// https://leetcode.com/problems/design-sql/

use std::collections::HashMap;

pub struct SQL {
    tables: HashMap<String, Vec<Vec<String>>>,
    next_id: HashMap<String, i32>,
}

impl SQL {
    pub fn new(names: Vec<String>, _columns: Vec<i32>) -> Self {
        let mut tables = HashMap::new();
        let mut next_id = HashMap::new();
        for name in names {
            tables.insert(name.clone(), Vec::new());
            next_id.insert(name, 1);
        }
        Self { tables, next_id }
    }

    pub fn ins(&mut self, name: String, row: Vec<String>) -> bool {
        if !self.tables.contains_key(&name) {
            return false;
        }
        let id = self.next_id[&name];
        *self.next_id.get_mut(&name).unwrap() += 1;
        let mut full = vec![id.to_string()];
        full.extend(row);
        self.tables.get_mut(&name).unwrap().push(full);
        true
    }

    pub fn rmv(&mut self, name: String, row_id: i32) {
        if let Some(rows) = self.tables.get_mut(&name) {
            if let Some(i) = rows.iter().position(|r| r[0].parse::<i32>().unwrap() == row_id) {
                rows.remove(i);
            }
        }
    }

    pub fn sel(&self, name: String, row_id: i32, column_id: i32) -> String {
        if let Some(rows) = self.tables.get(&name) {
            for r in rows {
                if r[0].parse::<i32>().unwrap() == row_id {
                    if column_id < 1 || column_id >= r.len() as i32 {
                        return "<null>".to_string();
                    }
                    return r[column_id as usize].clone();
                }
            }
        }
        "<null>".to_string()
    }

    pub fn exp(&self, name: String) -> Vec<String> {
        self.tables
            .get(&name)
            .map(|rows| rows.iter().map(|r| r.join(",")).collect())
            .unwrap_or_default()
    }
}
