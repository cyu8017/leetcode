// LeetCode 3111 - Minimum Rectangles to Cover Points
// https://leetcode.com/problems/minimum-rectangles-to-cover-points/

impl Solution {
    pub fn min_rectangles_to_cover_points(mut points: Vec<Vec<i32>>, w: i32) -> i32 {
        points.sort_unstable_by_key(|p| p[0]);
        let mut ans = 0;
        let mut x1 = -1;
        for p in points {
            if p[0] > x1 {
                ans += 1;
                x1 = p[0] + w;
            }
        }
        ans
    }
}
