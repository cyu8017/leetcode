// LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

impl Solution {
    pub fn min_max_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut ans = 0i64;
        for i in 0..n {
            let mut mn = nums[i];
            let mut mx = nums[i];
            let mut j = i;
            while j < n && (j - i + 1) as i32 <= k {
                if nums[j] < mn {
                    mn = nums[j];
                }
                if nums[j] > mx {
                    mx = nums[j];
                }
                ans += mn as i64 + mx as i64;
                j += 1;
            }
        }
        ans
    }
}
