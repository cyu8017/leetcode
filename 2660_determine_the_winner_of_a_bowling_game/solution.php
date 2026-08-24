<?php
// LeetCode 2660 - Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

class Solution {
    function isWinner($player1, $player2) {
        $score = function($p) {
            $s = 0;
            for ($i = 0; $i < count($p); $i++) {
                $mul = 1;
                if (($i > 0 && $p[$i - 1] === 10) || ($i > 1 && $p[$i - 2] === 10)) $mul = 2;
                $s += $mul * $p[$i];
            }
            return $s;
        };
        $a = $score($player1);
        $b = $score($player2);
        if ($a > $b) return 1;
        if ($b > $a) return 2;
        return 0;
    }
}
