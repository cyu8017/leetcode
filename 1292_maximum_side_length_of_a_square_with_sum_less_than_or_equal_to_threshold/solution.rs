// LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
// https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

impl Solution {
    pub fn max_side_length(mat: Vec<Vec<i32>>, threshold: i32) -> i32 {
        let m = mat.len();
        let n = mat[0].len();
        let mut prefix = vec![vec![0; n + 1]; m + 1];
        for r in 0..m {
            for c in 0..n {
                prefix[r + 1][c + 1] =
                    mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c];
            }
        }
        let possible = |size: usize| -> bool {
            for r in size..=m {
                for c in size..=n {
                    let sum = prefix[r][c] - prefix[r - size][c] - prefix[r][c - size]
                        + prefix[r - size][c - size];
                    if sum <= threshold {
                        return true;
                    }
                }
            }
            false
        };
        let mut lo = 0usize;
        let mut hi = m.min(n);
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if possible(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo as i32
    }
}
