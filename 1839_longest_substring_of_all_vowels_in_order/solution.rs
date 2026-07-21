// LeetCode 1839 - Longest Substring Of All Vowels in Order
// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

impl Solution {
    pub fn longest_beautiful_substring(word: String) -> i32 {
        let vowels = b"aeiou";
        let bytes = word.as_bytes();
        let mut best = 0;

        for start in 0..bytes.len() {
            if bytes[start] != b'a' {
                continue;
            }

            let mut counts = [0; 5];
            for end in start..bytes.len() {
                let current = bytes[end];
                if end > start && current < bytes[end - 1] {
                    break;
                }

                let idx = match vowels.iter().position(|&v| v == current) {
                    Some(i) => i,
                    None => break,
                };
                counts[idx] += 1;
                if idx > 0 && counts[idx - 1] == 0 {
                    break;
                }
                if counts.iter().all(|&count| count > 0) {
                    best = best.max((end - start + 1) as i32);
                }
            }
        }

        best
    }
}
