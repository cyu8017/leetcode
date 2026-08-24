// LeetCode 3877 - Minimum Removals to Achieve Target XOR
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

impl Solution {
    pub fn min_removals(nums: Vec<i32>, target: i32) -> i32 {
        let mx = *nums.iter().max().unwrap();
        let mut m = 0;
        if mx > 0 {
            let mut u = mx as u32;
            while u > 0 {
                m += 1;
                u >>= 1;
            }
        }
        if (1 << m) <= target {
            return -1;
        }
        let n = nums.len();
        let nmask = 1 << m;
        let mut f = vec![vec![i32::MIN; nmask]; n + 1];
        f[0][0] = 0;
        for i in 1..=n {
            let x = nums[i - 1] as usize;
            for j in 0..nmask {
                f[i][j] = f[i - 1][j];
                if f[i - 1][j ^ x] != i32::MIN {
                    f[i][j] = f[i][j].max(f[i - 1][j ^ x] + 1);
                }
            }
        }
        if f[n][target as usize] < 0 {
            return -1;
        }
        n as i32 - f[n][target as usize]
    }
}
