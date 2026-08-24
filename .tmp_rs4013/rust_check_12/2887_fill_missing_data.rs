struct Solution;
// LeetCode 2887 - Fill Missing Data
// https://leetcode.com/problems/fill-missing-data/

impl Solution {
    pub fn fill_missing_values(products: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        products
            .into_iter()
            .map(|mut r| {
                if r.len() > 1 && r[1] < 0 {
                    r[1] = 0;
                }
                r
            })
            .collect()
    }
}

fn main() {}
