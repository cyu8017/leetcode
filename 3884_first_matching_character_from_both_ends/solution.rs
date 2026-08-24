// LeetCode 3884 - First Matching Character From Both Ends
// https://leetcode.com/problems/first-matching-character-from-both-ends/

impl Solution {
    pub fn first_matching_index(s: String) -> i32 {
        let b = s.as_bytes();
        let n = b.len();
        for i in 0..n / 2 + 1 {
            if b[i] == b[n - i - 1] {
                return i as i32;
            }
        }
        -1
    }
}
