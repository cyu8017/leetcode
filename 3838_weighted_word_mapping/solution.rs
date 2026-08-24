// LeetCode 3838 - Weighted Word Mapping
// https://leetcode.com/problems/weighted-word-mapping/

impl Solution {
    pub fn map_word_weights(words: Vec<String>, weights: Vec<i32>) -> String {
        let mut ans = String::new();
        for w in words {
            let mut s = 0;
            for c in w.bytes() {
                s = (s + weights[(c - b'a') as usize]) % 26;
            }
            ans.push((b'a' + (25 - s) as u8) as char);
        }
        ans
    }
}
