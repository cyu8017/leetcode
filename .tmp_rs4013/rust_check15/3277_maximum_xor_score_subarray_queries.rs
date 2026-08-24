struct Solution;
// LeetCode 3277 - Maximum XOR Score Subarray Queries
// https://leetcode.com/problems/maximum-xor-score-subarray-queries/

impl Solution {
    pub fn maximum_subarray_xor(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = nums.len();
        let mut f = vec![vec![0; n]; n];
        for i in 0..n {
            f[i][i] = nums[i];
        }
        for length in 2..=n {
            for i in 0..=n - length {
                let j = i + length - 1;
                f[i][j] = f[i][j - 1] ^ f[i + 1][j];
            }
        }
        let mut best = vec![vec![0; n]; n];
        for i in 0..n {
            best[i][i] = f[i][i];
        }
        for length in 2..=n {
            for i in 0..=n - length {
                let j = i + length - 1;
                best[i][j] = f[i][j].max(best[i][j - 1]).max(best[i + 1][j]);
            }
        }
        queries.iter().map(|q| best[q[0] as usize][q[1] as usize]).collect()
    }
}

fn main() {}
