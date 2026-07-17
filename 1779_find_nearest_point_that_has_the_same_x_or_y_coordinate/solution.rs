// LeetCode 1779 - Find Nearest Point That Has the Same X or Y Coordinate
// https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

impl Solution {
    pub fn nearest_valid_point(x: i32, y: i32, points: Vec<Vec<i32>>) -> i32 {
        let mut best = i32::MAX;
        let mut ans = -1;
        for (i, point) in points.iter().enumerate() {
            let (px, py) = (point[0], point[1]);
            if px != x && py != y {
                continue;
            }
            let dist = (px - x).abs() + (py - y).abs();
            if dist < best {
                best = dist;
                ans = i as i32;
            }
        }
        ans
    }
}
