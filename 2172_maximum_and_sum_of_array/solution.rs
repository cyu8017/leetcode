// LeetCode 2172 - Maximum AND Sum of Array
// https://leetcode.com/problems/maximum-and-sum-of-array/

impl Solution {
    pub fn maximum_and_sum(nums: Vec<i32>, num_slots: i32) -> i32 {
        let n = nums.len();
        let slots = num_slots as usize;
        let mut max_mask = 1;
        for _ in 0..slots {
            max_mask *= 3;
        }
        let mut dp = vec![0i32; max_mask];
        for mask in 0..max_mask {
            let mut cnt = 0;
            let mut x = mask;
            while x > 0 {
                cnt += x % 3;
                x /= 3;
            }
            if cnt >= n {
                continue;
            }
            let v = nums[cnt];
            let mut base = 1;
            for s in 1..=slots {
                let occ = (mask / base) % 3;
                if occ < 2 {
                    let nm = mask + base;
                    dp[nm] = dp[nm].max(dp[mask] + (v & s as i32));
                }
                base *= 3;
            }
        }
        *dp.iter().max().unwrap()
    }
}
