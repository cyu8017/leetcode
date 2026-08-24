// LeetCode 0953 - Verifying an Alien Dictionary
// https://leetcode.com/problems/verifying-an-alien-dictionary/

impl Solution {
    pub fn is_alien_sorted(words: Vec<String>, order: String) -> bool {
        let mut rank = [0i32; 26];
        for (i, b) in order.bytes().enumerate() {
            rank[(b - b'a') as usize] = i as i32;
        }
        let less_eq = |a: &str, b: &str| {
            let n = a.len().min(b.len());
            let ab = a.as_bytes();
            let bb = b.as_bytes();
            for i in 0..n {
                let ra = rank[(ab[i] - b'a') as usize];
                let rb = rank[(bb[i] - b'a') as usize];
                if ra != rb {
                    return ra < rb;
                }
            }
            a.len() <= b.len()
        };
        for i in 0..words.len().saturating_sub(1) {
            if !less_eq(&words[i], &words[i + 1]) {
                return false;
            }
        }
        true
    }
}
