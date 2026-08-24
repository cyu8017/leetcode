// LeetCode 3006 - Find Beautiful Indices in the Given Array I
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

impl Solution {
    pub fn beautiful_indices(s: String, a: String, b: String, k: i32) -> Vec<i32> {
        fn build_lps(pattern: &[u8]) -> Vec<i32> {
            let s_l = pattern.len();
            let mut lps = vec![0; s_l];
            let mut l = 0;
            let mut i = 1;
            while i < s_l {
                if pattern[i] == pattern[l] {
                    l += 1;
                    lps[i] = l as i32;
                    i += 1;
                } else if l != 0 {
                    l = lps[l - 1] as usize;
                } else {
                    lps[i] = l as i32;
                    i += 1;
                }
            }
            lps
        }
        fn kmp(s: &[u8], pat: &[u8], lps: &[i32]) -> Vec<i32> {
            let s_len = s.len();
            let pat_l = pat.len();
            let mut index = Vec::new();
            let mut i = 0;
            let mut j = 0;
            while i <= s_len && j <= pat_l && s_len - i >= pat_l - j {
                if s[i] == pat[j] {
                    i += 1;
                    j += 1;
                }
                if j == pat_l {
                    index.push((i - pat_l) as i32);
                    j = lps[j - 1] as usize;
                } else if i < s_len && s[i] != pat[j] {
                    if j != 0 {
                        j = lps[j - 1] as usize;
                    } else {
                        i += 1;
                    }
                }
            }
            index
        }
        let sb = s.as_bytes();
        let ab = a.as_bytes();
        let bb = b.as_bytes();
        if ab.is_empty() || bb.is_empty() {
            return vec![];
        }
        let lps_a = build_lps(ab);
        let lps_b = build_lps(bb);
        let a_index = kmp(sb, ab, &lps_a);
        let b_index = kmp(sb, bb, &lps_b);
        let mut final_v = Vec::new();
        let mut i = 0;
        let mut j = 0;
        while i < a_index.len() && j < b_index.len() {
            if a_index[i] + k >= b_index[j] && a_index[i] - k <= b_index[j] {
                final_v.push(a_index[i]);
                i += 1;
            } else if a_index[i] - k > b_index[j] {
                j += 1;
            } else {
                i += 1;
            }
        }
        final_v
    }
}
