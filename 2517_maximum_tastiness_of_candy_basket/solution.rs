// LeetCode 2517 - Maximum Tastiness of Candy Basket
// https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

impl Solution {
    pub fn maximum_tastiness(mut price: Vec<i32>, k: i32) -> i32 {
        price.sort_unstable();
        let ok = |d: i32| {
            let mut cnt = 1;
            let mut last = price[0];
            for i in 1..price.len() {
                if price[i] - last >= d {
                    cnt += 1;
                    last = price[i];
                    if cnt >= k {
                        return true;
                    }
                }
            }
            false
        };
        let mut lo = 0;
        let mut hi = price[price.len() - 1] - price[0];
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            if ok(mid) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        lo
    }
}
