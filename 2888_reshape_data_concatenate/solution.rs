// LeetCode 2888 - Reshape Data: Concatenate
// https://leetcode.com/problems/reshape-data-concatenate/

impl Solution {
    pub fn concatenate_tables(mut df1: Vec<Vec<i32>>, df2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        df1.extend(df2);
        df1
    }
}
