// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

impl Solution {
    pub fn max_score_words(words: Vec<String>, letters: Vec<char>, score: Vec<i32>) -> i32 {
        let mut available = [0; 26];
        for ch in letters {
            available[(ch as u8 - b'a') as usize] += 1;
        }
        let counts: Vec<[i32; 26]> = words
            .iter()
            .map(|word| {
                let mut c = [0; 26];
                for b in word.bytes() {
                    c[(b - b'a') as usize] += 1;
                }
                c
            })
            .collect();
        let values: Vec<i32> = words
            .iter()
            .map(|word| word.bytes().map(|b| score[(b - b'a') as usize]).sum())
            .collect();
        fn dfs(
            i: usize,
            words_len: usize,
            counts: &[[i32; 26]],
            values: &[i32],
            available: &mut [i32; 26],
        ) -> i32 {
            if i == words_len {
                return 0;
            }
            let mut best = dfs(i + 1, words_len, counts, values, available);
            let ok = (0..26).all(|c| counts[i][c] <= available[c]);
            if ok {
                for c in 0..26 {
                    available[c] -= counts[i][c];
                }
                best = best.max(values[i] + dfs(i + 1, words_len, counts, values, available));
                for c in 0..26 {
                    available[c] += counts[i][c];
                }
            }
            best
        }
        dfs(0, words.len(), &counts, &values, &mut available)
    }
}
