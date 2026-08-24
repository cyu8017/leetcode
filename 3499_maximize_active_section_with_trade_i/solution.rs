// LeetCode 3499 - Maximize Active Section with Trade I
// https://leetcode.com/problems/maximize-active-section-with-trade-i/

impl Solution {
    pub fn max_active_sections_after_trade(s: String) -> i32 {
        let ones = s.bytes().filter(|&c| c == b'1').count() as i32;
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut zeros = Vec::new();
        let mut i = 0;
        while i < n {
            if bytes[i] != b'0' {
                i += 1;
                continue;
            }
            let mut j = i;
            while j < n && bytes[j] == b'0' {
                j += 1;
            }
            zeros.push((i, j - 1));
            i = j;
        }
        let mut best = 0;
        for i in 0..zeros.len().saturating_sub(1) {
            let gain = (zeros[i].1 - zeros[i].0 + 1) + (zeros[i + 1].1 - zeros[i + 1].0 + 1);
            if gain as i32 > best {
                best = gain as i32;
            }
        }
        ones + best
    }
}
