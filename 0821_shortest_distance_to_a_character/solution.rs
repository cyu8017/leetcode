// LeetCode 0821 - Shortest Distance to a Character
// https://leetcode.com/problems/shortest-distance-to-a-character/

impl Solution {
    pub fn shortest_to_char(s: String, c: char) -> Vec<i32> {
        let chars: Vec<char> = s.chars().collect();
        let n = chars.len() as i32;
        let mut ans = vec![0; chars.len()];
        let mut prev = -n;
        for i in 0..chars.len() {
            if chars[i] == c {
                prev = i as i32;
            }
            ans[i] = i as i32 - prev;
        }
        prev = 2 * n;
        for i in (0..chars.len()).rev() {
            if chars[i] == c {
                prev = i as i32;
            }
            ans[i] = ans[i].min(prev - i as i32);
        }
        ans
    }
}
