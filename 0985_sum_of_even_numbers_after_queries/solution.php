<?php
// LeetCode 0985 - Sum of Even Numbers After Queries
// https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function sumEvenAfterQueries($nums, $queries) {
        $even = 0;
        foreach ($nums as $x) if ($x % 2 === 0) $even += $x;
        $ans = [];
        foreach ($queries as $qi => $q) {
            $val = $q[0];
            $i = $q[1];
            if ($nums[$i] % 2 === 0) $even -= $nums[$i];
            $nums[$i] += $val;
            if ($nums[$i] % 2 === 0) $even += $nums[$i];
            $ans[$qi] = $even;
        }
        return $ans;
    }
}
