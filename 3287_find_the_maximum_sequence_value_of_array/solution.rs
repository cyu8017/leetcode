// LeetCode 3287 - Find the Maximum Sequence Value of Array
// https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

impl Solution {
    pub fn max_value(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k = k as usize;
        const MAX: usize = 128;
        let mut left = vec![vec![vec![0u8; MAX]; k + 1]; n + 1];
        left[0][0][0] = 1;
        for i in 0..n {
            for j in 0..=k {
                for v in 0..MAX {
                    if left[i][j][v] == 0 {
                        continue;
                    }
                    left[i + 1][j][v] = 1;
                    if j < k {
                        left[i + 1][j + 1][v | nums[i] as usize] = 1;
                    }
                }
            }
        }
        let mut right = vec![vec![vec![0u8; MAX]; k + 1]; n + 1];
        right[n][0][0] = 1;
        for i in (0..n).rev() {
            for j in 0..=k {
                for v in 0..MAX {
                    if right[i + 1][j][v] == 0 {
                        continue;
                    }
                    right[i][j][v] = 1;
                    if j < k {
                        right[i][j + 1][v | nums[i] as usize] = 1;
                    }
                }
            }
        }
        let mut ans = 0;
        let mut mid = k;
        while mid + k <= n {
            for a in 0..MAX {
                if left[mid][k][a] == 0 {
                    continue;
                }
                for b in 0..MAX {
                    if right[mid][k][b] != 0 && (a ^ b) > ans {
                        ans = a ^ b;
                    }
                }
            }
            mid += 1;
        }
        ans as i32
    }
}
