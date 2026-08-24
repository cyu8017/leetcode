// LeetCode 3427 - Sum of Variable Length Subarrays
// https://leetcode.com/problems/sum-of-variable-length-subarrays/

impl Solution {
    pub fn subarray_sum(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut pref = vec![0; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i];
        }
        let mut ans = 0;
        for i in 0..n {
            let mut start = i as i32 - nums[i];
            if start < 0 {
                start = 0;
            }
            ans += pref[i + 1] - pref[start as usize];
        }
        ans
    }
}
