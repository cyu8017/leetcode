// LeetCode 3681 - Maximum XOR of Subsequences
// https://leetcode.com/problems/maximum-xor-of-subsequences/

impl Solution {
    pub fn max_xor_subsequences(nums: Vec<i32>) -> i32 {
        let mut basis = [0i32; 32];
        for x in nums {
            let mut cur = x;
            for b in (0..32).rev() {
                if (cur & (1 << b)) == 0 {
                    continue;
                }
                if basis[b] == 0 {
                    basis[b] = cur;
                    break;
                }
                cur ^= basis[b];
            }
        }
        let mut ans = 0;
        for b in (0..32).rev() {
            if (ans ^ basis[b]) > ans {
                ans ^= basis[b];
            }
        }
        ans
    }
}
