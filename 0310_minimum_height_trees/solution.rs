// LeetCode 0310 - Minimum Height Trees
// https://leetcode.com/problems/minimum-height-trees/

impl Solution {
    pub fn find_min_height_trees(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        if n <= 2 {
            return (0..n as i32).collect();
        }

        let mut graph = vec![Vec::new(); n];
        let mut degree = vec![0; n];
        for edge in edges {
            let left = edge[0] as usize;
            let right = edge[1] as usize;
            graph[left].push(right);
            graph[right].push(left);
            degree[left] += 1;
            degree[right] += 1;
        }

        let mut leaves = Vec::new();
        for node in 0..n {
            if degree[node] == 1 {
                leaves.push(node as i32);
            }
        }

        let mut remaining = n;
        while remaining > 2 {
            remaining -= leaves.len();
            let mut new_leaves = Vec::new();
            for leaf in leaves {
                for &neighbor in &graph[leaf as usize] {
                    degree[neighbor] -= 1;
                    if degree[neighbor] == 1 {
                        new_leaves.push(neighbor as i32);
                    }
                }
            }
            leaves = new_leaves;
        }

        leaves
    }
}
