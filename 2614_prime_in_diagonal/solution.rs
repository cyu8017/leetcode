// LeetCode 2614 - Prime In Diagonal
// https://leetcode.com/problems/prime-in-diagonal/

impl Solution {
    pub fn diagonal_prime(nums: Vec<Vec<i32>>) -> i32 {
        fn is_prime(x: i32) -> bool {
            if x < 2 {
                return false;
            }
            let mut i = 2;
            while i * i <= x {
                if x % i == 0 {
                    return false;
                }
                i += 1;
            }
            true
        }
        let n = nums.len();
        let mut best = 0;
        for i in 0..n {
            for v in [nums[i][i], nums[i][n - 1 - i]] {
                if is_prime(v) && v > best {
                    best = v;
                }
            }
        }
        best
    }
}
