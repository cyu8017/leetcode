// LeetCode 3163 - String Compression III
// https://leetcode.com/problems/string-compression-iii/

impl Solution {
    pub fn compressed_string(word: String) -> String {
        let b = word.as_bytes();
        let n = b.len();
        let mut ans = String::new();
        let mut i = 0;
        while i < n {
            let mut j = i + 1;
            while j < n && b[j] == b[i] {
                j += 1;
            }
            let mut k = j - i;
            while k > 0 {
                let x = 9.min(k);
                ans.push((b'0' + x as u8) as char);
                ans.push(b[i] as char);
                k -= x;
            }
            i = j;
        }
        ans
    }
}
