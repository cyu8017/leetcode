// LeetCode 1462 - Course Schedule IV
// https://leetcode.com/problems/course-schedule-iv/

impl Solution {
    pub fn check_if_prerequisite(
        num_courses: i32,
        prerequisites: Vec<Vec<i32>>,
        queries: Vec<Vec<i32>>,
    ) -> Vec<bool> {
        let n = num_courses as usize;
        let mut reach = vec![vec![false; n]; n];
        for e in prerequisites {
            reach[e[0] as usize][e[1] as usize] = true;
        }
        for k in 0..n {
            for i in 0..n {
                if reach[i][k] {
                    for j in 0..n {
                        reach[i][j] |= reach[k][j];
                    }
                }
            }
        }
        queries
            .into_iter()
            .map(|q| reach[q[0] as usize][q[1] as usize])
            .collect()
    }
}
