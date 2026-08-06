// LeetCode 1131 - Maximum of Absolute Value Expression
// https://leetcode.com/problems/maximum-of-absolute-value-expression/

impl Solution {
    pub fn max_abs_val_expr(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let n = arr1.len();
        let mut ans = 0;
        let signs = [(1, 1), (1, -1), (-1, 1), (-1, -1)];
        for (s0, s1) in signs {
            let mut max_v = arr1[0] * s0 + arr2[0] * s1;
            let mut min_v = max_v;
            for i in 1..n {
                let v = arr1[i] * s0 + arr2[i] * s1 + i as i32;
                max_v = max_v.max(v);
                min_v = min_v.min(v);
            }
            ans = ans.max(max_v - min_v);
        }
        ans
    }
}
