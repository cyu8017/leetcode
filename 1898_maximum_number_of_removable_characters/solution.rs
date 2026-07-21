// LeetCode 1898 - Maximum Number of Removable Characters
// https://leetcode.com/problems/maximum-number-of-removable-characters/

impl Solution {
    pub fn maximum_removals(s: String, p: String, removable: Vec<i32>) -> i32 {
        let s_bytes = s.as_bytes();
        let p_bytes = p.as_bytes();
        let still_subsequence = |k: usize| -> bool {
            let mut removed = vec![false; s_bytes.len()];
            for &idx in &removable[..k] {
                removed[idx as usize] = true;
            }
            let mut index = 0usize;
            for (position, &ch) in s_bytes.iter().enumerate() {
                if removed[position] {
                    continue;
                }
                if index < p_bytes.len() && ch == p_bytes[index] {
                    index += 1;
                }
            }
            index == p_bytes.len()
        };
        let mut lo = 0usize;
        let mut hi = removable.len();
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if still_subsequence(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo as i32
    }
}
