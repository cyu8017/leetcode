<?php
// LeetCode 3281 - Maximize Score of Numbers in Ranges
// https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution {
    function maxPossibleScore($start, $d) {
        sort($start);
        $n = count($start);
        $ok = function($mid) use ($start, $d) {
            $prev = $start[0];
            for ($i = 1; $i < count($start); $i++) {
                $need = $prev + $mid;
                $cur = $start[$i];
                if ($need > $cur + $d) return false;
                $prev = $need > $cur ? $need : $cur;
            }
            return true;
        };
        $lo = 0;
        $hi = $start[$n - 1] + $d - $start[0] + 1;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($ok($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
