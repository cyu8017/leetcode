// LeetCode 0843 - Guess the Word
// https://leetcode.com/problems/guess-the-word/

pub struct Master;

impl Master {
    pub fn guess(&self, _word: String) -> i32 {
        0
    }
}

impl Solution {
    pub fn find_secret_word(words: Vec<String>, master: &Master) {
        fn match_count(a: &str, b: &str) -> i32 {
            a.bytes()
                .zip(b.bytes())
                .filter(|(x, y)| x == y)
                .count() as i32
        }

        let mut candidates = words;
        while !candidates.is_empty() {
            let mut best = candidates[0].clone();
            let mut best_worst = candidates.len() as i32 + 1;
            for w in &candidates {
                let mut buckets = [0i32; 7];
                for c in &candidates {
                    buckets[match_count(w, c) as usize] += 1;
                }
                let worst = *buckets.iter().max().unwrap();
                if worst < best_worst {
                    best_worst = worst;
                    best = w.clone();
                }
            }
            let score = master.guess(best.clone());
            if score == 6 {
                return;
            }
            candidates.retain(|c| match_count(c, &best) == score);
        }
    }
}
