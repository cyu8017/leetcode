// LeetCode 2340 - Minimum Adjacent Swaps to Make a Valid Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/

impl Solution {
    pub fn minimum_swaps(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut min_i = 0;
        let mut max_i = 0;
        for i in 1..n {
            if nums[i] < nums[min_i] {
                min_i = i;
            }
            if nums[i] >= nums[max_i] {
                max_i = i;
            }
        }
        let mut ans = min_i as i32 + (n as i32 - 1 - max_i as i32);
        if min_i > max_i {
            ans -= 1;
        }
        ans
    }
}
