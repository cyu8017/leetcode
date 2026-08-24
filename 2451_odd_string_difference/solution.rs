// LeetCode 2451 - Odd String Difference
// https://leetcode.com/problems/odd-string-difference/

impl Solution {
    pub fn odd_string(words: Vec<String>) -> String {
        fn diff(w: &str) -> Vec<i32> {
            let b = w.as_bytes();
            let mut d = Vec::new();
            for i in 1..b.len() {
                d.push(b[i] as i32 - b[i - 1] as i32);
            }
            d
        }
        let d0 = diff(&words[0]);
        let d1 = diff(&words[1]);
        if d0 == d1 {
            for i in 2..words.len() {
                if diff(&words[i]) != d0 {
                    return words[i].clone();
                }
            }
        }
        if diff(&words[2]) == d0 {
            return words[1].clone();
        }
        words[0].clone()
    }
}
