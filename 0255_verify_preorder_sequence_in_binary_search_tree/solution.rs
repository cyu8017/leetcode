// LeetCode 0255 - Verify Preorder Sequence in Binary Search Tree
// https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

impl Solution {
    pub fn verify_preorder(preorder: Vec<i32>) -> bool {
        let mut low = i32::MIN;
        let mut stack: Vec<i32> = Vec::new();

        for value in preorder {
            if value < low {
                return false;
            }
            while let Some(&last) = stack.last() {
                if last < value {
                    low = stack.pop().unwrap();
                } else {
                    break;
                }
            }
            stack.push(value);
        }

        true
    }
}
