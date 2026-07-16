// LeetCode 0339 - Nested List Weight Sum
// https://leetcode.com/problems/nested-list-weight-sum/

pub struct NestedInteger {
    integer: Option<i32>,
    list: Vec<NestedInteger>,
}

impl NestedInteger {
    pub fn new(value: Option<i32>) -> Self {
        NestedInteger {
            integer: value,
            list: Vec::new(),
        }
    }

    pub fn is_integer(&self) -> bool {
        self.integer.is_some()
    }

    pub fn get_integer(&self) -> i32 {
        self.integer.unwrap_or(0)
    }

    pub fn get_list(&self) -> &Vec<NestedInteger> {
        &self.list
    }
}

impl Solution {
    pub fn depth_sum(nested_list: Vec<NestedInteger>) -> i32 {
        let mut total = 0;
        Self::dfs(&nested_list, 1, &mut total);
        total
    }

    fn dfs(items: &[NestedInteger], depth: i32, total: &mut i32) {
        for item in items {
            if item.is_integer() {
                *total += item.get_integer() * depth;
            } else {
                Self::dfs(item.get_list(), depth + 1, total);
            }
        }
    }
}
