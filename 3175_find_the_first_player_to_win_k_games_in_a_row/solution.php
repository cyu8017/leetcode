<?php
// LeetCode 3175 - Find The First Player to win K Games in a Row
// https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

class Solution {
    function findWinningPlayer($skills, $k) {
        $n = count($skills);
        $k = min($k, $n - 1);
        $i = 0;
        $cnt = 0;
        for ($j = 1; $j < $n; $j++) {
            if ($skills[$i] < $skills[$j]) { $i = $j; $cnt = 1; }
            else $cnt++;
            if ($cnt === $k) break;
        }
        return $i;
    }
}
