struct Solution;
// LeetCode 3450 - Maximum Students on a Single Bench
// https://leetcode.com/problems/maximum-students-on-a-single-bench/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn max_students_on_bench(students: Vec<Vec<i32>>) -> i32 {
        let mut bench: HashMap<i32, HashSet<i32>> = HashMap::new();
        for s in students {
            bench.entry(s[1]).or_default().insert(s[0]);
        }
        let mut ans = 0;
        for set in bench.values() {
            if set.len() as i32 > ans {
                ans = set.len() as i32;
            }
        }
        ans
    }
}

fn main() {}
