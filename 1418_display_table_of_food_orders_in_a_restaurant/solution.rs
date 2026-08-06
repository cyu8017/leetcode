// LeetCode 1418 - Display Table of Food Orders in a Restaurant
// https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

use std::collections::{BTreeSet, HashMap, HashSet};

impl Solution {
    pub fn display_table(orders: Vec<Vec<String>>) -> Vec<Vec<String>> {
        let mut foods: BTreeSet<String> = BTreeSet::new();
        let mut tables: BTreeSet<i32> = BTreeSet::new();
        let mut counts: HashMap<(i32, String), i32> = HashMap::new();
        for order in &orders {
            let table: i32 = order[1].parse().unwrap();
            let food = order[2].clone();
            foods.insert(food.clone());
            tables.insert(table);
            *counts.entry((table, food)).or_insert(0) += 1;
        }
        let foods: Vec<String> = foods.into_iter().collect();
        let mut result = vec![std::iter::once("Table".to_string())
            .chain(foods.iter().cloned())
            .collect()];
        for table in tables {
            let mut row = vec![table.to_string()];
            for food in &foods {
                row.push(counts.get(&(table, food.clone())).copied().unwrap_or(0).to_string());
            }
            result.push(row);
        }
        result
    }
}
