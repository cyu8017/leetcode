// LeetCode 0533 - Lonely Pixel II
// https://leetcode.com/problems/lonely-pixel-ii/

impl Solution {
    pub fn find_black_pixel(picture: Vec<Vec<char>>, target: i32) -> i32 {
        let rows = picture.len();
        let cols = picture[0].len();
        let row_strings: Vec<String> = picture
            .iter()
            .map(|row| row.iter().collect::<String>())
            .collect();
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
            if row_counts[r] != target {
                continue;
            }
            for c in 0..cols {
                if picture[r][c] != 'B' || col_counts[c] != target {
                    continue;
                }
                let matches = (0..rows).all(|i| {
                    picture[i][c] != 'B' || row_strings[r] == row_strings[i]
                });
                if matches {
                    lonely += 1;
                }
            }
        }
        lonely
    }
}
