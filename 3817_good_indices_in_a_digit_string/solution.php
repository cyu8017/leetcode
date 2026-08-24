<?php
// LeetCode 3817 - Good Indices in a Digit String
// https://leetcode.com/problems/good-indices-in-a-digit-string/

class Solution {
    function goodIndices($s) {
        $ans = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $t = strval($i);
            $k = strlen($t);
            if ($i + 1 - $k >= 0 && substr($s, $i + 1 - $k, $k) === $t) $ans[] = $i;
        }
        return $ans;
    }
}
