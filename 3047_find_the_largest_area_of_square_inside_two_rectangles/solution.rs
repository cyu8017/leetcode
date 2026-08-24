// LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles
// https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

impl Solution {
    pub fn largest_square_area(bottom_left: Vec<Vec<i32>>, top_right: Vec<Vec<i32>>) -> i64 {
        let mut ans = 0i64;
        let n = bottom_left.len();
        for i in 0..n {
            let (x1, y1) = (bottom_left[i][0], bottom_left[i][1]);
            let (x2, y2) = (top_right[i][0], top_right[i][1]);
            for j in i + 1..n {
                let (x3, y3) = (bottom_left[j][0], bottom_left[j][1]);
                let (x4, y4) = (top_right[j][0], top_right[j][1]);
                let ww = x2.min(x4) - x1.max(x3);
                let h = y2.min(y4) - y1.max(y3);
                let e = ww.min(h);
                if e > 0 {
                    ans = ans.max(e as i64 * e as i64);
                }
            }
        }
        ans
    }
}
