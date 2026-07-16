// LeetCode 0302 - Smallest Rectangle Enclosing Black Pixels
// https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

impl Solution {
    pub fn min_area(image: Vec<Vec<char>>, x: i32, y: i32) -> i32 {
        let rows = image.len() as i32;
        let cols = image[0].len() as i32;

        let column_has_black = |col: i32| -> bool {
            (0..rows).any(|row| image[row as usize][col as usize] == '1')
        };

        let row_has_black = |row: i32| -> bool {
            (0..cols).any(|col| image[row as usize][col as usize] == '1')
        };

        let mut left = 0;
        let mut right = y;
        while left < right {
            let mid = left + (right - left) / 2;
            if column_has_black(mid) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        let left_bound = left;

        left = y;
        right = cols - 1;
        while left < right {
            let mid = left + (right - left + 1) / 2;
            if column_has_black(mid) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        let right_bound = left;

        let mut top = 0;
        let mut bottom = x;
        while top < bottom {
            let mid = top + (bottom - top) / 2;
            if row_has_black(mid) {
                bottom = mid;
            } else {
                top = mid + 1;
            }
        }
        let top_bound = top;

        top = x;
        bottom = rows - 1;
        while top < bottom {
            let mid = top + (bottom - top + 1) / 2;
            if row_has_black(mid) {
                top = mid;
            } else {
                bottom = mid - 1;
            }
        }
        let bottom_bound = top;

        (right_bound - left_bound + 1) * (bottom_bound - top_bound + 1)
    }
}
