// LeetCode 2860 - Happy Students
// https://leetcode.com/problems/happy-students/

impl Solution {
    pub fn count_ways(mut nums: Vec<i32>) -> i32 {
        nums.sort_unstable();
        let n = nums.len();
        let mut ans = 0;
        if nums[0] > 0 {
            ans += 1;
        }
        for i in 0..n {
            let selected = (i + 1) as i32;
            if selected > nums[i] && (i == n - 1 || selected < nums[i + 1]) {
                ans += 1;
            }
        }
        ans
    }
}
