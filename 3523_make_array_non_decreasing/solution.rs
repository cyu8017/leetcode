// LeetCode 3523 - Make Array Non-decreasing
// https://leetcode.com/problems/make-array-non-decreasing/

impl Solution {
    pub fn maximum_possible_size(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut mx = 0;
        for x in nums {
            if mx <= x {
                ans += 1;
                mx = x;
            }
        }
        ans
    }
}
