// LeetCode 1663 - Smallest String With A Given Numeric Value
// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

impl Solution {
    pub fn get_smallest_string(n: i32, k: i32) -> String {
        let mut a = vec![b'a'; n as usize];
        let mut k = k - n;
        for i in (0..n as usize).rev() {
            let d = 25.min(k);
            a[i] = b'a' + d as u8;
            k -= d;
        }
        String::from_utf8(a).unwrap()
    }
}
