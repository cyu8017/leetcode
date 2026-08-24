// LeetCode 2645 - Minimum Additions to Make Valid String
// https://leetcode.com/problems/minimum-additions-to-make-valid-string/

impl Solution {
    pub fn add_minimum(word: String) -> i32 {
        let bytes = word.as_bytes();
        let mut ans = 0;
        let mut expect = 0;
        let mut i = 0;
        let n = bytes.len();
        while i < n {
            let need = b'a' + expect;
            if bytes[i] == need {
                i += 1;
            } else {
                ans += 1;
            }
            expect = (expect + 1) % 3;
        }
        ans += (3 - expect) % 3;
        ans
    }
}
