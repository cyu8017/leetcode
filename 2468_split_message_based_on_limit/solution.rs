// LeetCode 2468 - Split Message Based on Limit
// https://leetcode.com/problems/split-message-based-on-limit/

impl Solution {
    pub fn split_message(message: String, limit: i32) -> Vec<String> {
        let n = message.len();
        let bytes = message.as_bytes();
        for parts in 1..=n {
            let sb_digits = parts.to_string().len();
            let mut ok = true;
            let mut idx = 0;
            let mut res = Vec::new();
            for i in 1..=parts {
                let tail = 3 + i.to_string().len() + sb_digits;
                let cap = limit as isize - tail as isize;
                if cap <= 0 || idx >= n {
                    ok = false;
                    break;
                }
                let mut take = cap as usize;
                if take > n - idx {
                    take = n - idx;
                }
                let mut part = String::from_utf8(bytes[idx..idx + take].to_vec()).unwrap();
                part.push_str(&format!("<{}/{}>", i, parts));
                res.push(part);
                idx += take;
            }
            if ok && idx == n {
                return res;
            }
        }
        vec![]
    }
}
