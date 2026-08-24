// LeetCode 3730 - Maximum Calories Burnt from Jumps
// https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

impl Solution {
    pub fn max_calories_burnt(mut heights: Vec<i32>) -> i64 {
        heights.sort_unstable();
        let mut ans = 0i64;
        let mut pre = 0i32;
        let mut l = 0usize;
        let mut r = heights.len() - 1;
        while l < r {
            let d1 = (heights[r] - pre) as i64;
            ans += d1 * d1;
            let d2 = (heights[l] - heights[r]) as i64;
            ans += d2 * d2;
            pre = heights[l];
            l += 1;
            r -= 1;
        }
        let d = (heights[r] - pre) as i64;
        ans += d * d;
        ans
    }
}
