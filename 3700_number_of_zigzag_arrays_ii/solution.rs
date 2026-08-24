// LeetCode 3700 - Number of ZigZag Arrays II
// https://leetcode.com/problems/number-of-zigzag-arrays-ii/

impl Solution {
    pub fn zig_zag_arrays(n: i32, l: i32, r: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let m = (r - l + 1) as usize;
        if n == 1 {
            return (m as i32) % MOD;
        }
        let mut up = vec![1; m];
        let mut down = vec![1; m];
        for _ in 2..=n {
            let mut pref = vec![0; m + 1];
            for j in 0..m {
                pref[j + 1] = (pref[j] + down[j]) % MOD;
            }
            let mut nup = vec![0; m];
            for j in 0..m {
                nup[j] = pref[j];
            }
            let mut suf = vec![0; m + 1];
            for j in (0..m).rev() {
                suf[j] = (suf[j + 1] + up[j]) % MOD;
            }
            let mut ndown = vec![0; m];
            for j in 0..m {
                ndown[j] = suf[j + 1];
            }
            up = nup;
            down = ndown;
        }
        let mut ans = 0;
        for j in 0..m {
            ans = (ans + up[j]) % MOD;
            ans = (ans + down[j]) % MOD;
        }
        ans
    }
}
