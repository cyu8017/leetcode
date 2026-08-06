// LeetCode 1247 - Minimum Swaps to Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

impl Solution {
    pub fn minimum_swap(s1: String, s2: String) -> i32 {
        let mut xy = 0;
        let mut yx = 0;
        for (a, b) in s1.bytes().zip(s2.bytes()) {
            if a == b'x' && b == b'y' {
                xy += 1;
            } else if a == b'y' && b == b'x' {
                yx += 1;
            }
        }
        if (xy + yx) % 2 != 0 {
            return -1;
        }
        xy / 2 + yx / 2 + 2 * (xy % 2)
    }
}
