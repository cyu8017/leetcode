// LeetCode 0923 - 3Sum With Multiplicity
// https://leetcode.com/problems/3sum-with-multiplicity/

impl Solution {
    pub fn three_sum_multi(arr: Vec<i32>, target: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut count = [0i64; 101];
        for x in arr {
            count[x as usize] += 1;
        }
        let mut ans = 0i64;
        for a in 0..=100 {
            if count[a] == 0 {
                continue;
            }
            for b in a..=100 {
                if count[b] == 0 {
                    continue;
                }
                let c = target - a as i32 - b as i32;
                if c < b as i32 || c > 100 || count[c as usize] == 0 {
                    continue;
                }
                let c = c as usize;
                if a == b && b == c {
                    ans += count[a] * (count[a] - 1) * (count[a] - 2) / 6;
                } else if a == b {
                    ans += count[a] * (count[a] - 1) / 2 * count[c];
                } else if b == c {
                    ans += count[a] * count[b] * (count[b] - 1) / 2;
                } else {
                    ans += count[a] * count[b] * count[c];
                }
            }
        }
        (ans % MOD) as i32
    }
}
