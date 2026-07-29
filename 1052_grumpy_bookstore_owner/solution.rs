// LeetCode 1052 - Grumpy Bookstore Owner
// https://leetcode.com/problems/grumpy-bookstore-owner/

impl Solution {
    pub fn max_satisfied(customers: Vec<i32>, grumpy: Vec<i32>, minutes: i32) -> i32 {
        let minutes = minutes as usize;
        let base: i32 = customers
            .iter()
            .zip(grumpy.iter())
            .filter(|(_, &g)| g == 0)
            .map(|(c, _)| *c)
            .sum();
        let mut gain = 0;
        let mut best = 0;
        for i in 0..customers.len() {
            if grumpy[i] == 1 {
                gain += customers[i];
            }
            if i >= minutes && grumpy[i - minutes] == 1 {
                gain -= customers[i - minutes];
            }
            best = best.max(gain);
        }
        base + best
    }
}
