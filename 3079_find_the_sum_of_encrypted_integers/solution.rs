// LeetCode 3079 - Find the Sum of Encrypted Integers
// https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

impl Solution {
    fn encrypt(mut x: i32) -> i32 {
        let mut mx = 0;
        let mut p = 0;
        while x > 0 {
            mx = mx.max(x % 10);
            p = p * 10 + 1;
            x /= 10;
        }
        mx * p
    }

    pub fn sum_of_encrypted_int(nums: Vec<i32>) -> i32 {
        nums.into_iter().map(Self::encrypt).sum()
    }
}
