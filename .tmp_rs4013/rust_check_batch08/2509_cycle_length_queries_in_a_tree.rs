struct Solution;
// LeetCode 2509 - Cycle Length Queries in a Tree
// https://leetcode.com/problems/cycle-length-queries-in-a-tree/

impl Solution {
    pub fn cycle_length_queries(_n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut ans = vec![0; queries.len()];
        for (i, q) in queries.iter().enumerate() {
            let mut a = q[0];
            let mut b = q[1];
            let mut steps = 0;
            while a != b {
                if a > b {
                    a /= 2;
                } else {
                    b /= 2;
                }
                steps += 1;
            }
            ans[i] = steps + 1;
        }
        ans
    }
}

fn main() {}
