// LeetCode 0916 - Word Subsets
// https://leetcode.com/problems/word-subsets/

impl Solution {
    pub fn word_subsets(words1: Vec<String>, words2: Vec<String>) -> Vec<String> {
        let mut need = [0i32; 26];
        for w in &words2 {
            let mut cnt = [0i32; 26];
            for b in w.bytes() {
                cnt[(b - b'a') as usize] += 1;
            }
            for i in 0..26 {
                need[i] = need[i].max(cnt[i]);
            }
        }
        words1
            .into_iter()
            .filter(|w| {
                let mut cnt = [0i32; 26];
                for b in w.bytes() {
                    cnt[(b - b'a') as usize] += 1;
                }
                (0..26).all(|i| cnt[i] >= need[i])
            })
            .collect()
    }
}
