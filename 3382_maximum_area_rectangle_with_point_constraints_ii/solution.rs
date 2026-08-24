// LeetCode 3382 - Maximum Area Rectangle With Point Constraints II
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

use std::collections::HashSet;

impl Solution {
    pub fn max_rectangle_area(x_coord: Vec<i32>, y_coord: Vec<i32>) -> i64 {
        let n = x_coord.len();
        let points: Vec<(i32, i32)> = (0..n).map(|i| (x_coord[i], y_coord[i])).collect();
        let set: HashSet<(i32, i32)> = points.iter().cloned().collect();
        let mut ans = -1i64;
        for i in 0..n {
            for j in i + 1..n {
                let (x1, y1) = points[i];
                let (x2, y2) = points[j];
                if x1 == x2 || y1 == y2 {
                    continue;
                }
                if !set.contains(&(x1, y2)) || !set.contains(&(x2, y1)) {
                    continue;
                }
                let min_x = x1.min(x2);
                let max_x = x1.max(x2);
                let min_y = y1.min(y2);
                let max_y = y1.max(y2);
                let mut ok = true;
                for &(x, y) in &points {
                    if x > min_x && x < max_x && y > min_y && y < max_y {
                        ok = false;
                        break;
                    }
                    let on_border = ((x == min_x || x == max_x) && y >= min_y && y <= max_y)
                        || ((y == min_y || y == max_y) && x >= min_x && x <= max_x);
                    if on_border {
                        let is_corner = (x == min_x || x == max_x) && (y == min_y || y == max_y);
                        if !is_corner {
                            ok = false;
                            break;
                        }
                    }
                }
                if ok {
                    let area = (max_x - min_x) as i64 * (max_y - min_y) as i64;
                    if area > ans {
                        ans = area;
                    }
                }
            }
        }
        ans
    }
}
