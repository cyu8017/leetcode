// LeetCode 2708 - Maximum Strength of a Group
// https://leetcode.com/problems/maximum-strength-of-a-group/

impl Solution {
    pub fn max_strength(mut nums: Vec<i32>) -> i64 {
        nums.sort_unstable();
        let n = nums.len();
        if n == 1 {
            return nums[0] as i64;
        }
        let mut prod = 1i64;
        let mut used = false;
        let mut i = 0;
        while i + 1 < n && nums[i] < 0 && nums[i + 1] < 0 {
            prod *= nums[i] as i64 * nums[i + 1] as i64;
            used = true;
            i += 2;
        }
        let neg_left = i < n && nums[i] < 0;
        while i < n {
            if nums[i] > 0 {
                prod *= nums[i] as i64;
                used = true;
            }
            i += 1;
        }
        if !used {
            if neg_left {
                if nums.iter().any(|&x| x == 0) {
                    return 0;
                }
                return nums[n - 1] as i64;
            }
            return 0;
        }
        prod
    }
}
