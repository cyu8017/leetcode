// LeetCode 0875 - Koko Eating Bananas
// https://leetcode.com/problems/koko-eating-bananas/

impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let mut lo = 1;
        let mut hi = *piles.iter().max().unwrap();
        while lo < hi {
            let mid = (lo + hi) / 2;
            let hours: i64 = piles.iter().map(|&p| (p as i64 + mid as i64 - 1) / mid as i64).sum();
            if hours <= h as i64 {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
