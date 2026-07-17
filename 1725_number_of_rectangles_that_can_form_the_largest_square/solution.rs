// LeetCode 1725 - Number Of Rectangles That Can Form The Largest Square
// https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

impl Solution {
    pub fn count_good_rectangles(rectangles: Vec<Vec<i32>>) -> i32 {
        let mut best = 0;
        let mut count = 0;
        for rect in &rectangles {
            let side = rect[0].min(rect[1]);
            if side > best {
                best = side;
                count = 1;
            } else if side == best {
                count += 1;
            }
        }
        count
    }
}
