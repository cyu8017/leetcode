// LeetCode 0356 - Line Reflection
// https://leetcode.com/problems/line-reflection/

use std::collections::HashSet;

impl Solution {
    pub fn is_reflected(points: Vec<Vec<i32>>) -> bool {
        let mut point_set = HashSet::new();
        let mut min_x = points[0][0];
        let mut max_x = points[0][0];

        for point in &points {
            min_x = min_x.min(point[0]);
            max_x = max_x.max(point[0]);
            point_set.insert((point[0], point[1]));
        }

        let target = min_x + max_x;
        for point in &points {
            if !point_set.contains(&(target - point[0], point[1])) {
                return false;
            }
        }

        true
    }
}
