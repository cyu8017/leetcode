<?php
// LeetCode 3398 - Smallest Substring With Identical Characters I
// https://leetcode.com/problems/smallest-substring-with-identical-characters-i/

class Solution {
    function minLength($s, $numOps) {
        $n = strlen($s);
        $ok = function($L) use ($n, $s, $numOps) {
            if ($L === 0) return false;
            $ops = 0;
            for ($i = 0; $i < $n; ) {
                $j = $i;
                while ($j < $n && $s[$j] === $s[$i]) $j++;
                $ops += intdiv($j - $i, $L + 1);
                $i = $j;
            }
            return $ops <= $numOps;
        };
        $lo = 1;
        $hi = $n;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($ok($mid)) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
