// LeetCode 2483 - Minimum Penalty for a Shop
// https://leetcode.com/problems/minimum-penalty-for-a-shop/

impl Solution {
    pub fn best_closing_time(customers: String) -> i32 {
        let b = customers.as_bytes();
        let mut penalty = b.iter().filter(|&&c| c == b'Y').count() as i32;
        let mut best = penalty;
        let mut ans = 0;
        for (i, &c) in b.iter().enumerate() {
            if c == b'Y' {
                penalty -= 1;
            } else {
                penalty += 1;
            }
            if penalty < best {
                best = penalty;
                ans = i as i32 + 1;
            }
        }
        ans
    }
}
