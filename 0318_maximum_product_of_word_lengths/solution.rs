// LeetCode 0318 - Maximum Product of Word Lengths
// https://leetcode.com/problems/maximum-product-of-word-lengths/

impl Solution {
    pub fn max_product(words: Vec<String>) -> i32 {
        let mut masks = Vec::with_capacity(words.len());
        let mut lengths = Vec::with_capacity(words.len());

        for word in &words {
            let mut mask = 0;
            let mut valid = true;
            for character in word.bytes() {
                let bit = 1 << (character - b'a');
                if mask & bit != 0 {
                    valid = false;
                    break;
                }
                mask |= bit;
            }
            masks.push(if valid { mask } else { 0 });
            lengths.push(word.len() as i32);
        }

        let mut best = 0;
        for left in 0..words.len() {
            if masks[left] == 0 {
                continue;
            }
            for right in left + 1..words.len() {
                if masks[right] == 0 {
                    continue;
                }
                if masks[left] & masks[right] == 0 {
                    best = best.max(lengths[left] * lengths[right]);
                }
            }
        }

        best
    }
}
