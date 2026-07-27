// LeetCode 1668 - Maximum Repeating Substring
// https://leetcode.com/problems/maximum-repeating-substring/

impl Solution {
    pub fn max_repeating(sequence: String, word: String) -> i32 {
        let mut k = 0;
        let mut cur = word.clone();
        while sequence.contains(&cur) {
            k += 1;
            cur.push_str(&word);
        }
        k
    }
}
