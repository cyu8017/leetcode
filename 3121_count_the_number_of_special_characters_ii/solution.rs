// LeetCode 3121 - Count the Number of Special Characters II
// https://leetcode.com/problems/count-the-number-of-special-characters-ii/

impl Solution {
    pub fn number_of_special_chars(word: String) -> i32 {
        let mut first = [0i32; 128];
        let mut last = [0i32; 128];
        for (i, c) in word.bytes().enumerate() {
            if first[c as usize] == 0 {
                first[c as usize] = i as i32 + 1;
            }
            last[c as usize] = i as i32 + 1;
        }
        let mut ans = 0;
        for i in 0..26 {
            if last[b'a' as usize + i] > 0 && last[b'a' as usize + i] < first[b'A' as usize + i] {
                ans += 1;
            }
        }
        ans
    }
}
