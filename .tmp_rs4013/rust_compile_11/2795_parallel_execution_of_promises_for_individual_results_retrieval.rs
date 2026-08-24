struct Solution;
fn main() {}

// LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
// https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/

impl Solution {
    pub fn promise_all_settled<F: Fn() -> i32>(functions: Vec<F>) -> Vec<(String, i32)> {
        functions
            .into_iter()
            .map(|f| ("fulfilled".to_string(), f()))
            .collect()
    }
}
