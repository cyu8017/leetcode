// LeetCode 1548 - The Most Similar Path in a Graph
// https://leetcode.com/problems/the-most-similar-path-in-a-graph/

impl Solution {
    pub fn most_similar(
        n: i32,
        roads: Vec<Vec<i32>>,
        names: Vec<String>,
        target_path: Vec<String>,
    ) -> Vec<i32> {
        let n = n as usize;
        let mut graph = vec![Vec::new(); n];
        for e in roads {
            let a = e[0] as usize;
            let b = e[1] as usize;
            graph[a].push(b);
            graph[b].push(a);
        }
        let mut dp: Vec<(i32, Vec<i32>)> = (0..n)
            .map(|node| {
                let cost = if names[node] != target_path[0] { 1 } else { 0 };
                (cost, vec![node as i32])
            })
            .collect();
        for i in 1..target_path.len() {
            let mut next_dp = Vec::with_capacity(n);
            for node in 0..n {
                let mut best: Option<(i32, Vec<i32>)> = None;
                for &prev in &graph[node] {
                    let (cost, path) = &dp[prev];
                    match &best {
                        Some((bc, _)) if *cost >= *bc => {}
                        _ => best = Some((*cost, path.clone())),
                    }
                }
                let (cost, mut path) = best.unwrap();
                path.push(node as i32);
                let add = if names[node] != target_path[i] { 1 } else { 0 };
                next_dp.push((cost + add, path));
            }
            dp = next_dp;
        }
        dp.into_iter().min_by_key(|(c, _)| *c).unwrap().1
    }
}
