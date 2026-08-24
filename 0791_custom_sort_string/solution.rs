// LeetCode 0791 - Custom Sort String
// https://leetcode.com/problems/custom-sort-string/

impl Solution {
    pub fn custom_sort_string(order: String, s: String) -> String {
        let mut counts = [0i32; 26];
        for ch in s.bytes() {
            counts[(ch - b'a') as usize] += 1;
        }
        let mut parts = String::new();
        for ch in order.bytes() {
            let idx = (ch - b'a') as usize;
            while counts[idx] > 0 {
                parts.push(ch as char);
                counts[idx] -= 1;
            }
        }
        for i in 0..26 {
            while counts[i] > 0 {
                parts.push((b'a' + i as u8) as char);
                counts[i] -= 1;
            }
        }
        parts
    }
}
