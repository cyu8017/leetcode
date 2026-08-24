<?php
// LeetCode 0970 - Powerful Integers
// https://leetcode.com/problems/powerful-integers/

class Solution {
    function powerfulIntegers($x, $y, $bound) {
        $ans = [];
        for ($a = 1; $a < $bound; $a *= $x) {
            for ($b = 1; $a + $b <= $bound; $b *= $y) {
                $ans[$a + $b] = true;
                if ($y === 1) break;
            }
            if ($x === 1) break;
        }
        $keys = array_map('intval', array_keys($ans));
        sort($keys);
        return $keys;
    }
}
