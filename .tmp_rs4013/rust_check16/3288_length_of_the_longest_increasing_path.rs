struct Solution;
// LeetCode 3288 - Length of the Longest Increasing Path
// https://leetcode.com/problems/length-of-the-longest-increasing-path/

impl Solution {
    fn lis(a: &[i32]) -> i32 {
        let mut tails = Vec::new();
        for &x in a {
            match tails.binary_search(&x) {
                Ok(_) => {}
                Err(i) => {
                    if i == tails.len() {
                        tails.push(x);
                    } else {
                        tails[i] = x;
                    }
                }
            }
        }
        tails.len() as i32
    }

    pub fn max_path_length(coordinates: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = coordinates.len();
        let mut arr: Vec<(i32, i32, usize)> = (0..n)
            .map(|i| (coordinates[i][0], coordinates[i][1], i))
            .collect();
        arr.sort_by(|a, b| {
            if a.0 == b.0 {
                b.1.cmp(&a.1)
            } else {
                a.0.cmp(&b.0)
            }
        });
        let kx = coordinates[k as usize][0];
        let ky = coordinates[k as usize][1];
        let mut left = Vec::new();
        let mut right = Vec::new();
        for p in &arr {
            if p.0 < kx && p.1 < ky {
                left.push(p.1);
            }
            if p.0 > kx && p.1 > ky {
                right.push(p.1);
            }
        }
        Self::lis(&left) + 1 + Self::lis(&right)
    }
}

fn main() {}
