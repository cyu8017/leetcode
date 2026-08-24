<?php
// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

class Solution {
    function lexSmallest($s) {
        $n = strlen($s);
        $best = $s;
        $reverse = function(&$a, $l, $r) {
            for ($i = $l, $j = $r - 1; $i < $j; $i++, $j--) {
                $t = $a[$i]; $a[$i] = $a[$j]; $a[$j] = $t;
            }
        };
        for ($i = 1; $i <= $n; $i++) {
            $t = str_split($s);
            $reverse($t, 0, $i);
            $ts = implode('', $t);
            if ($ts < $best) $best = $ts;
        }
        for ($i = 0; $i < $n; $i++) {
            $t = str_split($s);
            $reverse($t, $i, $n);
            $ts = implode('', $t);
            if ($ts < $best) $best = $ts;
        }
        return $best;
    }
}
