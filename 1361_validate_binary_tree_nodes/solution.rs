// LeetCode 1361 - Validate Binary Tree Nodes
// https://leetcode.com/problems/validate-binary-tree-nodes/

impl Solution {
    pub fn validate_binary_tree_nodes(n: i32, left_child: Vec<i32>, right_child: Vec<i32>) -> bool {
        let n = n as usize;
        let mut indeg = vec![0; n];
        for &x in left_child.iter().chain(right_child.iter()) {
            if x != -1 {
                indeg[x as usize] += 1;
                if indeg[x as usize] > 1 {
                    return false;
                }
            }
        }
        let roots: Vec<usize> = (0..n).filter(|&i| indeg[i] == 0).collect();
        if roots.len() != 1 {
            return false;
        }
        let mut seen = vec![false; n];
        let mut stack = roots;
        while let Some(u) = stack.pop() {
            if seen[u] {
                return false;
            }
            seen[u] = true;
            for &v in &[left_child[u], right_child[u]] {
                if v != -1 {
                    stack.push(v as usize);
                }
            }
        }
        seen.iter().all(|&x| x)
    }
}
