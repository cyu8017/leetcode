// LeetCode 2064 - Minimized Maximum of Products Distributed to Any Store
// https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

impl Solution {
    pub fn minimized_maximum(n: i32, quantities: Vec<i32>) -> i32 {
        let can = |x: i32| -> bool {
            let mut need = 0i32;
            for &q in &quantities {
                need += (q + x - 1) / x;
                if need > n {
                    return false;
                }
            }
            true
        };
        let mut lo = 1;
        let mut hi = *quantities.iter().max().unwrap();
        while lo < hi {
            let mid = (lo + hi) / 2;
            if can(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
