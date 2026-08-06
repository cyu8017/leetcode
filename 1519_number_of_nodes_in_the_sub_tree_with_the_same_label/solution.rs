// LeetCode 1519 - Number of Nodes in the Sub-Tree With the Same Label
// https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

impl Solution {
    pub fn count_sub_trees(n: i32, edges: Vec<Vec<i32>>, labels: String) -> Vec<i32> {
        let n = n as usize;
        let mut graph = vec![Vec::new(); n];
        for e in edges {
            let a = e[0] as usize;
            let b = e[1] as usize;
            graph[a].push(b);
            graph[b].push(a);
        }
        let labels = labels.into_bytes();
        let mut answer = vec![0; n];

        fn dfs(
            node: usize,
            parent: i32,
            graph: &[Vec<usize>],
            labels: &[u8],
            answer: &mut [i32],
        ) -> [i32; 26] {
            let mut counts = [0; 26];
            let index = (labels[node] - b'a') as usize;
            counts[index] = 1;
            for &neighbor in &graph[node] {
                if neighbor as i32 != parent {
                    let child = dfs(neighbor, node as i32, graph, labels, answer);
                    for i in 0..26 {
                        counts[i] += child[i];
                    }
                }
            }
            answer[node] = counts[index];
            counts
        }

        dfs(0, -1, &graph, &labels, &mut answer);
        answer
    }
}
