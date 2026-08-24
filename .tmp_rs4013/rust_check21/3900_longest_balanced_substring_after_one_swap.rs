struct Solution;
// LeetCode 3900 - Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

use std::collections::HashMap;

impl Solution {
    pub fn longest_balanced(s: String) -> i32 {
        let b = s.as_bytes();
        let cnt0 = b.iter().filter(|&&c| c == b'0').count() as i32;
        let cnt1 = b.len() as i32 - cnt0;
        let mut pos: HashMap<i32, Vec<i32>> = HashMap::new();
        pos.insert(0, vec![-1]);
        let mut ans = 0;
        let mut pre = 0;
        for (i, &c) in b.iter().enumerate() {
            if c == b'1' {
                pre += 1;
            } else {
                pre -= 1;
            }
            pos.entry(pre).or_default().push(i as i32);
            ans = ans.max(i as i32 - pos[&pre][0]);
            if let Some(p) = pos.get(&(pre - 2)) {
                if (i as i32 - p[0] - 2) / 2 < cnt0 {
                    ans = ans.max(i as i32 - p[0]);
                } else if p.len() > 1 {
                    ans = ans.max(i as i32 - p[1]);
                }
            }
            if let Some(p) = pos.get(&(pre + 2)) {
                if (i as i32 - p[0] - 2) / 2 < cnt1 {
                    ans = ans.max(i as i32 - p[0]);
                } else if p.len() > 1 {
                    ans = ans.max(i as i32 - p[1]);
                }
            }
        }
        ans
    }
}
