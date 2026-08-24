// LeetCode 3300 - Minimum Element After Replacement With Digit Sum
// https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

impl Solution {
    pub fn min_element(nums: Vec<i32>) -> i32 {
        let mut ans = 1_000_000_000;
        for mut x in nums {
            let mut s = 0;
            while x > 0 {
                s += x % 10;
                x /= 10;
            }
            if s < ans {
                ans = s;
            }
        }
        ans
    }
}
