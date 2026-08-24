// LeetCode 2211 - Count Collisions on a Road
// https://leetcode.com/problems/count-collisions-on-a-road/

impl Solution {
    pub fn count_collisions(directions: String) -> i32 {
        let d = directions.as_bytes();
        let mut i = 0;
        let mut j = d.len() as i32 - 1;
        while i < d.len() && d[i] == b'L' {
            i += 1;
        }
        while j >= 0 && d[j as usize] == b'R' {
            j -= 1;
        }
        let mut ans = 0;
        if j >= i as i32 {
            for k in i..=j as usize {
                if d[k] != b'S' {
                    ans += 1;
                }
            }
        }
        ans
    }
}
