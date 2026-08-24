// LeetCode 3139 - Minimum Cost to Equalize Array
// https://leetcode.com/problems/minimum-cost-to-equalize-array/

impl Solution {
    pub fn min_cost_to_equalize_array(nums: Vec<i32>, cost1: i32, cost2: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len() as i64;
        let mut min_num = nums[0];
        let mut max_num = nums[0];
        let mut sum = 0i64;
        for &v in &nums {
            min_num = min_num.min(v);
            max_num = max_num.max(v);
            sum += v as i64;
        }
        if cost1 as i64 * 2 <= cost2 as i64 || n < 3 {
            let total_gap = max_num as i64 * n - sum;
            return (cost1 as i64 * total_gap % MOD) as i32;
        }
        let mut ans = i64::MAX;
        for target in max_num..2 * max_num {
            let max_gap = (target - min_num) as i64;
            let total_gap = target as i64 * n - sum;
            let mut pairs = total_gap / 2;
            let alt = total_gap - max_gap;
            if alt < pairs {
                pairs = alt;
            }
            let cost = cost1 as i64 * (total_gap - 2 * pairs) + cost2 as i64 * pairs;
            ans = ans.min(cost);
        }
        (ans % MOD) as i32
    }
}
