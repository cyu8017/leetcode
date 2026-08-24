// LeetCode 2138 - Divide a String Into Groups of Size k
// https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

impl Solution {
    pub fn divide_string(s: String, k: i32, fill: char) -> Vec<String> {
        let k = k as usize;
        let mut ans = Vec::new();
        let mut i = 0;
        let b = s.as_bytes();
        while i < b.len() {
            if i + k <= b.len() {
                ans.push(s[i..i + k].to_string());
            } else {
                let mut chunk = s[i..].to_string();
                while chunk.len() < k {
                    chunk.push(fill);
                }
                ans.push(chunk);
            }
            i += k;
        }
        ans
    }
}
