struct Solution;

// LeetCode 2548 - Maximum Price to Fill a Bag
// https://leetcode.com/problems/maximum-price-to-fill-a-bag/

impl Solution {
    pub fn max_price(mut items: Vec<Vec<i32>>, capacity: i32) -> f64 {
        items.sort_by(|a, b| {
            let ra = a[0] as f64 / a[1] as f64;
            let rb = b[0] as f64 / b[1] as f64;
            rb.partial_cmp(&ra).unwrap()
        });
        let mut ans = 0.0;
        let mut remain = capacity;
        for it in items {
            let price = it[0];
            let weight = it[1];
            if remain >= weight {
                ans += price as f64;
                remain -= weight;
            } else {
                ans += price as f64 * remain as f64 / weight as f64;
                remain = 0;
                break;
            }
        }
        if remain > 0 {
            -1.0
        } else {
            ans
        }
    }
}

fn main() {}
