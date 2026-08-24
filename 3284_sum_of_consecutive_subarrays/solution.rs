// LeetCode 3284 - Sum of Consecutive Subarrays
// https://leetcode.com/problems/sum-of-consecutive-subarrays/

impl Solution {
    pub fn range_sum(nums: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = nums.len();
        let mut ans = 0;
        let mut i = 0;
        while i < n {
            let mut j = i;
            while j + 1 < n && (nums[j + 1] == nums[j] + 1 || nums[j + 1] == nums[j] - 1) {
                j += 1;
            }
            for l in i..=j {
                let mut s = 0;
                for r in l..=j {
                    s += nums[r];
                    ans = (ans + s) % MOD;
                }
            }
            i = j + 1;
        }
        ans
    }
}
