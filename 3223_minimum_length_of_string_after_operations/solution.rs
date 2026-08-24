// LeetCode 3223 - Minimum Length of String After Operations
// https://leetcode.com/problems/minimum-length-of-string-after-operations/

impl Solution {
    pub fn minimum_length(s: String) -> i32 {
        let mut cnt = [0; 26];
        for c in s.bytes() {
            cnt[(c - b'a') as usize] += 1;
        }
        let mut ans = 0;
        for x in cnt {
            if x > 0 {
                ans += if x & 1 == 1 { 1 } else { 2 };
            }
        }
        ans
    }
}
