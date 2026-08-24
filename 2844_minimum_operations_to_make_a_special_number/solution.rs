// LeetCode 2844 - Minimum Operations to Make a Special Number
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

impl Solution {
    pub fn minimum_operations(num: String) -> i32 {
        let n = num.len() as i32;
        let bytes = num.as_bytes();
        let mut ans = n;
        if bytes.contains(&b'0') {
            ans = ans.min(n - 1);
        }
        for t in [b"00", b"25", b"50", b"75"] {
            let mut j = n - 1;
            while j >= 0 && bytes[j as usize] != t[1] {
                j -= 1;
            }
            if j < 0 {
                continue;
            }
            let mut i = j - 1;
            while i >= 0 && bytes[i as usize] != t[0] {
                i -= 1;
            }
            if i < 0 {
                continue;
            }
            ans = ans.min(n - i - 2);
        }
        ans
    }
}
