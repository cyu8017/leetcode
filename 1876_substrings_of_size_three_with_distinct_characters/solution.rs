// LeetCode 1876 - Substrings of Size Three with Distinct Characters
// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

impl Solution {
    pub fn count_good_substrings(s: String) -> i32 {
        if s.len() < 3 {
            return 0;
        }
        let bytes = s.as_bytes();
        let mut count = 0;
        for i in 0..bytes.len() - 2 {
            let a = bytes[i];
            let b = bytes[i + 1];
            let c = bytes[i + 2];
            if a != b && b != c && a != c {
                count += 1;
            }
        }
        count
    }
}
