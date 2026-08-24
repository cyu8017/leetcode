// LeetCode 0792 - Number of Matching Subsequences
// https://leetcode.com/problems/number-of-matching-subsequences/

impl Solution {
    pub fn num_matching_subseq(s: String, words: Vec<String>) -> i32 {
        let mut waiting: Vec<Vec<(usize, usize)>> = vec![Vec::new(); 128];
        for (i, word) in words.iter().enumerate() {
            let first = word.as_bytes()[0] as usize;
            waiting[first].push((i, 0));
        }
        let mut count = 0;
        for ch in s.bytes() {
            let advance = std::mem::take(&mut waiting[ch as usize]);
            for (wi, mut idx) in advance {
                idx += 1;
                if idx == words[wi].len() {
                    count += 1;
                } else {
                    let next = words[wi].as_bytes()[idx] as usize;
                    waiting[next].push((wi, idx));
                }
            }
        }
        count
    }
}
