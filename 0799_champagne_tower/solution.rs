// LeetCode 0799 - Champagne Tower
// https://leetcode.com/problems/champagne-tower/

impl Solution {
    pub fn champagne_tower(poured: i32, query_row: i32, query_glass: i32) -> f64 {
        let mut row = vec![poured as f64];
        for r in 0..query_row {
            let mut next_row = vec![0.0; (r + 2) as usize];
            for i in 0..row.len() {
                let overflow = (row[i] - 1.0) / 2.0;
                if overflow > 0.0 {
                    next_row[i] += overflow;
                    next_row[i + 1] += overflow;
                }
            }
            row = next_row;
        }
        1.0_f64.min(row[query_glass as usize])
    }
}
