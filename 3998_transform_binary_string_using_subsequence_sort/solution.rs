// LeetCode 3998 - Transform Binary String Using Subsequence Sort
// https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/

impl Solution {
    pub fn transform_str(s: String, strs: Vec<String>) -> Vec<bool> {
        let s = s.as_bytes();
        let n = s.len();
        let mut prefix = vec![0; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + if s[i] == b'1' { 1 } else { 0 };
        }
        let mut result = vec![false; strs.len()];
        for (i, st) in strs.iter().enumerate() {
            let t = st.as_bytes();
            let mut left = 0;
            let mut right = 0;
            let mut ok = true;
            for j in 0..n {
                left += if t[j] == b'1' { 1 } else { 0 };
                let add = if t[j] != b'0' { 1 } else { 0 };
                right += add;
                if right > prefix[j + 1] {
                    right = prefix[j + 1];
                }
                if left > right {
                    ok = false;
                    break;
                }
            }
            result[i] = ok && left <= prefix[n] && prefix[n] <= right;
        }
        result
    }
}
