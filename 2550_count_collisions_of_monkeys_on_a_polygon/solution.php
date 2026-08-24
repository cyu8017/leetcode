<?php
// LeetCode 2550 - Count Collisions of Monkeys on a Polygon
// https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution {
    function monkeyMove($n) {
        $MOD = 1000000007;
        $powMod = function($a, $e) use ($MOD) {
            $res = 1;
            while ($e > 0) {
                if ($e & 1) $res = $res * $a % $MOD;
                $a = $a * $a % $MOD;
                $e >>= 1;
            }
            return $res;
        };
        return ($powMod(2, $n) - 2 + $MOD) % $MOD;
    }
}
