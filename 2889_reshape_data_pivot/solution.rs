// LeetCode 2889 - Reshape Data: Pivot
// https://leetcode.com/problems/reshape-data-pivot/

use std::collections::HashMap;

impl Solution {
    pub fn pivot_table(weather: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut months = Vec::new();
        let mut by_month: HashMap<i32, HashMap<i32, i32>> = HashMap::new();
        for r in weather {
            if r.len() < 3 {
                continue;
            }
            let (city, month, temperature) = (r[0], r[1], r[2]);
            if !by_month.contains_key(&month) {
                months.push(month);
            }
            by_month.entry(month).or_default().insert(city, temperature);
        }
        months
            .into_iter()
            .map(|month| {
                let mut row = vec![month];
                if let Some(cities) = by_month.get(&month) {
                    let mut keys: Vec<i32> = cities.keys().copied().collect();
                    keys.sort_unstable();
                    for k in keys {
                        row.push(cities[&k]);
                    }
                }
                row
            })
            .collect()
    }
}
