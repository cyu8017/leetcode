// LeetCode 3577 - Count the Number of Computer Unlocking Permutations
// https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

impl Solution {
    pub fn count_permutations(complexity: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut ans = 1i64;
        for i in 1..complexity.len() {
            if complexity[i] <= complexity[0] {
                return 0;
            }
            ans = ans * i as i64 % MOD;
        }
        ans as i32
    }
}
