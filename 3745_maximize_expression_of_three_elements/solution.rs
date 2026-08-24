// LeetCode 3745 - Maximize Expression of Three Elements
// https://leetcode.com/problems/maximize-expression-of-three-elements/

impl Solution {
    pub fn maximize_expression_of_three(nums: Vec<i32>) -> i32 {
        const INF: i32 = 1 << 30;
        let mut a = -INF;
        let mut b = -INF;
        let mut c = INF;
        for &x in &nums {
            if x < c {
                c = x;
            }
            if x >= a {
                b = a;
                a = x;
            } else if x > b {
                b = x;
            }
        }
        a + b - c
    }
}
