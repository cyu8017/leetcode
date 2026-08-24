struct Solution;
// LeetCode 3380 - Maximum Area Rectangle With Point Constraints I
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/

use std::collections::HashSet;

impl Solution {
    pub fn max_rectangle_area(points: Vec<Vec<i32>>) -> i32 {
        let set: HashSet<(i32, i32)> = points.iter().map(|p| (p[0], p[1])).collect();
        let mut ans = -1;
        let n = points.len();
        for i in 0..n {
            for j in i + 1..n {
                let x1 = points[i][0];
                let y1 = points[i][1];
                let x2 = points[j][0];
                let y2 = points[j][1];
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
                for p in &points {
                    let x = p[0];
                    let y = p[1];
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
                    let area = (max_x - min_x) * (max_y - min_y);
                    if area > ans {
                        ans = area;
                    }
                }
            }
        }
        ans
    }
}

fn main() {}
