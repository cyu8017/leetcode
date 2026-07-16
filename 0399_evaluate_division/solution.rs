// LeetCode 0399 - Evaluate Division
// https://leetcode.com/problems/evaluate-division/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn calc_equation(
        equations: Vec<Vec<String>>,
        values: Vec<f64>,
        queries: Vec<Vec<String>>,
    ) -> Vec<f64> {
        let mut graph: HashMap<String, HashMap<String, f64>> = HashMap::new();

        for (equation, value) in equations.iter().zip(values.iter()) {
            graph
                .entry(equation[0].clone())
                .or_default()
                .insert(equation[1].clone(), *value);
            graph
                .entry(equation[1].clone())
                .or_default()
                .insert(equation[0].clone(), 1.0 / value);
        }

        fn dfs(
            graph: &HashMap<String, HashMap<String, f64>>,
            start: &str,
            end: &str,
            visited: &mut HashSet<String>,
        ) -> f64 {
            if !graph.contains_key(start) || !graph.contains_key(end) {
                return -1.0;
            }
            if start == end {
                return 1.0;
            }
            visited.insert(start.to_string());
            for (neighbor, weight) in graph.get(start).unwrap() {
                if visited.contains(neighbor) {
                    continue;
                }
                let result = dfs(graph, neighbor, end, visited);
                if result >= 0.0 {
                    return weight * result;
                }
            }
            -1.0
        }

        queries
            .iter()
            .map(|query| {
                let mut visited = HashSet::new();
                dfs(&graph, &query[0], &query[1], &mut visited)
            })
            .collect()
    }
}
