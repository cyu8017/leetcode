// LeetCode 3653 - XOR After Range Multiplication Queries I
// https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

impl Solution {
    pub fn xor_after_queries(mut nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        for q in queries {
            let l = q[0] as usize;
            let r = q[1] as usize;
            let k = q[2] as usize;
            let v = q[3] as i64;
            let mut idx = l;
            while idx <= r {
                nums[idx] = ((nums[idx] as i64 * v) % MOD) as i32;
                idx += k;
            }
        }
        let mut ans = 0;
        for x in nums {
            ans ^= x;
        }
        ans
    }
}
