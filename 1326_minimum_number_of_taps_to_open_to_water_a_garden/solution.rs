// LeetCode 1326 - Minimum Number of Taps to Open to Water a Garden
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

impl Solution {
    pub fn min_taps(n: i32, ranges: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut farthest = vec![0usize; n + 1];
        for (center, &radius) in ranges.iter().enumerate() {
            let left = center.saturating_sub(radius as usize);
            let right = (center + radius as usize).min(n);
            farthest[left] = farthest[left].max(right);
        }
        let mut taps = 0;
        let mut end = 0usize;
        let mut reach = 0usize;
        for position in 0..n {
            reach = reach.max(farthest[position]);
            if position == end {
                if reach <= position {
                    return -1;
                }
                taps += 1;
                end = reach;
            }
        }
        taps
    }
}
