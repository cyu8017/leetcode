struct Solution;
// LeetCode 3880 - Minimum Absolute Difference Between Two Values
// https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

impl Solution {
    pub fn min_absolute_difference(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut ans = n + 1;
        let mut last = [-ans, -ans, -ans];
        for (i, &x) in nums.iter().enumerate() {
            if x != 0 {
                ans = ans.min(i as i32 - last[(3 - x) as usize]);
                last[x as usize] = i as i32;
            }
        }
        if ans > n {
            -1
        } else {
            ans
        }
    }
}
