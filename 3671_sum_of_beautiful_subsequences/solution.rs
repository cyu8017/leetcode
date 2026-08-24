// LeetCode 3671 - Sum of Beautiful Subsequences
// https://leetcode.com/problems/sum-of-beautiful-subsequences/

impl Solution {
    pub fn total_beauty(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mx = nums.iter().copied().max().unwrap_or(0) as usize;
        let mut pos = vec![Vec::new(); mx + 1];
        for (i, &v) in nums.iter().enumerate() {
            pos[v as usize].push(i);
        }
        let mut cnt = vec![0i32; mx + 1];
        for g in 1..=mx {
            let mut seq = Vec::new();
            let mut m = g;
            while m <= mx {
                seq.extend_from_slice(&pos[m]);
                m += g;
            }
            if seq.is_empty() {
                continue;
            }
            seq.sort_unstable();
            let mut ways = 1i64;
            for _ in 0..seq.len() {
                ways = (ways * 2) % MOD;
            }
            cnt[g] = ((ways - 1 + MOD) % MOD) as i32;
        }
        let mut ans = 0i64;
        for g in (1..=mx).rev() {
            let mut m = 2 * g;
            while m <= mx {
                cnt[g] = ((cnt[g] as i64 - cnt[m] as i64 + MOD) % MOD) as i32;
                m += g;
            }
            ans = (ans + cnt[g] as i64 * g as i64) % MOD;
        }
        ans as i32
    }
}
