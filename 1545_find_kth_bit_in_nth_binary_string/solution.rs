// LeetCode 1545 - Find Kth Bit in Nth Binary String
// https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

impl Solution {
    pub fn find_kth_bit(n: i32, mut k: i32) -> char {
        let mut invert = false;
        let mut length = (1 << n) - 1;
        while k != 1 {
            let middle = length / 2 + 1;
            if k == middle {
                return if invert { '0' } else { '1' };
            }
            if k > middle {
                k = length - k + 1;
                invert = !invert;
            }
            length /= 2;
        }
        if invert { '1' } else { '0' }
    }
}
