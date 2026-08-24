struct Solution;
// LeetCode 3279 - Maximum Total Area Occupied by Pistons
// https://leetcode.com/problems/maximum-total-area-occupied-by-pistons/

impl Solution {
    pub fn max_area(height: i32, positions: Vec<i32>, directions: String) -> i64 {
        let n = positions.len();
        let mut pos = positions;
        let mut dir = directions.into_bytes();
        let mut best = 0i64;
        for _ in 0..=2 * height {
            let mut sum = 0i64;
            for &p in &pos {
                sum += p as i64;
            }
            if sum > best {
                best = sum;
            }
            for i in 0..n {
                if dir[i] == b'U' {
                    if pos[i] == height {
                        dir[i] = b'D';
                        pos[i] -= 1;
                    } else {
                        pos[i] += 1;
                    }
                } else if pos[i] == 0 {
                    dir[i] = b'U';
                    pos[i] += 1;
                } else {
                    pos[i] -= 1;
                }
            }
        }
        best
    }
}

fn main() {}
