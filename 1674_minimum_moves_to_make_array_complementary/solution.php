<?php
// LeetCode 1674 - Minimum Moves to Make Array Complementary
// https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

class Solution {
    function minMoves($nums, $limit) {
        $n = count($nums);
        $d = array_fill(0, 2 * $limit + 2, 0);
        for ($i = 0; $i < intdiv($n, 2); $i++) {
            $a = $nums[$i];
            $b = $nums[$n - 1 - $i];
            $lo = min($a, $b) + 1;
            $hi = max($a, $b) + $limit;
            $s = $a + $b;
            $d[2] += 2;
            $d[$lo] -= 1;
            $d[$s] -= 1;
            $d[$s + 1] += 1;
            $d[$hi + 1] += 1;
        }
        $ans = PHP_INT_MAX;
        $cur = 0;
        for ($s = 2; $s <= 2 * $limit; $s++) {
            $cur += $d[$s];
            $ans = min($ans, $cur);
        }
        return $ans;
    }
}
