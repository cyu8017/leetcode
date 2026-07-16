// LeetCode 0006 - Zigzag Conversion
// https://leetcode.com/problems/zigzag-conversion/

impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        let num_rows = num_rows as usize;
        let bytes = s.as_bytes();
        if num_rows == 1 || num_rows >= bytes.len() {
            return s;
        }

        let mut rows: Vec<Vec<u8>> = vec![Vec::new(); num_rows];
        let mut index = 0isize;
        let mut step = 1isize;

        for &ch in bytes {
            rows[index as usize].push(ch);
            if index == 0 {
                step = 1;
            } else if index == num_rows as isize - 1 {
                step = -1;
            }
            index += step;
        }

        rows.into_iter().flat_map(|row| row.into_iter()).map(|b| b as char).collect()
    }
}
