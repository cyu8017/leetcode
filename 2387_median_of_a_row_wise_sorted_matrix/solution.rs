// LeetCode 2387 - Median of a Row Wise Sorted Matrix
// https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/

impl Solution {
    pub fn matrix_median(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut lo = 1;
        let mut hi = 1_000_000;
        let need = (m * n) / 2 + 1;
        let count_le = |x: i32| {
            let mut cnt = 0;
            for row in &grid {
                let mut l = 0;
                let mut r = n;
                while l < r {
                    let mid = (l + r) / 2;
                    if row[mid] <= x {
                        l = mid + 1;
                    } else {
                        r = mid;
                    }
                }
                cnt += l;
            }
            cnt
        };
        while lo < hi {
            let mid = (lo + hi) / 2;
            if count_le(mid) >= need {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }
}
