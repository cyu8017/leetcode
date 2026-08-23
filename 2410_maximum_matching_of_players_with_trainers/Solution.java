// LeetCode 2410 - Maximum Matching of Players With Trainers
// https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

import java.util.Arrays;

class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        Arrays.sort(players);
        Arrays.sort(trainers);
        int i = 0, j = 0, ans = 0;
        while (i < players.length && j < trainers.length) {
            if (players[i] <= trainers[j]) { ans++; i++; j++; }
            else j++;
        }
        return ans;
    }
}
