struct Solution;
// LeetCode 2917 - Find the K-or of an Array
// https://leetcode.com/problems/find-the-k-or-of-an-array/

impl Solution {
    pub fn find_k_or(nums: Vec<i32>, k: i32) -> i32 {
        let mut ans = 0;
        for b in 0..31 {
            let mut cnt = 0;
            for &v in &nums {
                if (v & (1 << b)) != 0 {
                    cnt += 1;
                }
            }
            if cnt >= k {
                ans |= 1 << b;
            }
        }
        ans
    }
}

fn main() {}
