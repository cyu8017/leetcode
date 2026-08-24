// LeetCode 3660 - Jump Game IX
// https://leetcode.com/problems/jump-game-ix/

impl Solution {
    pub fn max_value(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut ans = vec![0; n];
        let mut pre_max = vec![0; n];
        pre_max[0] = nums[0];
        for i in 1..n {
            pre_max[i] = pre_max[i - 1].max(nums[i]);
        }
        let mut suf_min = i32::MAX / 2;
        for i in (0..n).rev() {
            if pre_max[i] > suf_min {
                ans[i] = ans[i + 1];
            } else {
                ans[i] = pre_max[i];
            }
            suf_min = suf_min.min(nums[i]);
        }
        ans
    }
}
