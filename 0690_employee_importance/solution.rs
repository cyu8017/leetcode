// LeetCode 0690 - Employee Importance
// https://leetcode.com/problems/employee-importance/

use std::collections::HashMap;

pub struct Employee {
    pub id: i32,
    pub importance: i32,
    pub subordinates: Vec<i32>,
}

impl Solution {
    pub fn get_importance(employees: Vec<Employee>, id: i32) -> i32 {
        let mut table = HashMap::new();
        for emp in &employees {
            table.insert(emp.id, (emp.importance, emp.subordinates.clone()));
        }
        Self::dfs(id, &table)
    }

    fn dfs(eid: i32, table: &HashMap<i32, (i32, Vec<i32>)>) -> i32 {
        let (importance, subordinates) = table.get(&eid).unwrap();
        importance + subordinates.iter().map(|&sub| Self::dfs(sub, table)).sum::<i32>()
    }
}
