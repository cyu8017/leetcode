struct Solution;
// LeetCode 3417 - Zigzag Grid Traversal With Skip
// https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

impl Solution {
    pub fn zigzag_traversal(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let mut ans = Vec::new();
        let mut skip = false;
        for (i, row) in grid.iter().enumerate() {
            if i % 2 == 0 {
                for &v in row {
                    if !skip {
                        ans.push(v);
                    }
                    skip = !skip;
                }
            } else {
                for j in (0..row.len()).rev() {
                    if !skip {
                        ans.push(row[j]);
                    }
                    skip = !skip;
                }
            }
        }
        ans
    }
}

fn main() {}
