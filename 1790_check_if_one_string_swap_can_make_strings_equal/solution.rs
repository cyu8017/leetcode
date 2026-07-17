// LeetCode 1790 - Check if One String Swap Can Make Strings Equal
// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

impl Solution {
    pub fn are_almost_equal(s1: String, s2: String) -> bool {
        let a = s1.as_bytes();
        let b = s2.as_bytes();
        let diff: Vec<usize> = (0..a.len()).filter(|&i| a[i] != b[i]).collect();
        diff.is_empty()
            || (diff.len() == 2 && a[diff[0]] == b[diff[1]] && a[diff[1]] == b[diff[0]])
    }
}
