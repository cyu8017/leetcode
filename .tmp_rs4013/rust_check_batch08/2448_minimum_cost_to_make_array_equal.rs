struct Solution;
// LeetCode 2448 - Minimum Cost to Make Array Equal
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/

impl Solution {
    pub fn min_cost(nums: Vec<i32>, cost: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut idx: Vec<usize> = (0..n).collect();
        idx.sort_by_key(|&i| nums[i]);
        let total_cost: i64 = cost.iter().map(|&c| c as i64).sum();
        let mut pref = 0i64;
        let mut median = 0;
        for &i in &idx {
            pref += cost[i] as i64;
            if pref * 2 >= total_cost {
                median = nums[i];
                break;
            }
        }
        let mut ans = 0i64;
        for i in 0..n {
            let mut diff = nums[i] as i64 - median as i64;
            if diff < 0 {
                diff = -diff;
            }
            ans += diff * cost[i] as i64;
        }
        ans
    }
}

fn main() {}
