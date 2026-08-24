// LeetCode 2677 - Chunk Array
// https://leetcode.com/problems/chunk-array/

impl Solution {
    pub fn chunk(arr: Vec<i32>, size: i32) -> Vec<Vec<i32>> {
        let size = size as usize;
        let mut ans = Vec::new();
        let mut i = 0;
        while i < arr.len() {
            let end = (i + size).min(arr.len());
            ans.push(arr[i..end].to_vec());
            i += size;
        }
        ans
    }
}
