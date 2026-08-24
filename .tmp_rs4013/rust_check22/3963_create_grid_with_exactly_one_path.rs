struct Solution;
// LeetCode 3963 - Create Grid With Exactly One Path
// https://leetcode.com/problems/create-grid-with-exactly-one-path/

impl Solution {
    pub fn create_grid(m: i32, n: i32) -> Vec<String> {
        let mut g = vec![vec![b'#'; n as usize]; m as usize];
        for j in 0..n as usize {
            g[0][j] = b'.';
        }
        for i in 0..m as usize {
            g[i][n as usize - 1] = b'.';
        }
        g.into_iter()
            .map(|row| String::from_utf8(row).unwrap())
            .collect()
    }
}

fn main() {}
