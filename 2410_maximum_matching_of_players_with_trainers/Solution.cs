// LeetCode 2410 - Maximum Matching of Players With Trainers
// https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

using System;

public class Solution {
    public int MatchPlayersAndTrainers(int[] players, int[] trainers) {
        Array.Sort(players);
        Array.Sort(trainers);
        int i = 0, j = 0, ans = 0;
        while (i < players.Length && j < trainers.Length) {
            if (players[i] <= trainers[j]) { ans++; i++; j++; }
            else j++;
        }
        return ans;
    }
}
