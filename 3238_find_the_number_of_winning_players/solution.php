<?php
// LeetCode 3238 - Find the Number of Winning Players
// https://leetcode.com/problems/find-the-number-of-winning-players/

class Solution {
    function winningPlayerCount($n, $pick) {
        $cnt = [];
        for ($i = 0; $i < $n; $i++) $cnt[$i] = array_fill(0, 11, 0);
        $s = [];
        foreach ($pick as $p) {
            $x = $p[0];
            $y = $p[1];
            $cnt[$x][$y]++;
            if ($cnt[$x][$y] > $x) $s[$x] = true;
        }
        return count($s);
    }
}
