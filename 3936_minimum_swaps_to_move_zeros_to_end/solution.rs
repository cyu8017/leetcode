// LeetCode 3936 - Minimum Swaps To Move Zeros To End
// https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/

impl Solution {
    pub fn minimum_swaps(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let n = nums.len() as i32;
        let mut i = 0i32;
        let mut j = n - 1;
        while i < j {
            while i < n && nums[i as usize] != 0 {
                i += 1;
            }
            while j > 0 && nums[j as usize] == 0 {
                j -= 1;
            }
            if i >= j {
                break;
            }
            ans += 1;
            i += 1;
            j -= 1;
        }
        ans
    }
}
