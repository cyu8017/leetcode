<?php
// LeetCode 1153 - String Transforms Into Another String
// https://leetcode.com/problems/string-transforms-into-another-string/

class Solution {
    /**
     * @param String $str1
     * @param String $str2
     * @return Boolean
     */
    function canConvert($str1, $str2) {
        if ($str1 === $str2) return true;
        $mapping = [];
        $n = strlen($str1);
        for ($i = 0; $i < $n; $i++) {
            $a = $str1[$i];
            $b = $str2[$i];
            if (isset($mapping[$a]) && $mapping[$a] !== $b) return false;
            $mapping[$a] = $b;
        }
        return count(array_unique(str_split($str2))) < 26;
    }
}
