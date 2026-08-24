<?php
// LeetCode 0982 - Triples with Bitwise AND Equal To Zero
// https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countTriplets($nums) {
        $cnt = [];
        foreach ($nums as $a) {
            foreach ($nums as $b) {
                $k = $a & $b;
                $cnt[$k] = ($cnt[$k] ?? 0) + 1;
            }
        }
        $ans = 0;
        foreach ($nums as $c) {
            foreach ($cnt as $k => $v) {
                if (($k & $c) === 0) $ans += $v;
            }
        }
        return $ans;
    }
}
