// LeetCode 2216 - Minimum Deletions to Make Array Beautiful
// https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

impl Solution {
    pub fn min_deletion(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut i = 0;
        let n = nums.len();
        while i + 1 < n {
            if nums[i] == nums[i + 1] {
                ans += 1;
                i += 1;
            } else {
                i += 2;
            }
        }
        if (n as i32 - ans) % 2 == 1 {
            ans += 1;
        }
        ans
    }
}
