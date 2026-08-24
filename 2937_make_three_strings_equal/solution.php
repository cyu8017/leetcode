<?php
// LeetCode 2937 - Make Three Strings Equal
// https://leetcode.com/problems/make-three-strings-equal/

class Solution {
    function findMinimumOperations($s1, $s2, $s3) {
        $n = min(strlen($s1), strlen($s2), strlen($s3));
        $i = 0;
        while ($i < $n && $s1[$i] === $s2[$i] && $s2[$i] === $s3[$i]) $i++;
        if ($i === 0) return -1;
        return strlen($s1) + strlen($s2) + strlen($s3) - 3 * $i;
    }
}
