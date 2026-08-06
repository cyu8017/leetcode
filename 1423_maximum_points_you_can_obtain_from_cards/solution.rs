// LeetCode 1423 - Maximum Points You Can Obtain from Cards
// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

impl Solution {
    pub fn max_score(card_points: Vec<i32>, k: i32) -> i32 {
        let n = card_points.len();
        let k = k as usize;
        if k == n {
            return card_points.iter().sum();
        }
        let window = n - k;
        let mut current: i32 = card_points[..window].iter().sum();
        let mut smallest = current;
        for i in window..n {
            current += card_points[i] - card_points[i - window];
            smallest = smallest.min(current);
        }
        card_points.iter().sum::<i32>() - smallest
    }
}
