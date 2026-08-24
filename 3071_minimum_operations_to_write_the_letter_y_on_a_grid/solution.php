<?php
// LeetCode 3071 - Minimum Operations to Write the Letter Y on a Grid
// https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/

class Solution {
    function minimumOperationsToWriteY($grid) {
        $n = count($grid);
        $cnt1 = [0, 0, 0];
        $cnt2 = [0, 0, 0];
        $half = intdiv($n, 2);
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $x = $grid[$i][$j];
                $a = $i === $j && $i <= $half;
                $b = $i + $j === $n - 1 && $i <= $half;
                $c = $j === $half && $i >= $half;
                if ($a || $b || $c) $cnt1[$x]++;
                else $cnt2[$x]++;
            }
        }
        $ans = $n * $n;
        for ($i = 0; $i < 3; $i++) {
            for ($j = 0; $j < 3; $j++) {
                if ($i !== $j) $ans = min($ans, $n * $n - $cnt1[$i] - $cnt2[$j]);
            }
        }
        return $ans;
    }
}
