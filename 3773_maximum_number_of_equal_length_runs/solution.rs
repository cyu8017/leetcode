// LeetCode 3773 - Maximum Number Of Equal Length Runs
// https://leetcode.com/problems/maximum-number-of-equal-length-runs/

use std::collections::HashMap;

impl Solution {
    pub fn max_same_length_runs(s: String) -> i32 {
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut ans = 0;
        let mut i = 0;
        while i < n {
            let mut j = i + 1;
            while j < n && bytes[j] == bytes[i] {
                j += 1;
            }
            let m = (j - i) as i32;
            let e = cnt.entry(m).or_insert(0);
            *e += 1;
            ans = ans.max(*e);
            i = j;
        }
        ans
    }
}
