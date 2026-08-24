<?php
// LeetCode 3320 - Count the Number of Winning Sequences
// https://leetcode.com/problems/count-the-number-of-winning-sequences/

class Solution {
    function countWinningSequences($s) {
        $mod = 1000000007;
        $n = strlen($s);
        $mp = ['F' => 0, 'W' => 1, 'E' => 2];
        $beat = [2, 0, 1];
        $score = [];
        for ($a = 0; $a < 3; $a++) {
            for ($b = 0; $b < 3; $b++) {
                if ($a === $b) $score[$a][$b] = 0;
                else if ($beat[$a] === $b) $score[$a][$b] = 1;
                else $score[$a][$b] = -1;
            }
        }
        $offset = $n;
        $dp = [];
        for ($a = 0; $a < 3; $a++) $dp[$a] = array_fill(0, 2 * $n + 1, 0);
        $b0 = $mp[$s[0]];
        for ($a = 0; $a < 3; $a++) $dp[$a][$score[$a][$b0] + $offset] = 1;
        for ($i = 1; $i < $n; $i++) {
            $ndp = [];
            for ($a = 0; $a < 3; $a++) $ndp[$a] = array_fill(0, 2 * $n + 1, 0);
            $b = $mp[$s[$i]];
            for ($last = 0; $last < 3; $last++) {
                for ($d = 0; $d <= 2 * $n; $d++) {
                    if ($dp[$last][$d] === 0) continue;
                    for ($a = 0; $a < 3; $a++) {
                        if ($a === $last) continue;
                        $nd = $d + $score[$a][$b];
                        if ($nd < 0 || $nd > 2 * $n) continue;
                        $ndp[$a][$nd] = ($ndp[$a][$nd] + $dp[$last][$d]) % $mod;
                    }
                }
            }
            $dp = $ndp;
        }
        $ans = 0;
        for ($a = 0; $a < 3; $a++) {
            for ($d = $offset + 1; $d <= 2 * $n; $d++) $ans = ($ans + $dp[$a][$d]) % $mod;
        }
        return $ans;
    }
}
