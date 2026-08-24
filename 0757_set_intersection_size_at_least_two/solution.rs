// LeetCode 0757 - Set Intersection Size At Least Two
// https://leetcode.com/problems/set-intersection-size-at-least-two/

impl Solution {
    pub fn intersection_size_two(mut intervals: Vec<Vec<i32>>) -> i32 {
        intervals.sort_by(|a, b| {
            if a[1] != b[1] {
                a[1].cmp(&b[1])
            } else {
                a[0].cmp(&b[0])
            }
        });
        let mut size = 0;
        let mut first = -1;
        let mut second = -1;
        for interval in intervals {
            let left = interval[0];
            let right = interval[1];
            if left <= first {
                continue;
            }
            if left <= second {
                size += 1;
                first = second;
                second = right;
            } else {
                size += 2;
                first = right - 1;
                second = right;
            }
        }
        size
    }
}
