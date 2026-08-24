// LeetCode 2036 - Maximum Alternating Subarray Sum
// https://leetcode.com/problems/maximum-alternating-subarray-sum/

impl Solution {
    pub fn maximum_alternating_subarray_sum(nums: Vec<i32>) -> i64 {
        let mut ans = i64::MIN;
        let mut even = 0i64;
        for (i, &num) in nums.iter().enumerate() {
            let x = num as i64;
            if i % 2 == 0 {
                even += x;
            } else {
                even = (even - x).max(0);
            }
            ans = ans.max(even);
        }
        let mut odd = 0i64;
        for i in 1..nums.len() {
            let x = nums[i] as i64;
            if i % 2 == 1 {
                odd += x;
            } else {
                odd = (odd - x).max(0);
            }
            ans = ans.max(odd);
        }
        ans
    }
}
