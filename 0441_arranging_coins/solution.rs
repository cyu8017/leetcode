// LeetCode 0441 - Arranging Coins
// https://leetcode.com/problems/arranging-coins/

impl Solution {
    pub fn arrange_coins(n: i32) -> i32 {
        let mut low = 0;
        let mut high = n;
        while low <= high {
            let mid = low + (high - low) / 2;
            if i64::from(mid) * i64::from(mid + 1) / 2 <= i64::from(n) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        high
    }
}
