// LeetCode 2249 - Count Lattice Points Inside a Circle
// https://leetcode.com/problems/count-lattice-points-inside-a-circle/

use std::collections::HashSet;

impl Solution {
    pub fn count_lattice_points(circles: Vec<Vec<i32>>) -> i32 {
        let mut seen = HashSet::new();
        for c in circles {
            let (x, y, r) = (c[0], c[1], c[2]);
            for i in x - r..=x + r {
                for j in y - r..=y + r {
                    if (i - x) * (i - x) + (j - y) * (j - y) <= r * r {
                        seen.insert((i, j));
                    }
                }
            }
        }
        seen.len() as i32
    }
}
