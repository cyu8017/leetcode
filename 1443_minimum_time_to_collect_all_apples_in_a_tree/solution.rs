// LeetCode 1443 - Minimum Time to Collect All Apples in a Tree
// https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

impl Solution {
    pub fn min_time(n: i32, edges: Vec<Vec<i32>>, has_apple: Vec<bool>) -> i32 {
        let n = n as usize;
        let mut graph = vec![Vec::new(); n];
        for e in edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            graph[a].push(b);
            graph[b].push(a);
        }
        fn visit(node: usize, parent: i32, graph: &[Vec<usize>], has_apple: &[bool]) -> i32 {
            let mut cost = 0;
            for &child in &graph[node] {
                if child as i32 != parent {
                    let child_cost = visit(child, node as i32, graph, has_apple);
                    if child_cost > 0 || has_apple[child] {
                        cost += child_cost + 2;
                    }
                }
            }
            cost
        }
        visit(0, -1, &graph, &has_apple)
    }
}
