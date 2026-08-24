// LeetCode 3152 - Special Array II
// https://leetcode.com/problems/special-array-ii/

impl Solution {
    pub fn is_array_special(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let n = nums.len();
        let mut d = vec![0; n];
        for i in 0..n {
            d[i] = i;
        }
        for i in 1..n {
            if nums[i] % 2 != nums[i - 1] % 2 {
                d[i] = d[i - 1];
            }
        }
        queries.iter().map(|q| d[q[1] as usize] <= q[0] as usize).collect()
    }
}
