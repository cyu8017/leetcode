struct Solution;
// LeetCode 3946 - Maximum Number Of Items From Sale I
// https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

impl Solution {
    pub fn maximum_sale_items(items: Vec<Vec<i32>>, budget: i32) -> i32 {
        let mut f = vec![0; (budget + 1) as usize];
        let mut mn = i32::MAX;
        for item in &items {
            let factor = item[0];
            let price = item[1];
            mn = mn.min(price);
            let mut cnt = 0;
            for j_item in &items {
                if j_item[0] % factor == 0 {
                    cnt += 1;
                }
            }
            for j in (price..=budget).rev() {
                f[j as usize] = f[j as usize].max(f[(j - price) as usize] + cnt);
            }
        }
        let mut ans = 0;
        for i in 0..=budget {
            let extra = (budget - i) / mn;
            ans = ans.max(f[i as usize] + extra);
        }
        ans
    }
}

fn main() {}
