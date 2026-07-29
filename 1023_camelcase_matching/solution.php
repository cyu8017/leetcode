<?php
// LeetCode 1023 - Camelcase Matching
// https://leetcode.com/problems/camelcase-matching/

class Solution {
    /**
     * @param String[] $queries
     * @param String $pattern
     * @return Boolean[]
     */
    function camelMatch($queries, $pattern) {
        $ans = [];
        $pLen = strlen($pattern);
        foreach ($queries as $q) {
            $i = 0;
            $ok = true;
            $qLen = strlen($q);
            for ($j = 0; $j < $qLen; $j++) {
                $ch = $q[$j];
                if ($i < $pLen && $ch === $pattern[$i]) {
                    $i++;
                } elseif (ctype_upper($ch)) {
                    $ok = false;
                    break;
                }
            }
            $ans[] = $ok && $i === $pLen;
        }
        return $ans;
    }
}
