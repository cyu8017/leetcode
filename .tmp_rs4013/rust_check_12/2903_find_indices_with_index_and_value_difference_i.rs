struct Solution;
// LeetCode 2903 - Find Indices With Index and Value Difference I
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

impl Solution {
    pub fn find_indices(nums: Vec<i32>, index_difference: i32, value_difference: i32) -> Vec<i32> {
        let n = nums.len();
        for i in 0..n {
            for j in i..n {
                let di = (j as i32 - i as i32).abs();
                let dv = (nums[i] - nums[j]).abs();
                if di >= index_difference && dv >= value_difference {
                    return vec![i as i32, j as i32];
                }
            }
        }
        vec![-1, -1]
    }
}

fn main() {}
