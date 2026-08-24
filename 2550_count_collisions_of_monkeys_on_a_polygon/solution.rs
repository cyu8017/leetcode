// LeetCode 2550 - Count Collisions of Monkeys on a Polygon
// https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

impl Solution {
    pub fn monkey_move(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        fn powmod(mut a: i64, mut e: i32) -> i32 {
            let mut res = 1i64;
            while e > 0 {
                if e & 1 == 1 {
                    res = res * a % MOD;
                }
                a = a * a % MOD;
                e >>= 1;
            }
            res as i32
        }
        (powmod(2, n) as i64 - 2 + MOD) as i32 % MOD as i32
    }
}
