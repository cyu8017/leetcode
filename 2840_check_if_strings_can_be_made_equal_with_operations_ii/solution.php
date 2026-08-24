<?php
// LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

class Solution {
    function checkStrings($s1, $s2) {
        $even1 = array_fill(0, 26, 0);
        $odd1 = array_fill(0, 26, 0);
        $even2 = array_fill(0, 26, 0);
        $odd2 = array_fill(0, 26, 0);
        $n = strlen($s1);
        for ($i = 0; $i < $n; $i++) {
            if ($i % 2 === 0) {
                $even1[ord($s1[$i]) - 97]++;
                $even2[ord($s2[$i]) - 97]++;
            } else {
                $odd1[ord($s1[$i]) - 97]++;
                $odd2[ord($s2[$i]) - 97]++;
            }
        }
        return $even1 === $even2 && $odd1 === $odd2;
    }
}
