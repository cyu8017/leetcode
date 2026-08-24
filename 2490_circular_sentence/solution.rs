// LeetCode 2490 - Circular Sentence
// https://leetcode.com/problems/circular-sentence/

impl Solution {
    pub fn is_circular_sentence(sentence: String) -> bool {
        let b = sentence.as_bytes();
        let n = b.len();
        if b[0] != b[n - 1] {
            return false;
        }
        for i in 0..n {
            if b[i] == b' ' && b[i - 1] != b[i + 1] {
                return false;
            }
        }
        true
    }
}
