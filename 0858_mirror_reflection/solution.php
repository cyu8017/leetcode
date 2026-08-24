<?php
// LeetCode 0858 - Mirror Reflection
// https://leetcode.com/problems/mirror-reflection/

class Solution {
    /**
     * @param Integer $p
     * @param Integer $q
     * @return Integer
     */
    function mirrorReflection($p, $q) {
        $gcd = function($a, $b) {
            while ($b !== 0) {
                $t = $a % $b;
                $a = $b;
                $b = $t;
            }
            return $a;
        };
        $g = $gcd($p, $q);
        $p = intdiv($p, $g);
        $q = intdiv($q, $g);
        if ($p % 2 === 0) return 2;
        if ($q % 2 === 0) return 0;
        return 1;
    }
}
