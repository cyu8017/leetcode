// LeetCode 1104 - Path In Zigzag Labelled Binary Tree
// https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

impl Solution {
    pub fn path_in_zig_zag_tree(mut label: i32) -> Vec<i32> {
        let mut path = vec![label];
        while label > 1 {
            let level = 32 - label.leading_zeros() - 1;
            label >>= 1;
            label = (1 << level) - 1 - label + (1 << (level - 1));
            path.push(label);
        }
        path.reverse();
        path
    }
}
