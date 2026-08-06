// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

impl Solution {
    pub fn delete_tree_nodes(nodes: i32, parent: Vec<i32>, value: Vec<i32>) -> i32 {
        let nodes = nodes as usize;
        let mut children = vec![Vec::new(); nodes];
        for node in 1..nodes {
            children[parent[node] as usize].push(node);
        }
        fn dfs(node: usize, children: &[Vec<usize>], value: &[i32]) -> (i32, i32) {
            let mut total = value[node];
            let mut count = 1;
            for &child in &children[node] {
                let (cs, cc) = dfs(child, children, value);
                total += cs;
                count += cc;
            }
            if total == 0 {
                (0, 0)
            } else {
                (total, count)
            }
        }
        dfs(0, &children, &value).1
    }
}
