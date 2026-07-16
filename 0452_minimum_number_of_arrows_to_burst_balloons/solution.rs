// LeetCode 0452 - Minimum Number of Arrows to Burst Balloons
// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

impl Solution {
    pub fn find_min_arrow_shots(points: &mut Vec<Vec<i32>>) -> i32 {
        if points.is_empty() {
            return 0;
        }

        points.sort_by_key(|point| point[1]);

        let mut arrows = 1;
        let mut end = points[0][1];
        for point in points.iter().skip(1) {
            if point[0] > end {
                arrows += 1;
                end = point[1];
            }
        }
        arrows
    }
}
