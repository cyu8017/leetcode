// LeetCode 2184 - Number of Ways to Build Sturdy Brick Wall
// https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

impl Solution {
    pub fn build_wall(height: i32, width: i32, bricks: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut masks = Vec::new();
        fn gen(remain: i32, mask: i32, bricks: &[i32], masks: &mut Vec<i32>) {
            if remain == 0 {
                masks.push(mask);
                return;
            }
            for &b in bricks {
                if b <= remain {
                    let mut nm = mask;
                    if remain - b > 0 {
                        nm |= 1 << (remain - b);
                    }
                    gen(remain - b, nm, bricks, masks);
                }
            }
        }
        gen(width, 0, &bricks, &mut masks);
        let m = masks.len();
        let mut compat = vec![Vec::new(); m];
        for i in 0..m {
            for j in 0..m {
                if (masks[i] & masks[j]) == 0 {
                    compat[i].push(j);
                }
            }
        }
        let mut dp = vec![1i32; m];
        for _ in 1..height {
            let mut ndp = vec![0i32; m];
            for i in 0..m {
                for &j in &compat[i] {
                    ndp[j] = (ndp[j] + dp[i]) % MOD;
                }
            }
            dp = ndp;
        }
        dp.iter().fold(0, |a, &v| (a + v) % MOD)
    }
}
