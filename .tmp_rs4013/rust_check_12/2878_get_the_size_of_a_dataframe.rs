struct Solution;
// LeetCode 2878 - Get the Size of a DataFrame
// https://leetcode.com/problems/get-the-size-of-a-dataframe/

impl Solution {
    pub fn get_dataframe_size(players: Vec<Vec<i32>>) -> Vec<i32> {
        if players.is_empty() {
            return vec![0, 0];
        }
        vec![players.len() as i32, players[0].len() as i32]
    }
}

fn main() {}
