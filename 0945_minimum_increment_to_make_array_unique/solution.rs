// LeetCode 0945 - Minimum Increment to Make Array Unique
// https://leetcode.com/problems/minimum-increment-to-make-array-unique/

impl Solution {
    pub fn min_increment_for_unique(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let mut ans = 0;
        for i in 1..nums.len() {
            if nums[i] <= nums[i - 1] {
                let need = nums[i - 1] + 1;
                ans += need - nums[i];
                nums[i] = need;
            }
        }
        ans
    }
}
