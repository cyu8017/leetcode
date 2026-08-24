// LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
// https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

impl Solution {
    pub fn max_sum(nums: Vec<i32>, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut cnt = [0i32; 32];
        for v in nums {
            for b in 0..32 {
                if (v & (1 << b)) != 0 {
                    cnt[b] += 1;
                }
            }
        }
        let mut ans = 0i64;
        for _ in 0..k {
            let mut cur = 0i32;
            for b in 0..32 {
                if cnt[b] > 0 {
                    cur |= 1 << b;
                    cnt[b] -= 1;
                }
            }
            let c = (cur as i64) % MOD;
            ans = (ans + c * c % MOD) % MOD;
        }
        ans as i32
    }
}
