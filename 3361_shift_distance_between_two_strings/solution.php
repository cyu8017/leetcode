<?php
// LeetCode 3361 - Shift Distance Between Two Strings
// https://leetcode.com/problems/shift-distance-between-two-strings/

class Solution {
    function shiftDistance($s, $t, $nextCost, $previousCost) {
        $ans = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $a = ord($s[$i]) - 97;
            $b = ord($t[$i]) - 97;
            if ($a === $b) continue;
            $fwd = 0;
            for ($x = $a; $x !== $b; $x = ($x + 1) % 26) $fwd += $nextCost[$x];
            $bwd = 0;
            for ($x = $a; $x !== $b; $x = ($x + 25) % 26) $bwd += $previousCost[$x];
            $ans += $fwd < $bwd ? $fwd : $bwd;
        }
        return $ans;
    }
}
