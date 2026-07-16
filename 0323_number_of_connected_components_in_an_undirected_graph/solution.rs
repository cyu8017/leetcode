// LeetCode 0323 - Number of Connected Components in an Undirected Graph
// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

impl Solution {
    pub fn count_components(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut parent: Vec<usize> = (0..n).collect();
        let mut rank = vec![0; n];

        fn find(parent: &mut [usize], node: usize) -> usize {
            if parent[node] != node {
                let root = find(parent, parent[node]);
                parent[node] = root;
            }
            parent[node]
        }

        let mut components = n as i32;
        for edge in edges {
            let left = edge[0] as usize;
            let right = edge[1] as usize;
            let mut root_left = find(&mut parent, left);
            let mut root_right = find(&mut parent, right);
            if root_left == root_right {
                continue;
            }
            if rank[root_left] < rank[root_right] {
                std::mem::swap(&mut root_left, &mut root_right);
            }
            parent[root_right] = root_left;
            if rank[root_left] == rank[root_right] {
                rank[root_left] += 1;
            }
            components -= 1;
        }
        components
    }
}
