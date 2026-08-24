struct Solution;
// LeetCode 2500 - Delete Greatest Value in Each Row
// https://leetcode.com/problems/delete-greatest-value-in-each-row/

impl Solution {
    pub fn delete_greatest_value(mut grid: Vec<Vec<i32>>) -> i32 {
        for row in &mut grid {
            row.sort_unstable();
        }
        let mut ans = 0;
        let n = grid[0].len();
        for c in 0..n {
            let mut mx = 0;
            for row in &grid {
                if row[c] > mx {
                    mx = row[c];
                }
            }
            ans += mx;
        }
        ans
    }
}

fn main() {}
