<?php
// LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
// https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

class Solution {
    function getSmallestString($s, $k) {
        $arr = str_split($s);
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) {
            $c1 = ord($arr[$i]);
            for ($c2 = 97; $c2 < $c1; $c2++) {
                $d = min($c1 - $c2, 26 - ($c1 - $c2));
                if ($d <= $k) {
                    $arr[$i] = chr($c2);
                    $k -= $d;
                    break;
                }
            }
        }
        return implode("", $arr);
    }
}
