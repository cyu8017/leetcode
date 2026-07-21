// LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

use std::collections::HashMap;

impl Solution {
    pub fn earliest_and_latest(n: i32, first_player: i32, second_player: i32) -> Vec<i32> {
        let first = first_player;
        let second = second_player;
        let mut memo: HashMap<Vec<i32>, (i32, i32)> = HashMap::new();

        fn dfs(
            players: Vec<i32>,
            first: i32,
            second: i32,
            memo: &mut HashMap<Vec<i32>, (i32, i32)>,
        ) -> (i32, i32) {
            if let Some(&cached) = memo.get(&players) {
                return cached;
            }
            let count = players.len();
            let first_index = players.iter().position(|&p| p == first).unwrap();
            let second_index = players.iter().position(|&p| p == second).unwrap();
            if first_index + second_index == count - 1 {
                memo.insert(players, (1, 1));
                return (1, 1);
            }

            let mut choices: Vec<Vec<i32>> = Vec::new();
            for index in 0..count / 2 {
                let left = players[index];
                let right = players[count - 1 - index];
                if left == first || left == second {
                    choices.push(vec![left]);
                } else if right == first || right == second {
                    choices.push(vec![right]);
                } else {
                    choices.push(vec![left, right]);
                }
            }
            if count % 2 == 1 {
                choices.push(vec![players[count / 2]]);
            }

            let mut earliest = i32::MAX;
            let mut latest = 0;
            let mut picks = Vec::new();
            enumerate(
                &choices,
                0,
                &mut picks,
                &mut earliest,
                &mut latest,
                first,
                second,
                memo,
            );
            memo.insert(players, (earliest, latest));
            (earliest, latest)
        }

        fn enumerate(
            choices: &[Vec<i32>],
            idx: usize,
            picks: &mut Vec<i32>,
            earliest: &mut i32,
            latest: &mut i32,
            first: i32,
            second: i32,
            memo: &mut HashMap<Vec<i32>, (i32, i32)>,
        ) {
            if idx == choices.len() {
                let mut winners = picks.clone();
                winners.sort_unstable();
                let (early, late) = dfs(winners, first, second, memo);
                *earliest = (*earliest).min(early + 1);
                *latest = (*latest).max(late + 1);
                return;
            }
            for &player in &choices[idx] {
                picks.push(player);
                enumerate(choices, idx + 1, picks, earliest, latest, first, second, memo);
                picks.pop();
            }
        }

        let players: Vec<i32> = (1..=n).collect();
        let (early, late) = dfs(players, first, second, &mut memo);
        vec![early, late]
    }
}
