// LeetCode 0471 - Encode String with Shortest Length
// https://leetcode.com/problems/encode-string-with-shortest-length/

impl Solution {
    fn encode_word(word: &str) -> String {
        let size = word.len();
        let mut best = word.to_string();
        for unit_length in 1..=size / 2 {
            if size % unit_length != 0 {
                continue;
            }
            let unit = &word[..unit_length];
            let matches = (unit_length..size)
                .step_by(unit_length)
                .all(|start| &word[start..start + unit_length] == unit);
            if !matches {
                continue;
            }
            let encoded = format!("{}[{}]", size / unit_length, unit);
            if encoded.len() < best.len()
                || (encoded.len() == best.len() && encoded < best)
            {
                best = encoded;
            }
        }
        best
    }

    pub fn encode(s: String) -> String {
        let length = s.len();
        let mut dp = vec![String::new(); length + 1];
        for index in 1..=length {
            dp[index] = Self::encode_word(&s[..index]);
            for split in 1..index {
                let candidate =
                    format!("{}{}", dp[index - split], Self::encode_word(&s[index - split..index]));
                if candidate.len() < dp[index].len()
                    || (candidate.len() == dp[index].len() && candidate < dp[index])
                {
                    dp[index] = candidate;
                }
            }
        }
        dp[length].clone()
    }
}
