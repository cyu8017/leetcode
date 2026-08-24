// LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

impl Solution {
    pub fn min_operations_to_make_median_k(mut nums: Vec<i32>, k: i32) -> i64 {
        nums.sort_unstable();
        let n = nums.len();
        let m = n >> 1;
        let mut ans = (nums[m] - k).abs() as i64;
        if nums[m] > k {
            let mut i = m;
            while i > 0 && nums[i - 1] > k {
                i -= 1;
                ans += (nums[i] - k) as i64;
            }
        } else {
            for i in m + 1..n {
                if nums[i] >= k {
                    break;
                }
                ans += (k - nums[i]) as i64;
            }
        }
        ans
    }
}
