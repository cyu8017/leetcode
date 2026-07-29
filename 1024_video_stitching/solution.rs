// LeetCode 1024 - Video Stitching
// https://leetcode.com/problems/video-stitching/

impl Solution {
    pub fn video_stitching(clips: Vec<Vec<i32>>, time: i32) -> i32 {
        let time = time as usize;
        let mut furthest = vec![0usize; time + 1];
        for clip in clips {
            let start = clip[0] as usize;
            let end = clip[1] as usize;
            if start <= time {
                furthest[start] = furthest[start].max(end);
            }
        }
        let mut ans = 0;
        let mut reach = 0usize;
        let mut next_reach = 0usize;
        for i in 0..time {
            next_reach = next_reach.max(furthest[i]);
            if i == reach {
                if next_reach <= i {
                    return -1;
                }
                ans += 1;
                reach = next_reach;
            }
        }
        ans
    }
}
