<?php
// LeetCode 0927 - Three Equal Parts
// https://leetcode.com/problems/three-equal-parts/

class Solution {
    function threeEqualParts($arr) {
        $ones = [];
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) if ($arr[$i] !== 0) $ones[] = $i;
        $cnt = count($ones);
        if ($cnt % 3 !== 0) return [-1, -1];
        if ($cnt === 0) return [0, $n - 1];
        $third = intdiv($cnt, 3);
        $length = $ones[$cnt - 1] - $ones[2 * $third] + 1;
        $a = $ones[0];
        $b = $ones[$third];
        $c = $ones[2 * $third];
        if ($a + $length > $n || $b + $length > $n || $c + $length > $n) return [-1, -1];
        for ($i = 0; $i < $length; $i++) {
            if ($arr[$a + $i] !== $arr[$b + $i] || $arr[$a + $i] !== $arr[$c + $i]) return [-1, -1];
        }
        return [$a + $length - 1, $b + $length];
    }
}
