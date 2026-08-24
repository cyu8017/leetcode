// LeetCode 2784 - Check if Array is Good
// https://leetcode.com/problems/check-if-array-is-good/

impl Solution {
    pub fn is_good(nums: Vec<i32>) -> bool {
        let n = nums.len() as i32 - 1;
        if n < 1 {
            return false;
        }
        let mut freq = vec![0; (n + 1) as usize];
        for v in nums {
            if v < 1 || v > n {
                return false;
            }
            freq[v as usize] += 1;
        }
        for i in 1..n {
            if freq[i as usize] != 1 {
                return false;
            }
        }
        freq[n as usize] == 2
    }
}
