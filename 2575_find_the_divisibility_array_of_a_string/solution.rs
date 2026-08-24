// LeetCode 2575 - Find the Divisibility Array of a String
// https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

impl Solution {
    pub fn divisibility_array(word: String, m: i32) -> Vec<i32> {
        let mut ans = vec![0; word.len()];
        let mut cur = 0i64;
        let m = m as i64;
        for (i, c) in word.bytes().enumerate() {
            cur = (cur * 10 + (c - b'0') as i64) % m;
            if cur == 0 {
                ans[i] = 1;
            }
        }
        ans
    }
}
