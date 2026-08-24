<?php
// LeetCode 2976 - Minimum Cost to Convert String I
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/

class Solution {
    function minimumCost($source, $target, $original, $changed, $cost) {
        $inf = PHP_INT_MAX / 4;
        $dist = [];
        for ($i = 0; $i < 26; $i++) {
            $dist[$i] = array_fill(0, 26, $inf);
            $dist[$i][$i] = 0;
        }
        for ($i = 0; $i < count($original); $i++) {
            $u = ord($original[$i][0]) - 97;
            $v = ord($changed[$i][0]) - 97;
            $ww = $cost[$i];
            if ($ww < $dist[$u][$v]) $dist[$u][$v] = $ww;
        }
        for ($k = 0; $k < 26; $k++) {
            for ($i = 0; $i < 26; $i++) {
                for ($j = 0; $j < 26; $j++) {
                    if ($dist[$i][$k] + $dist[$k][$j] < $dist[$i][$j]) {
                        $dist[$i][$j] = $dist[$i][$k] + $dist[$k][$j];
                    }
                }
            }
        }
        $ans = 0;
        $len = strlen($source);
        for ($i = 0; $i < $len; $i++) {
            $a = ord($source[$i]) - 97;
            $b = ord($target[$i]) - 97;
            if ($dist[$a][$b] >= $inf / 2) return -1;
            $ans += $dist[$a][$b];
        }
        return $ans;
    }
}
