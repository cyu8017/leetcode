<?php
// LeetCode 2961 - Double Modular Exponentiation
// https://leetcode.com/problems/double-modular-exponentiation/

class Solution {
    private function modPow($a, $b, $mod) {
        $res = 1 % $mod;
        $a %= $mod;
        while ($b > 0) {
            if (($b & 1) !== 0) $res = $res * $a % $mod;
            $a = $a * $a % $mod;
            $b >>= 1;
        }
        return $res;
    }

    function getGoodIndices($variables, $target) {
        $ans = [];
        for ($i = 0; $i < count($variables); $i++) {
            $v = $variables[$i];
            $a = $v[0];
            $b = $v[1];
            $c = $v[2];
            $m = $v[3];
            if ($this->modPow($this->modPow($a, $b, 10), $c, $m) === $target) $ans[] = $i;
        }
        return $ans;
    }
}
