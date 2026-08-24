<?php
// LeetCode 3968 - Maximum Manhattan Distance After All Moves
// https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/

class Solution {
    function maxDistance($moves) {
        $x = 0;
        $y = 0;
        $z = 0;
        $n = strlen($moves);
        for ($i = 0; $i < $n; $i++) {
            $c = $moves[$i];
            if ($c == 'U') $x -= 1;
            else if ($c == 'D') $x += 1;
            else if ($c == 'L') $y -= 1;
            else if ($c == 'R') $y += 1;
            else $z += 1;
        }
        return abs($x) + abs($y) + $z;
    }
}
