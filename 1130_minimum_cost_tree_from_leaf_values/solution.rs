// LeetCode 1130 - Minimum Cost Tree From Leaf Values
// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

impl Solution {
    pub fn mct_from_leaf_values(arr: Vec<i32>) -> i32 {
        let mut stack = vec![i32::MAX];
        let mut ans = 0;
        for x in arr {
            while *stack.last().unwrap() <= x {
                let mid = stack.pop().unwrap();
                let left = *stack.last().unwrap();
                ans += mid * left.min(x);
            }
            stack.push(x);
        }
        while stack.len() > 2 {
            let mid = stack.pop().unwrap();
            ans += mid * *stack.last().unwrap();
        }
        ans
    }
}
