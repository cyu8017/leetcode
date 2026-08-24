<?php
// LeetCode 0784 - Letter Case Permutation
// https://leetcode.com/problems/letter-case-permutation/

class Solution {
    /**
     * @param String $s
     * @return String[]
     */
    function letterCasePermutation($s) {
        $result = [""];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            $next = [];
            if (ctype_alpha($ch)) {
                $lower = strtolower($ch);
                $upper = strtoupper($ch);
                foreach ($result as $prefix) {
                    $next[] = $prefix . $lower;
                    $next[] = $prefix . $upper;
                }
            } else {
                foreach ($result as $prefix) $next[] = $prefix . $ch;
            }
            $result = $next;
        }
        return $result;
    }
}
