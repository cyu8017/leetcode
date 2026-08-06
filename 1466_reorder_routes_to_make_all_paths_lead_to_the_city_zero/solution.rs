// LeetCode 1466 - Reorder Routes to Make All Paths Lead to the City Zero
// https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

impl Solution {
    pub fn min_reorder(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut graph = vec![Vec::new(); n];
        for e in connections {
            let (a, b) = (e[0] as usize, e[1] as usize);
            graph[a].push((b, 1));
            graph[b].push((a, 0));
        }
        let mut ans = 0;
        let mut stack = vec![0usize];
        let mut seen = vec![false; n];
        seen[0] = true;
        while let Some(node) = stack.pop() {
            for &(nei, cost) in &graph[node] {
                if !seen[nei] {
                    seen[nei] = true;
                    stack.push(nei);
                    ans += cost;
                }
            }
        }
        ans
    }
}
