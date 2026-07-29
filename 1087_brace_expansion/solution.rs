// LeetCode 1087 - Brace Expansion
// https://leetcode.com/problems/brace-expansion/

impl Solution {
    pub fn expand(s: String) -> Vec<String> {
        let bytes = s.as_bytes();
        let mut groups: Vec<Vec<String>> = Vec::new();
        let mut i = 0;
        while i < bytes.len() {
            if bytes[i] == b'{' {
                let mut j = i + 1;
                while bytes[j] != b'}' {
                    j += 1;
                }
                let mut opts: Vec<String> = s[i + 1..j]
                    .split(',')
                    .map(|x| x.to_string())
                    .collect();
                opts.sort();
                groups.push(opts);
                i = j + 1;
            } else {
                groups.push(vec![s[i..=i].to_string()]);
                i += 1;
            }
        }
        let mut ans = vec![String::new()];
        for group in groups {
            let mut next = Vec::new();
            for prefix in &ans {
                for ch in &group {
                    next.push(format!("{}{}", prefix, ch));
                }
            }
            ans = next;
        }
        ans
    }
}
