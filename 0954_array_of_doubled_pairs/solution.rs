// LeetCode 0954 - Array of Doubled Pairs
// https://leetcode.com/problems/array-of-doubled-pairs/

use std::collections::BTreeMap;

impl Solution {
    pub fn can_reorder_doubled(arr: Vec<i32>) -> bool {
        let mut count = BTreeMap::new();
        for x in arr {
            *count.entry(x).or_insert(0) += 1;
        }
        let mut keys: Vec<i32> = count.keys().copied().collect();
        keys.sort_by_key(|x| x.abs());
        for x in keys {
            let cx = *count.get(&x).unwrap_or(&0);
            if cx == 0 {
                continue;
            }
            let c2 = *count.get(&(2 * x)).unwrap_or(&0);
            if c2 < cx {
                return false;
            }
            *count.entry(2 * x).or_insert(0) -= cx;
        }
        true
    }
}
