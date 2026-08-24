// LeetCode 3444 - Minimum Increments for Target Multiples in an Array
// https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

impl Solution {
    fn gcd(mut a: i32, mut b: i32) -> i32 {
        while b != 0 {
            let t = a % b;
            a = b;
            b = t;
        }
        a
    }

    fn lcm(a: i32, b: i32) -> i32 {
        a / Self::gcd(a, b) * b
    }

    pub fn minimum_increments(nums: Vec<i32>, target: Vec<i32>) -> i32 {
        let m = target.len();
        let nmask = 1 << m;
        const INF: i64 = 1e18 as i64;
        let mut dp = vec![INF; nmask];
        dp[0] = 0;
        for x in nums {
            let mut ndp = dp.clone();
            for mask in 0..nmask {
                for sub in 1..nmask {
                    let mut l = 1i32;
                    let mut ok = true;
                    for i in 0..m {
                        if sub & (1 << i) != 0 {
                            l = Self::lcm(l, target[i]);
                            if l > 1_000_000_000 {
                                ok = false;
                                break;
                            }
                        }
                    }
                    if !ok {
                        continue;
                    }
                    let cost = (l - x % l) % l;
                    let nm = mask | sub;
                    if dp[mask] + (cost as i64) < ndp[nm] {
                        ndp[nm] = dp[mask] + cost as i64;
                    }
                }
            }
            dp = ndp;
        }
        dp[nmask - 1] as i32
    }
}
