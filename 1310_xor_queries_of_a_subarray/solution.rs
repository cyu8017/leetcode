// LeetCode 1310 - XOR Queries of a Subarray
// https://leetcode.com/problems/xor-queries-of-a-subarray/

impl Solution {
    pub fn xor_queries(arr: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut prefix = vec![0; arr.len() + 1];
        for i in 0..arr.len() {
            prefix[i + 1] = prefix[i] ^ arr[i];
        }
        queries
            .into_iter()
            .map(|q| prefix[q[1] as usize + 1] ^ prefix[q[0] as usize])
            .collect()
    }
}
