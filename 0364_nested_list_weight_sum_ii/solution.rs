// LeetCode 0364 - Nested List Weight Sum II
// https://leetcode.com/problems/nested-list-weight-sum-ii/

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
        let mut weighted: Vec<(i32, i32)> = Vec::new();
        Self::dfs(&nested_list, 1, &mut weighted);

        if weighted.is_empty() {
            return 0;
        }

        let max_depth = weighted.iter().map(|entry| entry.1).max().unwrap();
        weighted
            .iter()
            .map(|entry| entry.0 * (max_depth - entry.1 + 1))
            .sum()
    }

    fn dfs(items: &[NestedInteger], depth: i32, weighted: &mut Vec<(i32, i32)>) {
        for item in items {
            if item.is_integer() {
                weighted.push((item.get_integer(), depth));
            } else {
                Self::dfs(item.get_list(), depth + 1, weighted);
            }
        }
    }
}
