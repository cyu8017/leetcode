// LeetCode 1552 - Magnetic Force Between Two Balls
// https://leetcode.com/problems/magnetic-force-between-two-balls/

impl Solution {
    pub fn max_distance(mut position: Vec<i32>, m: i32) -> i32 {
        position.sort_unstable();
        let mut lo = 1;
        let mut hi = (position[position.len() - 1] - position[0]) / (m - 1);
        while lo <= hi {
            let mid = (lo + hi) / 2;
            let mut count = 1;
            let mut last = position[0];
            for &x in &position[1..] {
                if x - last >= mid {
                    count += 1;
                    last = x;
                }
            }
            if count >= m {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        hi
    }
}
