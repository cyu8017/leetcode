// LeetCode 3699 - Number of ZigZag Arrays I
// https://leetcode.com/problems/number-of-zigzag-arrays-i/

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
            let mut pref_down = vec![0; m + 1];
            for j in 0..m {
                pref_down[j + 1] = (pref_down[j] + down[j]) % MOD;
            }
            let mut nup = vec![0; m];
            for j in 0..m {
                nup[j] = pref_down[j];
            }
            let mut suf_up = vec![0; m + 1];
            for j in (0..m).rev() {
                suf_up[j] = (suf_up[j + 1] + up[j]) % MOD;
            }
            let mut ndown = vec![0; m];
            for j in 0..m {
                ndown[j] = suf_up[j + 1];
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
