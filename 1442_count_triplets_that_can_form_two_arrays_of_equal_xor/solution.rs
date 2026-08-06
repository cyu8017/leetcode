// LeetCode 1442 - Count Triplets That Can Form Two Arrays of Equal XOR
// https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

impl Solution {
    pub fn count_triplets(arr: Vec<i32>) -> i32 {
        let mut answer = 0;
        for i in 0..arr.len() {
            let mut value = 0;
            for k in i..arr.len() {
                value ^= arr[k];
                if value == 0 {
                    answer += (k - i) as i32;
                }
            }
        }
        answer
    }
}
