// LeetCode 2764 - Is Array a Preorder of Some Binary Tree
// https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

impl Solution {
    pub fn is_preorder(nodes: Vec<Vec<i32>>) -> bool {
        if nodes.is_empty() {
            return true;
        }
        let mut stack = vec![nodes[0][0]];
        for node in nodes.iter().skip(1) {
            let id = node[0];
            let parent = node[1];
            while !stack.is_empty() && *stack.last().unwrap() != parent {
                stack.pop();
            }
            if stack.is_empty() {
                return false;
            }
            stack.push(id);
        }
        true
    }
}
