// LeetCode 0932 - Beautiful Array
// https://leetcode.com/problems/beautiful-array/

impl Solution {
    pub fn beautiful_array(n: i32) -> Vec<i32> {
        if n == 1 {
            return vec![1];
        }
        let left = Self::beautiful_array((n + 1) / 2);
        let right = Self::beautiful_array(n / 2);
        let mut ans = Vec::new();
        for x in left {
            ans.push(2 * x - 1);
        }
        for x in right {
            ans.push(2 * x);
        }
        ans
    }
}
