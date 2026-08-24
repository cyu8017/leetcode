// LeetCode 2182 - Construct String With Repeat Limit
// https://leetcode.com/problems/construct-string-with-repeat-limit/

impl Solution {
    pub fn repeat_limited_string(s: String, repeat_limit: i32) -> String {
        let mut freq = [0i32; 26];
        for c in s.bytes() {
            freq[(c - b'a') as usize] += 1;
        }
        let mut ans = String::new();
        loop {
            let mut placed = false;
            for c in (0..26).rev() {
                if freq[c] == 0 {
                    continue;
                }
                if !ans.is_empty() && ans.as_bytes()[ans.len() - 1] - b'a' == c as u8 {
                    let mut found = false;
                    for d in (0..c).rev() {
                        if freq[d] > 0 {
                            ans.push((b'a' + d as u8) as char);
                            freq[d] -= 1;
                            found = true;
                            placed = true;
                            break;
                        }
                    }
                    if !found {
                        return ans;
                    }
                    break;
                }
                let use_n = freq[c].min(repeat_limit);
                for _ in 0..use_n {
                    ans.push((b'a' + c as u8) as char);
                }
                freq[c] -= use_n;
                placed = true;
                break;
            }
            if !placed {
                break;
            }
        }
        ans
    }
}
