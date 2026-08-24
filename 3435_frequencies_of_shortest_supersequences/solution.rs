// LeetCode 3435 - Frequencies of Shortest Supersequences
// https://leetcode.com/problems/frequencies-of-shortest-supersequences/

impl Solution {
    pub fn supersequences(words: Vec<String>) -> Vec<Vec<i32>> {
        let mut used = [false; 26];
        for w in &words {
            let b = w.as_bytes();
            used[(b[0] - b'a') as usize] = true;
            used[(b[1] - b'a') as usize] = true;
        }
        let letters: Vec<usize> = (0..26).filter(|&i| used[i]).collect();
        let m = letters.len();
        let mut best = 1_000_000_000;
        let mut best_freqs = Vec::new();
        let mut freq = [0i32; 26];
        fn dfs(
            i: usize,
            m: usize,
            letters: &[usize],
            words: &[String],
            freq: &mut [i32; 26],
            best: &mut i32,
            best_freqs: &mut Vec<Vec<i32>>,
        ) {
            if i == m {
                let mut ok = true;
                for w in words {
                    let b = w.as_bytes();
                    let a = (b[0] - b'a') as usize;
                    let bb = (b[1] - b'a') as usize;
                    if a == bb {
                        if freq[a] < 2 {
                            ok = false;
                            break;
                        }
                    } else if freq[a] < 1 || freq[bb] < 1 {
                        ok = false;
                        break;
                    }
                }
                if !ok {
                    return;
                }
                let sum: i32 = freq.iter().sum();
                let f = freq.to_vec();
                if sum < *best {
                    *best = sum;
                    *best_freqs = vec![f];
                } else if sum == *best {
                    best_freqs.push(f);
                }
                return;
            }
            let l = letters[i];
            for c in 1..=2 {
                freq[l] = c;
                dfs(i + 1, m, letters, words, freq, best, best_freqs);
            }
            freq[l] = 0;
        }
        dfs(0, m, &letters, &words, &mut freq, &mut best, &mut best_freqs);
        best_freqs
    }
}
