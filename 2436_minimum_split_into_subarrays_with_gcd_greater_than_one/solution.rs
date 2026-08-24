// LeetCode 2436 - Minimum Split Into Subarrays With GCD Greater Than One
// https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

impl Solution {
    pub fn minimum_splits(nums: Vec<i32>) -> i32 {
        fn gcd(mut x: i32, mut y: i32) -> i32 {
            while y != 0 {
                let t = x % y;
                x = y;
                y = t;
            }
            x
        }
        let mut ans = 1;
        let mut g = nums[0];
        for i in 1..nums.len() {
            let ng = gcd(g, nums[i]);
            if ng == 1 {
                ans += 1;
                g = nums[i];
            } else {
                g = ng;
            }
        }
        ans
    }
}
