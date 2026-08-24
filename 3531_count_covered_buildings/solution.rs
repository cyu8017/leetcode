// LeetCode 3531 - Count Covered Buildings
// https://leetcode.com/problems/count-covered-buildings/

use std::collections::HashMap;

impl Solution {
    pub fn count_covered_buildings(_n: i32, buildings: Vec<Vec<i32>>) -> i32 {
        let mut g1: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut g2: HashMap<i32, Vec<i32>> = HashMap::new();
        for b in &buildings {
            g1.entry(b[0]).or_default().push(b[1]);
            g2.entry(b[1]).or_default().push(b[0]);
        }
        for list in g1.values_mut() {
            list.sort();
        }
        for list in g2.values_mut() {
            list.sort();
        }
        let mut ans = 0;
        for b in &buildings {
            let (x, y) = (b[0], b[1]);
            let l1 = g1.get(&x).unwrap();
            let l2 = g2.get(&y).unwrap();
            if *l2.first().unwrap() < x && x < *l2.last().unwrap() && *l1.first().unwrap() < y && y < *l1.last().unwrap() {
                ans += 1;
            }
        }
        ans
    }
}
