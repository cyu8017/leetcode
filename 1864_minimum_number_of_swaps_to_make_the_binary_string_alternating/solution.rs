// LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

impl Solution {
    pub fn min_swaps(s: String) -> i32 {
        let zeros = s.bytes().filter(|&b| b == b'0').count() as i32;
        let ones = s.len() as i32 - zeros;
        if (zeros - ones).abs() > 1 {
            return -1;
        }
        let mismatches = |pattern: &[u8; 2]| -> i32 {
            s.bytes()
                .enumerate()
                .filter(|(i, ch)| *ch != pattern[i % 2])
                .count() as i32
                / 2
        };
        if zeros == ones {
            mismatches(b"01").min(mismatches(b"10"))
        } else if zeros > ones {
            mismatches(b"01")
        } else {
            mismatches(b"10")
        }
    }
}
