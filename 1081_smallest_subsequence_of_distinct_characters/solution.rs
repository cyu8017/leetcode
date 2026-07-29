// LeetCode 1081 - Smallest Subsequence of Distinct Characters
// https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

impl Solution {
    pub fn smallest_subsequence(s: String) -> String {
        let bytes = s.as_bytes();
        let mut last = [0usize; 26];
        for (i, &ch) in bytes.iter().enumerate() {
            last[(ch - b'a') as usize] = i;
        }
        let mut stack: Vec<u8> = Vec::new();
        let mut used = [false; 26];
        for (i, &ch) in bytes.iter().enumerate() {
            let idx = (ch - b'a') as usize;
            if used[idx] {
                continue;
            }
            while let Some(&top) = stack.last() {
                let top_idx = (top - b'a') as usize;
                if ch < top && last[top_idx] > i {
                    stack.pop();
                    used[top_idx] = false;
                } else {
                    break;
                }
            }
            stack.push(ch);
            used[idx] = true;
        }
        String::from_utf8(stack).unwrap()
    }
}
