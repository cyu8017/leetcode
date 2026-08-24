// LeetCode 3703 - Remove K-Balanced Substrings
// https://leetcode.com/problems/remove-k-balanced-substrings/

impl Solution {
    pub fn remove_substring(s: String, k: i32) -> String {
        let mut stk: Vec<(char, i32)> = Vec::new();
        for c in s.chars() {
            if stk.last().map(|p| p.0) == Some(c) {
                stk.last_mut().unwrap().1 += 1;
            } else {
                stk.push((c, 1));
            }
            if c == ')' && stk.len() > 1 {
                let n = stk.len();
                if stk[n - 1].1 == k && stk[n - 2].1 >= k {
                    stk.pop();
                    if let Some(prev) = stk.last_mut() {
                        prev.1 -= k;
                    }
                    if stk.last().map(|p| p.1) == Some(0) {
                        stk.pop();
                    }
                }
            }
        }
        let mut res = String::new();
        for (ch, count) in stk {
            for _ in 0..count {
                res.push(ch);
            }
        }
        res
    }
}
