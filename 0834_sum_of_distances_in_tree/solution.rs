// LeetCode 0834 - Sum of Distances in Tree
// https://leetcode.com/problems/sum-of-distances-in-tree/

impl Solution {
    pub fn sum_of_distances_in_tree(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut graph = vec![Vec::new(); n];
        for e in &edges {
            graph[e[0] as usize].push(e[1] as usize);
            graph[e[1] as usize].push(e[0] as usize);
        }
        let mut count = vec![1i32; n];
        let mut ans = vec![0i32; n];
        Self::post(&graph, 0, usize::MAX, &mut count, &mut ans);
        Self::reroot(&graph, 0, usize::MAX, n as i32, &count, &mut ans);
        ans
    }

    fn post(
        graph: &[Vec<usize>],
        node: usize,
        parent: usize,
        count: &mut [i32],
        ans: &mut [i32],
    ) {
        for &child in &graph[node] {
            if child == parent {
                continue;
            }
            Self::post(graph, child, node, count, ans);
            count[node] += count[child];
            ans[node] += ans[child] + count[child];
        }
    }

    fn reroot(
        graph: &[Vec<usize>],
        node: usize,
        parent: usize,
        n: i32,
        count: &[i32],
        ans: &mut [i32],
    ) {
        for &child in &graph[node] {
            if child == parent {
                continue;
            }
            ans[child] = ans[node] - count[child] + (n - count[child]);
            Self::reroot(graph, child, node, n, count, ans);
        }
    }
}
