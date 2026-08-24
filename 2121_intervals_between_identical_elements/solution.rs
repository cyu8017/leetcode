// LeetCode 2121 - Intervals Between Identical Elements
// https://leetcode.com/problems/intervals-between-identical-elements/

use std::collections::HashMap;

impl Solution {
    pub fn get_distances(arr: Vec<i32>) -> Vec<i64> {
        let n = arr.len();
        let mut pos: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in arr.iter().enumerate() {
            pos.entry(v).or_default().push(i);
        }
        let mut ans = vec![0i64; n];
        for idxs in pos.values() {
            let m = idxs.len();
            let mut pref = vec![0i64; m + 1];
            for i in 0..m {
                pref[i + 1] = pref[i] + idxs[i] as i64;
            }
            for i in 0..m {
                let left = i as i64 * idxs[i] as i64 - pref[i];
                let right = (pref[m] - pref[i + 1]) - (m as i64 - i as i64 - 1) * idxs[i] as i64;
                ans[idxs[i]] = left + right;
            }
        }
        ans
    }
}
