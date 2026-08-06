// LeetCode 1964 - Find the Longest Valid Obstacle Course at Each Position
// https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

impl Solution {
    pub fn longest_obstacle_course_at_each_position(obstacles: Vec<i32>) -> Vec<i32> {
        let mut tails: Vec<i32> = Vec::new();
        let mut ans = Vec::with_capacity(obstacles.len());
        for x in obstacles {
            let i = tails.partition_point(|&y| y <= x);
            if i == tails.len() {
                tails.push(x);
            } else {
                tails[i] = x;
            }
            ans.push((i + 1) as i32);
        }
        ans
    }
}
