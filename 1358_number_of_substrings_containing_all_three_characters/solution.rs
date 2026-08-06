// LeetCode 1358 - Number of Substrings Containing All Three Characters
// https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        let mut last = [-1i32; 3];
        let mut ans = 0;
        for (i, c) in s.bytes().enumerate() {
            last[(c - b'a') as usize] = i as i32;
            ans += last.iter().copied().min().unwrap() + 1;
        }
        ans
    }
}
