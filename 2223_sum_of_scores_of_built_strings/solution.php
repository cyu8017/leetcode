<?php
// LeetCode 2223 - Sum of Scores of Built Strings
// https://leetcode.com/problems/sum-of-scores-of-built-strings/

class Solution {
    function sumScores($s) {
        $n = strlen($s);
        $z = array_fill(0, $n, 0);
        $l = 0;
        $r = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($i <= $r) $z[$i] = min($r - $i + 1, $z[$i - $l]);
            while ($i + $z[$i] < $n && $s[$z[$i]] === $s[$i + $z[$i]]) $z[$i]++;
            if ($i + $z[$i] - 1 > $r) { $l = $i; $r = $i + $z[$i] - 1; }
        }
        $ans = $n;
        for ($i = 1; $i < $n; $i++) $ans += $z[$i];
        return $ans;
    }
}
