// LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

impl Solution {
    pub fn largest_combination(candidates: Vec<i32>) -> i32 {
        let mut ans = 0;
        for bit in 0..24 {
            let mut cnt = 0;
            for &x in &candidates {
                if (x >> bit) & 1 == 1 {
                    cnt += 1;
                }
            }
            ans = ans.max(cnt);
        }
        ans
    }
}
