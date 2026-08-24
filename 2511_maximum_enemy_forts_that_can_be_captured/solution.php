<?php
// LeetCode 2511 - Maximum Enemy Forts That Can Be Captured
// https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

class Solution {
    function captureForts($forts) {
        $ans = 0;
        $prev = -1;
        $n = count($forts);
        for ($i = 0; $i < $n; $i++) {
            if ($forts[$i] !== 0) {
                if ($prev >= 0 && $forts[$prev] === -$forts[$i]) {
                    if ($i - $prev - 1 > $ans) $ans = $i - $prev - 1;
                }
                $prev = $i;
            }
        }
        return $ans;
    }
}
