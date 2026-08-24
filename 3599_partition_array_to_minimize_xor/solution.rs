// LeetCode 3599 - Partition Array to Minimize XOR
// https://leetcode.com/problems/partition-array-to-minimize-xor/

impl Solution {
    pub fn min_xor(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k = k as usize;
        let mut g = vec![0; n + 1];
        for i in 1..=n {
            g[i] = g[i - 1] ^ nums[i - 1];
        }
        let inf = i32::MAX / 2;
        let mut f = vec![vec![inf; k + 1]; n + 1];
        f[0][0] = 0;
        for i in 1..=n {
            for j in 1..=i.min(k) {
                for h in (j - 1)..i {
                    f[i][j] = f[i][j].min(f[h][j - 1].max(g[i] ^ g[h]));
                }
            }
        }
        f[n][k]
    }
}
