// LeetCode 1591 - Strange Printer II
// https://leetcode.com/problems/strange-printer-ii/

use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn is_printable(target_grid: Vec<Vec<i32>>) -> bool {
        let mut colors = HashSet::new();
        for row in &target_grid {
            for &x in row {
                colors.insert(x);
            }
        }
        let mut bounds: HashMap<i32, [i32; 4]> = colors
            .iter()
            .map(|&c| (c, [i32::MAX, i32::MAX, -1, -1]))
            .collect();
        for (r, row) in target_grid.iter().enumerate() {
            for (col, &c) in row.iter().enumerate() {
                let b = bounds.get_mut(&c).unwrap();
                b[0] = b[0].min(r as i32);
                b[1] = b[1].min(col as i32);
                b[2] = b[2].max(r as i32);
                b[3] = b[3].max(col as i32);
            }
        }
        let mut graph: HashMap<i32, HashSet<i32>> = HashMap::new();
        let mut indegree: HashMap<i32, i32> = colors.iter().map(|&c| (c, 0)).collect();
        for (&c, &[r1, c1, r2, c2]) in &bounds {
            for r in r1..=r2 {
                for col in c1..=c2 {
                    let other = target_grid[r as usize][col as usize];
                    if other != c {
                        let set = graph.entry(c).or_default();
                        if set.insert(other) {
                            *indegree.entry(other).or_insert(0) += 1;
                        }
                    }
                }
            }
        }
        let mut queue: VecDeque<i32> = colors
            .iter()
            .copied()
            .filter(|c| indegree[c] == 0)
            .collect();
        let mut seen = 0;
        while let Some(c) = queue.pop_front() {
            seen += 1;
            if let Some(nexts) = graph.get(&c) {
                for &nxt in nexts {
                    let d = indegree.get_mut(&nxt).unwrap();
                    *d -= 1;
                    if *d == 0 {
                        queue.push_back(nxt);
                    }
                }
            }
        }
        seen == colors.len()
    }
}
