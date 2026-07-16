// LeetCode 0469 - Convex Polygon
// https://leetcode.com/problems/convex-polygon/

impl Solution {
    pub fn is_convex(points: Vec<Vec<i32>>) -> bool {
        let count = points.len();
        let mut direction = 0;

        for index in 0..count {
            let x1 = points[(index + 1) % count][0] - points[index][0];
            let y1 = points[(index + 1) % count][1] - points[index][1];
            let x2 = points[(index + 2) % count][0] - points[(index + 1) % count][0];
            let y2 = points[(index + 2) % count][1] - points[(index + 1) % count][1];
            let cross = i64::from(x1) * i64::from(y2) - i64::from(y1) * i64::from(x2);
            if cross == 0 {
                continue;
            }
            let current = if cross > 0 { 1 } else { -1 };
            if direction == 0 {
                direction = current;
            } else if direction != current {
                return false;
            }
        }

        true
    }
}
