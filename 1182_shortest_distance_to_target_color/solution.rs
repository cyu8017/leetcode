// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

use std::collections::HashMap;

impl Solution {
    pub fn shortest_distance_color(colors: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut pos: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &c) in colors.iter().enumerate() {
            pos.entry(c).or_default().push(i);
        }
        queries
            .into_iter()
            .map(|q| {
                let i = q[0] as usize;
                let c = q[1];
                let Some(arr) = pos.get(&c) else {
                    return -1;
                };
                let idx = arr.partition_point(|&x| x < i);
                let mut best = i32::MAX;
                if idx < arr.len() {
                    best = best.min((arr[idx] - i) as i32);
                }
                if idx > 0 {
                    best = best.min((i - arr[idx - 1]) as i32);
                }
                if best == i32::MAX {
                    -1
                } else {
                    best
                }
            })
            .collect()
    }
}
