struct Solution;
// LeetCode 3251 - Find the Count of Monotonic Pairs II
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/

impl Solution {
    pub fn count_of_pairs(nums: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = nums.len();
        let max_v = *nums.iter().max().unwrap() as usize;
        let mut dp = vec![0; max_v + 1];
        for a in 0..=nums[0] as usize {
            dp[a] = 1;
        }
        for i in 1..n {
            let mut ndp = vec![0; max_v + 1];
            let mut pref = vec![0; max_v + 2];
            for a in 0..=max_v {
                pref[a + 1] = (pref[a] + dp[a]) % MOD;
            }
            for a2 in 0..=nums[i] as usize {
                let b2 = nums[i] - a2 as i32;
                let mut max_a1 = a2 as i32;
                let lim = nums[i - 1] - b2;
                if lim < max_a1 {
                    max_a1 = lim;
                }
                if max_a1 < 0 {
                    continue;
                }
                if max_a1 > max_v as i32 {
                    max_a1 = max_v as i32;
                }
                ndp[a2] = pref[(max_a1 + 1) as usize];
            }
            dp = ndp;
        }
        let mut ans = 0;
        for v in dp {
            ans = (ans + v) % MOD;
        }
        ans
    }
}

fn main() {}
