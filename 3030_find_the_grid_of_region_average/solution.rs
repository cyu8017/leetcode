// LeetCode 3030 - Find the Grid of Region Average
// https://leetcode.com/problems/find-the-grid-of-region-average/

impl Solution {
    pub fn result_grid(image: Vec<Vec<i32>>, threshold: i32) -> Vec<Vec<i32>> {
        let n = image.len();
        let m = image[0].len();
        let mut ans = vec![vec![0; m]; n];
        let mut ct = vec![vec![0; m]; n];
        for i in 0..n.saturating_sub(2) {
            for j in 0..m.saturating_sub(2) {
                let mut region = true;
                for k in 0..3 {
                    for l in 0..2 {
                        region = region
                            && (image[i + k][j + l] - image[i + k][j + l + 1]).abs() <= threshold;
                    }
                }
                for k in 0..2 {
                    for l in 0..3 {
                        region = region
                            && (image[i + k][j + l] - image[i + k + 1][j + l]).abs() <= threshold;
                    }
                }
                if region {
                    let mut tot = 0;
                    for k in 0..3 {
                        for l in 0..3 {
                            tot += image[i + k][j + l];
                        }
                    }
                    for k in 0..3 {
                        for l in 0..3 {
                            ct[i + k][j + l] += 1;
                            ans[i + k][j + l] += tot / 9;
                        }
                    }
                }
            }
        }
        for i in 0..n {
            for j in 0..m {
                if ct[i][j] == 0 {
                    ans[i][j] = image[i][j];
                } else {
                    ans[i][j] /= ct[i][j];
                }
            }
        }
        ans
    }
}
