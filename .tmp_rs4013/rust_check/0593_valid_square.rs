struct Solution;
// LeetCode 0593 - Valid Square
// https://leetcode.com/problems/valid-square/

impl Solution {
    fn dist_sq(a: &[i32], b: &[i32]) -> i64 {
        let dx = a[0] as i64 - b[0] as i64;
        let dy = a[1] as i64 - b[1] as i64;
        dx * dx + dy * dy
    }

    pub fn valid_square(p1: Vec<i32>, p2: Vec<i32>, p3: Vec<i32>, p4: Vec<i32>) -> bool {
        let points = [p1, p2, p3, p4];
        let mut distances = Vec::new();
        for i in 0..4 {
            for j in i + 1..4 {
                distances.push(Self::dist_sq(&points[i], &points[j]));
            }
        }
        distances.sort_unstable();
        distances[0] > 0
            && distances[0] == distances[1]
            && distances[1] == distances[2]
            && distances[2] == distances[3]
            && distances[4] == distances[5]
            && distances[4] == 2 * distances[0]
    }
}

fn main() {}
