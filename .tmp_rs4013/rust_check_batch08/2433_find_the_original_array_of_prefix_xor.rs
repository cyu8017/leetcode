struct Solution;
// LeetCode 2433 - Find The Original Array of Prefix Xor
// https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

impl Solution {
    pub fn find_array(pref: Vec<i32>) -> Vec<i32> {
        let mut ans = vec![0; pref.len()];
        ans[0] = pref[0];
        for i in 1..pref.len() {
            ans[i] = pref[i] ^ pref[i - 1];
        }
        ans
    }
}

fn main() {}
