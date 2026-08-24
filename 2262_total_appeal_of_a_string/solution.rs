// LeetCode 2262 - Total Appeal of A String
// https://leetcode.com/problems/total-appeal-of-a-string/

impl Solution {
    pub fn appeal_sum(s: String) -> i64 {
        let mut last = [-1i32; 26];
        let mut ans = 0i64;
        let mut cur = 0i64;
        for (i, c) in s.bytes().enumerate() {
            let idx = (c - b'a') as usize;
            cur += i as i64 - last[idx] as i64;
            last[idx] = i as i32;
            ans += cur;
        }
        ans
    }
}
