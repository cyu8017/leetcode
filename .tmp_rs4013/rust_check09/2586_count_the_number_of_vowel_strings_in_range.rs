struct Solution;

// LeetCode 2586 - Count the Number of Vowel Strings in Range
// https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

impl Solution {
    pub fn vowel_strings(words: Vec<String>, left: i32, right: i32) -> i32 {
        fn is_v(c: u8) -> bool {
            matches!(c, b'a' | b'e' | b'i' | b'o' | b'u')
        }
        let mut ans = 0;
        for i in left as usize..=right as usize {
            let w = words[i].as_bytes();
            if is_v(w[0]) && is_v(w[w.len() - 1]) {
                ans += 1;
            }
        }
        ans
    }
}

fn main() {}
