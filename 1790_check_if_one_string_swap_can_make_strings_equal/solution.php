<?php
// LeetCode 1790 - Check if One String Swap Can Make Strings Equal
// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution {
    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function areAlmostEqual($s1, $s2) {
        $diff = [];
        $n = strlen($s1);
        for ($i = 0; $i < $n; $i++) {
            if ($s1[$i] !== $s2[$i]) {
                $diff[] = $i;
            }
        }
        if (count($diff) === 0) return true;
        return count($diff) === 2
            && $s1[$diff[0]] === $s2[$diff[1]]
            && $s1[$diff[1]] === $s2[$diff[0]];
    }
}
