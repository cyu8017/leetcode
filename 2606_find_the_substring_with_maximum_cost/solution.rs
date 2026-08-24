// LeetCode 2606 - Find the Substring With Maximum Cost
// https://leetcode.com/problems/find-the-substring-with-maximum-cost/

impl Solution {
    pub fn maximum_cost_substring(s: String, chars: String, vals: Vec<i32>) -> i32 {
        let mut val = [0i32; 26];
        for i in 0..26 {
            val[i] = i as i32 + 1;
        }
        for (i, c) in chars.bytes().enumerate() {
            val[(c - b'a') as usize] = vals[i];
        }
        let mut best = 0;
        let mut cur = 0;
        for c in s.bytes() {
            cur += val[(c - b'a') as usize];
            if cur < 0 {
                cur = 0;
            }
            if cur > best {
                best = cur;
            }
        }
        best
    }
}
