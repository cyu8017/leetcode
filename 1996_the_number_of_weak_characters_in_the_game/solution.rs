// LeetCode 1996 - The Number of Weak Characters in the Game
// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

impl Solution {
    pub fn number_of_weak_characters(mut properties: Vec<Vec<i32>>) -> i32 {
        properties.sort_by(|a, b| a[0].cmp(&b[0]).then(b[1].cmp(&a[1])));
        let mut ans = 0;
        let mut max_def = 0;
        for i in (0..properties.len()).rev() {
            if properties[i][1] < max_def {
                ans += 1;
            } else {
                max_def = properties[i][1];
            }
        }
        ans
    }
}
