struct Solution;
// LeetCode 2438 - Range Product Queries of Powers
// https://leetcode.com/problems/range-product-queries-of-powers/

impl Solution {
    pub fn product_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        const MOD: i64 = 1_000_000_007;
        let mut powers = Vec::new();
        for bit in 0..31 {
            if (n >> bit) & 1 == 1 {
                powers.push(1 << bit);
            }
        }
        let mut ans = vec![0; queries.len()];
        for (i, q) in queries.iter().enumerate() {
            let mut prod = 1i64;
            for j in q[0] as usize..=q[1] as usize {
                prod = prod * powers[j] as i64 % MOD;
            }
            ans[i] = prod as i32;
        }
        ans
    }
}

fn main() {}
