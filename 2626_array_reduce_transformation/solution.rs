// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

impl Solution {
    pub fn reduce(nums: Vec<i32>, f: impl Fn(i32, i32) -> i32, init: i32) -> i32 {
        let mut acc = init;
        for x in nums {
            acc = f(acc, x);
        }
        acc
    }
}
