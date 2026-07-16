// LeetCode 0261 - Graph Valid Tree
// https://leetcode.com/problems/graph-valid-tree/

impl Solution {
    pub fn valid_tree(n: i32, edges: Vec<Vec<i32>>) -> bool {
        let n = n as usize;
        if edges.len() != n - 1 {
            return false;
        }
        let mut parent: Vec<usize> = (0..n).collect();

        fn find(parent: &mut Vec<usize>, node: usize) -> usize {
            if parent[node] != node {
                let root = find(parent, parent[node]);
                parent[node] = root;
            }
            parent[node]
        }

        for edge in edges {
            let left = edge[0] as usize;
            let right = edge[1] as usize;
            let root_left = find(&mut parent, left);
            let root_right = find(&mut parent, right);
            if root_left == root_right {
                return false;
            }
            parent[root_left] = root_right;
        }
        true
    }
}
