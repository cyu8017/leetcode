// LeetCode 1007 - Minimum Domino Rotations For Equal Row
// https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

impl Solution {
    pub fn min_domino_rotations(tops: Vec<i32>, bottoms: Vec<i32>) -> i32 {
        fn check(target: i32, tops: &[i32], bottoms: &[i32]) -> i32 {
            let mut rot_top = 0;
            let mut rot_bot = 0;
            for (&t, &b) in tops.iter().zip(bottoms.iter()) {
                if t != target && b != target {
                    return i32::MAX;
                }
                if t != target {
                    rot_top += 1;
                }
                if b != target {
                    rot_bot += 1;
                }
            }
            rot_top.min(rot_bot)
        }
        let ans = check(tops[0], &tops, &bottoms).min(check(bottoms[0], &tops, &bottoms));
        if ans == i32::MAX {
            -1
        } else {
            ans
        }
    }
}
