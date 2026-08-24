struct Solution;
// LeetCode 0634 - Find the Derangement of An Array
// https://leetcode.com/problems/find-the-derangement-of-an-array/

impl Solution {
    pub fn find_derangement(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        if n == 1 {
            return 0;
        }
        let mut prev2 = 0i64;
        let mut prev1 = 1i64;
        for size in 3..=n {
            let next = (size as i64 - 1) * (prev1 + prev2) % MOD;
            prev2 = prev1;
            prev1 = next;
        }
        prev1 as i32
    }
}

fn main() {}
