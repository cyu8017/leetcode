struct Solution;
// LeetCode 3363 - Find the Maximum Number of Fruits Collected
// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

impl Solution {
    pub fn max_collected_fruits(mut fruits: Vec<Vec<i32>>) -> i32 {
        let n = fruits.len();
        let mut ans = 0;
        for i in 0..n {
            ans += fruits[i][i];
            fruits[i][i] = 0;
        }
        const NEG: i32 = -(1 << 30);
        let mut dp2 = vec![vec![NEG; n]; n];
        let mut dp3 = vec![vec![NEG; n]; n];
        dp2[0][n - 1] = fruits[0][n - 1];
        for i in 0..n {
            for j in 0..n {
                if dp2[i][j] == NEG {
                    continue;
                }
                for dj in [-1, 0, 1] {
                    let ni = i as i32 + 1;
                    let nj = j as i32 + dj;
                    if ni < n as i32 && nj >= 0 && nj < n as i32 && nj > ni {
                        let v = dp2[i][j] + fruits[ni as usize][nj as usize];
                        if v > dp2[ni as usize][nj as usize] {
                            dp2[ni as usize][nj as usize] = v;
                        }
                    }
                }
            }
        }
        dp3[n - 1][0] = fruits[n - 1][0];
        for j in 0..n {
            for i in 0..n {
                if dp3[i][j] == NEG {
                    continue;
                }
                for di in [-1, 0, 1] {
                    let ni = i as i32 + di;
                    let nj = j as i32 + 1;
                    if ni >= 0 && ni < n as i32 && nj < n as i32 && ni > nj {
                        let v = dp3[i][j] + fruits[ni as usize][nj as usize];
                        if v > dp3[ni as usize][nj as usize] {
                            dp3[ni as usize][nj as usize] = v;
                        }
                    }
                }
            }
        }
        ans += dp2[n - 1][n - 1] + dp3[n - 1][n - 1];
        ans
    }
}

fn main() {}
