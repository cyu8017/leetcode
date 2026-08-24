struct Solution;
// LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

impl Solution {
    pub fn max_profit(prices: Vec<i32>, profits: Vec<i32>) -> i32 {
        let n = prices.len();
        let mut ans = -1;
        let mut max_left = vec![-1i32; n];
        let mut bit = vec![0i32; 5002];
        let update = |bit: &mut [i32], mut i: usize, val: i32| {
            while i < bit.len() {
                if val > bit[i] {
                    bit[i] = val;
                }
                i += i & i.wrapping_neg();
            }
        };
        let query = |bit: &[i32], mut i: usize| -> i32 {
            let mut best = -1;
            while i > 0 {
                if bit[i] > best {
                    best = bit[i];
                }
                i -= i & i.wrapping_neg();
            }
            best
        };
        for j in 0..n {
            max_left[j] = query(&bit, (prices[j] - 1) as usize);
            update(&mut bit, prices[j] as usize, profits[j]);
        }
        for j in 0..n {
            let mut best_r = -1;
            for k in j + 1..n {
                if prices[k] > prices[j] && profits[k] > best_r {
                    best_r = profits[k];
                }
            }
            if max_left[j] >= 0 && best_r >= 0 {
                ans = ans.max(max_left[j] + profits[j] + best_r);
            }
        }
        ans
    }
}

fn main() {}
