// LeetCode 0078 - Subsets
// https://leetcode.com/problems/subsets/

impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut result = vec![vec![]];

        for num in nums {
            let size = result.len();
            for i in 0..size {
                let mut subset = result[i].clone();
                subset.push(num);
                result.push(subset);
            }
        }

        result
    }
}
