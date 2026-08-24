<?php
// LeetCode 3694 - Distinct Points Reachable After Substring Removal
// https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/

class Solution {
    function distinctPoints($s, $k) {
        $n = strlen($s);
        $f = array_fill(0, $n + 1, 0);
        $g = array_fill(0, $n + 1, 0);
        $x = 0;
        $y = 0;
        for ($i = 1; $i <= $n; $i++) {
            $c = $s[$i - 1];
            if ($c === 'U') $y++;
            else if ($c === 'D') $y--;
            else if ($c === 'L') $x--;
            else $x++;
            $f[$i] = $x;
            $g[$i] = $y;
        }
        $st = [];
        for ($i = $k; $i <= $n; $i++) {
            $a = $f[$n] - ($f[$i] - $f[$i - $k]);
            $b = $g[$n] - ($g[$i] - $g[$i - $k]);
            $st[$a . ',' . $b] = true;
        }
        return count($st);
    }
}
