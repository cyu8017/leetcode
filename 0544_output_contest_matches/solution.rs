// LeetCode 0544 - Output Contest Matches
// https://leetcode.com/problems/output-contest-matches/

impl Solution {
    pub fn find_contest_match(n: i32) -> String {
        let mut teams: Vec<String> = (1..=n).map(|team| team.to_string()).collect();

        while teams.len() > 1 {
            let mut next_round = Vec::with_capacity(teams.len() / 2);
            for index in 0..teams.len() / 2 {
                let right = teams.len() - 1 - index;
                next_round.push(format!("({},{})", teams[index], teams[right]));
            }
            teams = next_round;
        }

        teams.pop().unwrap_or_default()
    }
}
