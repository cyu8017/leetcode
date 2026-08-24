fn main() {}

// LeetCode 2756 - Query Batching
// https://leetcode.com/problems/query-batching/

pub struct QueryBatcher {
    pending: Vec<i32>,
}

impl QueryBatcher {
    pub fn new(_query_multiple: fn(Vec<i32>) -> Vec<i32>, _t: i32) -> Self {
        Self {
            pending: Vec::new(),
        }
    }

    pub fn add_query(&mut self, query: i32) {
        self.pending.push(query);
    }
}
