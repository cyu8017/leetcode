// LeetCode 2937 - Make Three Strings Equal
// https://leetcode.com/problems/make-three-strings-equal/

impl Solution {
    pub fn find_minimum_operations(s1: String, s2: String, s3: String) -> i32 {
        let b1 = s1.as_bytes();
        let b2 = s2.as_bytes();
        let b3 = s3.as_bytes();
        let n = b1.len().min(b2.len()).min(b3.len());
        let mut i = 0;
        while i < n && b1[i] == b2[i] && b2[i] == b3[i] {
            i += 1;
        }
        if i == 0 {
            return -1;
        }
        (b1.len() + b2.len() + b3.len() - 3 * i) as i32
    }
}
