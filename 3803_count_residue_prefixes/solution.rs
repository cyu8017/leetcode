// LeetCode 3803 - Count Residue Prefixes
// https://leetcode.com/problems/count-residue-prefixes/

use std::collections::HashSet;

impl Solution {
    pub fn residue_prefixes(s: String) -> i32 {
        let mut st = HashSet::new();
        let mut ans = 0;
        for (i, c) in s.bytes().enumerate() {
            st.insert(c);
            if st.len() as i32 == ((i + 1) % 3) as i32 {
                ans += 1;
            }
        }
        ans
    }
}
