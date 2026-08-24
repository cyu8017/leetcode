// LeetCode 2410 - Maximum Matching of Players With Trainers
// https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

export function matchPlayersAndTrainers(players: number[], trainers: number[]): number {
    players = players.slice().sort((a, b) => a - b);
    trainers = trainers.slice().sort((a, b) => a - b);
    let i = 0, j = 0, ans = 0;
    while (i < players.length && j < trainers.length) {
        if (players[i] <= trainers[j]) { ans++; i++; j++; }
        else j++;
    }
    return ans;
}
