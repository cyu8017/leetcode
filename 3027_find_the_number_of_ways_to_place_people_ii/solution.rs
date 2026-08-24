// LeetCode 3027 - Find the Number of Ways to Place People II
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

impl Solution {
    pub fn number_of_pairs(mut points: Vec<Vec<i32>>) -> i32 {
        points.sort_by(|a, b| a[0].cmp(&b[0]).then(b[1].cmp(&a[1])));
        let mut ans = 0;
        for i in 0..points.len() {
            let y1 = points[i][1];
            let mut max_y = i32::MIN;
            for j in (i + 1)..points.len() {
                let y2 = points[j][1];
                if max_y < y2 && y2 <= y1 {
                    max_y = y2;
                    ans += 1;
                }
            }
        }
        ans
    }
}
