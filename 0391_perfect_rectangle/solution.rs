// LeetCode 0391 - Perfect Rectangle
// https://leetcode.com/problems/perfect-rectangle/

use std::collections::HashMap;

impl Solution {
    pub fn is_rectangle_cover(rectangles: Vec<Vec<i32>>) -> bool {
        let mut points: HashMap<(i32, i32), i32> = HashMap::new();
        let mut area: i64 = 0;
        let mut min_x = i32::MAX;
        let mut min_y = i32::MAX;
        let mut max_x = i32::MIN;
        let mut max_y = i32::MIN;

        for rect in rectangles {
            let x1 = rect[0];
            let y1 = rect[1];
            let x2 = rect[2];
            let y2 = rect[3];
            area += i64::from(x2 - x1) * i64::from(y2 - y1);
            min_x = min_x.min(x1);
            min_y = min_y.min(y1);
            max_x = max_x.max(x2);
            max_y = max_y.max(y2);

            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)] {
                *points.entry(point).or_insert(0) ^= 1;
            }
        }

        if points.len() != 4 {
            return false;
        }

        let corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)];
        for corner in corners {
            if points.get(&corner) != Some(&1) {
                return false;
            }
        }
        for count in points.values() {
            if *count != 1 {
                return false;
            }
        }

        area == i64::from(max_x - min_x) * i64::from(max_y - min_y)
    }
}
