// LeetCode 3757 - Number of Effective Subsequences
// https://leetcode.com/problems/number-of-effective-subsequences/

impl Solution {
    pub fn count_effective_subsequences(nums: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut all = 0;
        for &x in &nums {
            all |= x;
        }
        let mut bits = Vec::new();
        for b in 0..20 {
            if (all >> b) & 1 == 1 {
                bits.push(b);
            }
        }
        let m = bits.len();
        let mut freq = vec![0i32; 1 << m];
        for &x in &nums {
            let mut mask = 0;
            for (i, &bit) in bits.iter().enumerate() {
                if (x >> bit) & 1 == 1 {
                    mask |= 1 << i;
                }
            }
            freq[mask] += 1;
        }
        let mut disjoint = freq;
        for b in 0..m {
            for mask in 0..(1 << m) {
                if (mask >> b) & 1 == 1 {
                    disjoint[mask] += disjoint[mask ^ (1 << b)];
                }
            }
        }
        let mut pow2 = vec![0i32; nums.len() + 1];
        pow2[0] = 1;
        for i in 1..=nums.len() {
            pow2[i] = ((pow2[i - 1] as i64 * 2) % MOD as i64) as i32;
        }
        let mut ans = 0;
        let full = (1 << m) - 1;
        for s in 1..=full {
            let ways = pow2[disjoint[full ^ s] as usize];
            let bc = s.count_ones();
            if bc & 1 == 1 {
                ans += ways;
                if ans >= MOD {
                    ans -= MOD;
                }
            } else {
                ans -= ways;
                if ans < 0 {
                    ans += MOD;
                }
            }
        }
        ans
    }
}
