// LeetCode 0531 - Lonely Pixel I
// https://leetcode.com/problems/lonely-pixel-i/

impl Solution {
    pub fn find_lonely_pixel(picture: Vec<Vec<char>>) -> i32 {
        let rows = picture.len();
        let cols = picture[0].len();
        let mut row_counts = vec![0; rows];
        let mut col_counts = vec![0; cols];

        for r in 0..rows {
            for c in 0..cols {
                if picture[r][c] == 'B' {
                    row_counts[r] += 1;
                    col_counts[c] += 1;
                }
            }
        }

        let mut lonely = 0;
        for r in 0..rows {
            for c in 0..cols {
                if picture[r][c] == 'B' && row_counts[r] == 1 && col_counts[c] == 1 {
                    lonely += 1;
                }
            }
        }
        lonely
    }
}
