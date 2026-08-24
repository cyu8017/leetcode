<?php
// LeetCode 3449 - Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-game-score/

class Solution {
    function maxScore($points, $m) {
        $ok = function($mid) use ($points, $m) {
            $need = 0;
            $extra = 0;
            foreach ($points as $p) {
                $req = intdiv($mid + $p - 1, $p);
                if ($req > $extra) {
                    $visits = $req - $extra;
                    $need += 2 * $visits - 1;
                    $extra = $visits - 1;
                } else {
                    $need += 1;
                    $extra = 0;
                }
                if ($need > $m) return false;
            }
            return $need <= $m;
        };
        $lo = 0;
        $hi = 10 ** 18;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($ok($mid)) $lo = $mid;
            else $hi = $mid - 1;
        }
        return $lo;
    }
}
