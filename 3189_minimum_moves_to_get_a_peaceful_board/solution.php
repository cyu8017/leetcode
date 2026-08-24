<?php
// LeetCode 3189 - Minimum Moves to Get a Peaceful Board
// https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

class Solution {
    function minMoves($rooks) {
        $ans = 0;
        usort($rooks, function($a, $b) { return $a[0] <=> $b[0]; });
        for ($i = 0; $i < count($rooks); $i++) $ans += abs($rooks[$i][0] - $i);
        usort($rooks, function($a, $b) { return $a[1] <=> $b[1]; });
        for ($j = 0; $j < count($rooks); $j++) $ans += abs($rooks[$j][1] - $j);
        return $ans;
    }
}
