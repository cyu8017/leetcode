// LeetCode 3235 - Check if the Rectangle Corner Is Reachable
// https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

impl Solution {
    pub fn can_reach_corner(x_corner: i32, y_corner: i32, circles: Vec<Vec<i32>>) -> bool {
        let in_circle = |x: i32, y: i32, cx: i32, cy: i32, r: i32| {
            let dx = x as i64 - cx as i64;
            let dy = y as i64 - cy as i64;
            dx * dx + dy * dy <= r as i64 * r as i64
        };
        let cross_left_top = |cx: i32, cy: i32, r: i32| {
            let a = cx.abs() <= r && cy >= 0 && cy <= y_corner;
            let b = (cy - y_corner).abs() <= r && cx >= 0 && cx <= x_corner;
            a || b
        };
        let cross_right_bottom = |cx: i32, cy: i32, r: i32| {
            let a = (cx - x_corner).abs() <= r && cy >= 0 && cy <= y_corner;
            let b = cy.abs() <= r && cx >= 0 && cx <= x_corner;
            a || b
        };
        let n = circles.len();
        let mut vis = vec![false; n];
        fn dfs(
            i: usize,
            circles: &[Vec<i32>],
            vis: &mut [bool],
            x_corner: i32,
            y_corner: i32,
            cross_right_bottom: &dyn Fn(i32, i32, i32) -> bool,
        ) -> bool {
            let x1 = circles[i][0];
            let y1 = circles[i][1];
            let r1 = circles[i][2];
            if cross_right_bottom(x1, y1, r1) {
                return true;
            }
            vis[i] = true;
            for j in 0..circles.len() {
                if vis[j] {
                    continue;
                }
                let x2 = circles[j][0];
                let y2 = circles[j][1];
                let r2 = circles[j][2];
                if (x1 as i64 - x2 as i64) * (x1 as i64 - x2 as i64)
                    + (y1 as i64 - y2 as i64) * (y1 as i64 - y2 as i64)
                    > (r1 as i64 + r2 as i64) * (r1 as i64 + r2 as i64)
                {
                    continue;
                }
                if x1 as i64 * r2 as i64 + x2 as i64 * (r1 as i64)
                    < (r1 as i64 + r2 as i64) * x_corner as i64
                    && y1 as i64 * r2 as i64 + y2 as i64 * (r1 as i64)
                        < (r1 as i64 + r2 as i64) * y_corner as i64
                    && dfs(j, circles, vis, x_corner, y_corner, cross_right_bottom)
                {
                    return true;
                }
            }
            false
        }
        for i in 0..n {
            let x = circles[i][0];
            let y = circles[i][1];
            let r = circles[i][2];
            if in_circle(0, 0, x, y, r) || in_circle(x_corner, y_corner, x, y, r) {
                return false;
            }
            if !vis[i] && cross_left_top(x, y, r)
                && dfs(i, &circles, &mut vis, x_corner, y_corner, &cross_right_bottom)
            {
                return false;
            }
        }
        true
    }
}
