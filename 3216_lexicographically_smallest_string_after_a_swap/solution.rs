// LeetCode 3216 - Lexicographically Smallest String After a Swap
// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

impl Solution {
    pub fn get_smallest_string(s: String) -> String {
        let mut b = s.into_bytes();
        let n = b.len();
        for i in 1..n {
            let a = b[i - 1];
            let c = b[i];
            if a > c && a % 2 == c % 2 {
                b.swap(i - 1, i);
                return String::from_utf8(b).unwrap();
            }
        }
        String::from_utf8(b).unwrap()
    }
}
