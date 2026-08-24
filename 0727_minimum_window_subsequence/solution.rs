// LeetCode 0727 - Minimum Window Subsequence
// https://leetcode.com/problems/minimum-window-subsequence/

impl Solution {
    pub fn min_window(s1: String, s2: String) -> String {
        let s1: Vec<char> = s1.chars().collect();
        let s2: Vec<char> = s2.chars().collect();
        let m = s1.len();
        let n = s2.len();
        let mut best = String::new();
        let mut i = 0;
        while i < m {
            let mut j = 0;
            let mut k = i;
            while k < m && j < n {
                if s1[k] == s2[j] {
                    j += 1;
                }
                k += 1;
            }
            if j < n {
                break;
            }
            let end = k - 1;
            j = n - 1;
            k = end;
            while j != usize::MAX {
                if s1[k] == s2[j] {
                    j = j.wrapping_sub(1);
                }
                k = k.wrapping_sub(1);
            }
            let start = k.wrapping_add(1);
            if best.is_empty() || end - start + 1 < best.len() {
                best = s1[start..=end].iter().collect();
            }
            i = start + 1;
        }
        best
    }
}
