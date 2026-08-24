<?php
// LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
// https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

class Solution {
    function minimumOperationsToMakeEqual($x, $y) {
        if ($x <= $y) return $y - $x;
        $q = [[$x, 0]];
        $seen = [$x => true];
        $qi = 0;
        while ($qi < count($q)) {
            [$v, $d] = $q[$qi++];
            if ($v === $y) return $d;
            $cands = [$v + 1, $v - 1, $v % 11 === 0 ? intdiv($v, 11) : -1, $v % 5 === 0 ? intdiv($v, 5) : -1];
            foreach ($cands as $nxt) {
                if ($nxt > 0 && $nxt < 2 * $x + 20 && !isset($seen[$nxt])) {
                    $seen[$nxt] = true;
                    $q[] = [$nxt, $d + 1];
                }
            }
        }
        return -1;
    }
}
