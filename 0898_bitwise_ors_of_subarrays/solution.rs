// LeetCode 0898 - Bitwise ORs of Subarrays
// https://leetcode.com/problems/bitwise-ors-of-subarrays/

use std::collections::HashSet;

impl Solution {
    pub fn subarray_bitwise_o_rs(arr: Vec<i32>) -> i32 {
        let mut ans = HashSet::new();
        let mut cur = HashSet::new();
        for x in arr {
            let mut nxt = HashSet::new();
            nxt.insert(x);
            for y in cur {
                nxt.insert(x | y);
            }
            cur = nxt;
            ans.extend(cur.iter().copied());
        }
        ans.len() as i32
    }
}
