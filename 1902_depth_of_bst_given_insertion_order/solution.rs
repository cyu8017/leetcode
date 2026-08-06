// LeetCode 1902 - Depth of BST Given Insertion Order
// https://leetcode.com/problems/depth-of-bst-given-insertion-order/

impl Solution {
    pub fn max_depth_bst(order: Vec<i32>) -> i32 {
        let mut nodes: Vec<(i32, i32)> = Vec::new(); // sorted (value, depth)
        let mut ans = 0;
        for value in order {
            let i = nodes.partition_point(|&(v, _)| v < value);
            let mut depth = 1;
            if i > 0 {
                depth = depth.max(nodes[i - 1].1 + 1);
            }
            if i < nodes.len() {
                depth = depth.max(nodes[i].1 + 1);
            }
            nodes.insert(i, (value, depth));
            ans = ans.max(depth);
        }
        ans
    }
}
