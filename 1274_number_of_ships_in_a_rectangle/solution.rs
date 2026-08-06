// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

struct Point {
    x: i32,
    y: i32,
}

trait Sea {
    fn has_ships(&self, top_right: Point, bottom_left: Point) -> bool;
}

impl Solution {
    pub fn count_ships(sea: &impl Sea, top_right: Point, bottom_left: Point) -> i32 {
        let (tx, ty) = (top_right.x, top_right.y);
        let (bx, by) = (bottom_left.x, bottom_left.y);
        if tx < bx || ty < by || !sea.has_ships(Point { x: tx, y: ty }, Point { x: bx, y: by }) {
            return 0;
        }
        if tx == bx && ty == by {
            return 1;
        }
        let mx = (tx + bx) / 2;
        let my = (ty + by) / 2;
        Self::count_ships(sea, Point { x: mx, y: my }, Point { x: bx, y: by })
            + Self::count_ships(sea, Point { x: tx, y: my }, Point { x: mx + 1, y: by })
            + Self::count_ships(sea, Point { x: mx, y: ty }, Point { x: bx, y: my + 1 })
            + Self::count_ships(sea, Point { x: tx, y: ty }, Point { x: mx + 1, y: my + 1 })
    }
}
