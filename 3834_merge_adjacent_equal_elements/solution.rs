// LeetCode 3834 - Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge-adjacent-equal-elements/

impl Solution {
    pub fn merge_adjacent(nums: Vec<i32>) -> Vec<i64> {
        let mut stk = Vec::new();
        for x in nums {
            stk.push(x as i64);
            while stk.len() > 1 && stk[stk.len() - 1] == stk[stk.len() - 2] {
                let a = stk.pop().unwrap();
                let b = stk.pop().unwrap();
                stk.push(a + b);
            }
        }
        stk
    }
}
