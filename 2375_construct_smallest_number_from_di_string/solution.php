<?php
// LeetCode 2375 - Construct Smallest Number From DI String
// https://leetcode.com/problems/construct-smallest-number-from-di-string/

class Solution {
    function smallestNumber($pattern) {
        $n = strlen($pattern);
        $ans = [];
        for ($i = 0; $i <= $n; $i++) $ans[$i] = chr(49 + $i);
        $i = 0;
        while ($i < $n) {
            if ($pattern[$i] === 'I') { $i++; continue; }
            $j = $i;
            while ($j < $n && $pattern[$j] === 'D') $j++;
            $l = $i;
            $r = $j;
            while ($l < $r) {
                $t = $ans[$l]; $ans[$l] = $ans[$r]; $ans[$r] = $t;
                $l++; $r--;
            }
            $i = $j;
        }
        return implode('', $ans);
    }
}
