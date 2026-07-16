// LeetCode 0544 - Output Contest Matches
// https://leetcode.com/problems/output-contest-matches/

class Solution {
    findContestMatch(n) {
        let teams = Array.from({ length: n }, (_, i) => String(i + 1));
        while (teams.length > 1) {
            const nextRound = [];
            for (let i = 0; i < teams.length / 2; i++) {
                nextRound.push(`(${teams[i]},${teams[teams.length - 1 - i]})`);
            }
            teams = nextRound;
        }
        return teams[0];
    }
}

module.exports = { Solution };
