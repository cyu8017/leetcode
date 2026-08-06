// LeetCode 1994 - The Number of Good Subsets
// https://leetcode.com/problems/the-number-of-good-subsets/

impl Solution {
    pub fn number_of_good_subsets(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];
        let mut masks = [0i32; 31];
        for x in 2..31 {
            let mut m = 0i32;
            let mut y = x;
            let mut ok = true;
            for (i, &p) in primes.iter().enumerate() {
                if y % p == 0 {
                    if (y / p) % p == 0 {
                        ok = false;
                        break;
                    }
                    m |= 1 << i;
                    y /= p;
                }
            }
            masks[x] = if ok { m } else { -1 };
        }

        let mut cnt = [0i64; 31];
        for &v in &nums {
            cnt[v as usize] += 1;
        }

        let mut dp = vec![0i64; 1 << primes.len()];
        dp[0] = 1;
        for x in 2..31 {
            if cnt[x] == 0 || masks[x] < 0 {
                continue;
            }
            let m = masks[x] as usize;
            for state in (0..(1 << primes.len())).rev() {
                if state & m != 0 {
                    continue;
                }
                dp[state | m] = (dp[state | m] + dp[state] * cnt[x]) % MOD;
            }
        }

        let mut ans: i64 = dp[1..].iter().sum::<i64>() % MOD;
        let mut pow2 = 1i64;
        for _ in 0..cnt[1] {
            pow2 = (pow2 * 2) % MOD;
        }
        ans = ans * pow2 % MOD;
        ans as i32
    }
}
