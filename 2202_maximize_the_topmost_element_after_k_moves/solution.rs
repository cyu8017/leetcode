// LeetCode 2202 - Maximize the Topmost Element After K Moves
// https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

impl Solution {
    pub fn maximum_top(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len() as i32;
        if n == 1 {
            return if k % 2 == 1 { -1 } else { nums[0] };
        }
        if k == 0 {
            return nums[0];
        }
        let mut ans = -1;
        let limit = (k - 1).min(n);
        for i in 0..limit {
            ans = ans.max(nums[i as usize]);
        }
        if k < n {
            ans = ans.max(nums[k as usize]);
        }
        ans
    }
}
