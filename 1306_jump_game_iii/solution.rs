// LeetCode 1306 - Jump Game III
// https://leetcode.com/problems/jump-game-iii/

impl Solution {
    pub fn can_reach(arr: Vec<i32>, start: i32) -> bool {
        let n = arr.len() as i32;
        let mut stack = vec![start];
        let mut seen = vec![false; arr.len()];
        while let Some(i) = stack.pop() {
            if i < 0 || i >= n || seen[i as usize] {
                continue;
            }
            if arr[i as usize] == 0 {
                return true;
            }
            seen[i as usize] = true;
            stack.push(i - arr[i as usize]);
            stack.push(i + arr[i as usize]);
        }
        false
    }
}
