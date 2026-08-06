// LeetCode 1536 - Minimum Swaps to Arrange a Binary Grid
// https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

impl Solution {
    pub fn min_swaps(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut zeros: Vec<i32> = grid
            .iter()
            .map(|row| {
                let mut count = 0;
                for j in (0..n).rev() {
                    if row[j] != 0 {
                        break;
                    }
                    count += 1;
                }
                count
            })
            .collect();
        let mut answer = 0;
        for i in 0..n {
            let required = (n - i - 1) as i32;
            let mut j = i;
            while j < n && zeros[j] < required {
                j += 1;
            }
            if j == n {
                return -1;
            }
            answer += (j - i) as i32;
            let val = zeros[j];
            for k in (i..j).rev() {
                zeros[k + 1] = zeros[k];
            }
            zeros[i] = val;
        }
        answer
    }
}
