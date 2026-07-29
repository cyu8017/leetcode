<?php
// LeetCode 1061 - Lexicographically Smallest Equivalent String
// https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution {
    /**
     * @param String $s1
     * @param String $s2
     * @param String $baseStr
     * @return String
     */
    function smallestEquivalentString($s1, $s2, $baseStr) {
        $parent = range(0, 25);
        $find = function ($x) use (&$parent, &$find) {
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $union = function ($a, $b) use (&$parent, $find) {
            $ra = $find($a);
            $rb = $find($b);
            if ($ra === $rb) {
                return;
            }
            if ($ra < $rb) {
                $parent[$rb] = $ra;
            } else {
                $parent[$ra] = $rb;
            }
        };
        $n = strlen($s1);
        for ($i = 0; $i < $n; $i++) {
            $union(ord($s1[$i]) - 97, ord($s2[$i]) - 97);
        }
        $ans = "";
        $m = strlen($baseStr);
        for ($i = 0; $i < $m; $i++) {
            $ans .= chr($find(ord($baseStr[$i]) - 97) + 97);
        }
        return $ans;
    }
}
