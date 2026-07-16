// LeetCode 0447 - Number of Boomerangs
// https://leetcode.com/problems/number-of-boomerangs/

use std::collections::HashMap;

impl Solution {
    pub fn number_of_boomerangs(points: Vec<Vec<i32>>) -> i32 {
        let mut total = 0;
        for anchor in &points {
            let mut distances: HashMap<i64, i32> = HashMap::new();
            for other in &points {
                let dx = i64::from(anchor[0] - other[0]);
                let dy = i64::from(anchor[1] - other[1]);
                *distances.entry(dx * dx + dy * dy).or_insert(0) += 1;
            }
            for count in distances.values() {
                total += count * (count - 1);
            }
        }
        total
    }
}
