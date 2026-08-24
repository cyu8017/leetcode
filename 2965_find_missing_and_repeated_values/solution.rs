// LeetCode 2965 - Find Missing and Repeated Values
// https://leetcode.com/problems/find-missing-and-repeated-values/

impl Solution {
    pub fn find_missing_and_repeated_values(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let n = grid.len();
        let mut freq = vec![0; n * n + 1];
        for row in &grid {
            for &v in row {
                freq[v as usize] += 1;
            }
        }
        let mut rep = 0;
        let mut miss = 0;
        for i in 1..=n * n {
            if freq[i] == 2 {
                rep = i as i32;
            }
            if freq[i] == 0 {
                miss = i as i32;
            }
        }
        vec![rep, miss]
    }
}
