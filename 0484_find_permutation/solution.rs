// LeetCode 0484 - Find Permutation
// https://leetcode.com/problems/find-permutation/

impl Solution {
    pub fn find_permutation(s: String) -> Vec<i32> {
        let mut stack = vec![1];
        let mut result = Vec::new();
        for ch in s.chars() {
            if ch == 'I' {
                while let Some(value) = stack.pop() {
                    result.push(value);
                }
            }
            stack.push((stack.len() + result.len() + 1) as i32);
        }
        while let Some(value) = stack.pop() {
            result.push(value);
        }
        result
    }
}
