// LeetCode 2375 - Construct Smallest Number From DI String
// https://leetcode.com/problems/construct-smallest-number-from-di-string/

impl Solution {
    pub fn smallest_number(pattern: String) -> String {
        let n = pattern.len();
        let mut ans: Vec<u8> = (0..=n).map(|i| b'1' + i as u8).collect();
        let p = pattern.as_bytes();
        let mut i = 0;
        while i < n {
            if p[i] == b'I' {
                i += 1;
                continue;
            }
            let mut j = i;
            while j < n && p[j] == b'D' {
                j += 1;
            }
            ans[i..=j].reverse();
            i = j;
        }
        String::from_utf8(ans).unwrap()
    }
}
