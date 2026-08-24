// LeetCode 3192 - Minimum Operations to Make Binary Array Elements Equal to One II
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut v = 0;
        for x in nums {
            let x = x ^ v;
            if x == 0 {
                v ^= 1;
                ans += 1;
            }
        }
        ans
    }
}
