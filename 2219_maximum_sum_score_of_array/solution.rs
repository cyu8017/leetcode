// LeetCode 2219 - Maximum Sum Score of Array
// https://leetcode.com/problems/maximum-sum-score-of-array/

impl Solution {
    pub fn maximum_sum_score(nums: Vec<i32>) -> i64 {
        let total: i64 = nums.iter().map(|&x| x as i64).sum();
        let mut pref = 0i64;
        let mut ans = i64::MIN;
        for x in nums {
            pref += x as i64;
            ans = ans.max(pref.max(total - pref + x as i64));
        }
        ans
    }
}
