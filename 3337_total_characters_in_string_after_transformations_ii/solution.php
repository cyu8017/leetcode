<?php
// LeetCode 3337 - Total Characters in String After Transformations II
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

class Solution {
    function matMul($a, $b, $mod) {
        $n = count($a);
        $c = [];
        for ($i = 0; $i < $n; $i++) $c[$i] = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            for ($k = 0; $k < $n; $k++) {
                if ($a[$i][$k] === 0) continue;
                for ($j = 0; $j < $n; $j++) {
                    $c[$i][$j] = ($c[$i][$j] + $a[$i][$k] * $b[$k][$j] % $mod) % $mod;
                }
            }
        }
        return $c;
    }

    function matPow($a, $e, $mod) {
        $n = count($a);
        $r = [];
        for ($i = 0; $i < $n; $i++) {
            $r[$i] = array_fill(0, $n, 0);
            $r[$i][$i] = 1;
        }
        while ($e > 0) {
            if ($e & 1) $r = $this->matMul($r, $a, $mod);
            $a = $this->matMul($a, $a, $mod);
            $e >>= 1;
        }
        return $r;
    }

    function lengthAfterTransformations($s, $t, $nums) {
        $mod = 1000000007;
        $mat = [];
        for ($i = 0; $i < 26; $i++) $mat[$i] = array_fill(0, 26, 0);
        for ($i = 0; $i < 26; $i++) {
            for ($j = 1; $j <= $nums[$i]; $j++) $mat[$i][($i + $j) % 26] = 1;
        }
        $mat = $this->matPow($mat, $t, $mod);
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $ans = 0;
        for ($i = 0; $i < 26; $i++) {
            for ($j = 0; $j < 26; $j++) {
                $ans = ($ans + $cnt[$i] * $mat[$i][$j] % $mod) % $mod;
            }
        }
        return $ans;
    }
}
