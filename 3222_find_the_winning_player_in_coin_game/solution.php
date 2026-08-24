<?php
// LeetCode 3222 - Find the Winning Player in Coin Game
// https://leetcode.com/problems/find-the-winning-player-in-coin-game/

class Solution {
    function winningPlayer($x, $y) {
        $k = min(intdiv($x, 2), intdiv($y, 8));
        $x -= 2 * $k;
        $y -= 8 * $k;
        if ($x > 0 && $y >= 4) return "Alice";
        return "Bob";
    }
}
