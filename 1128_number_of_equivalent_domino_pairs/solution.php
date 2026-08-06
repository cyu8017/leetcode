<?php
// LeetCode 1128 - Number of Equivalent Domino Pairs
// https://leetcode.com/problems/number-of-equivalent-domino-pairs/

class Solution {
    /**
     * @param Integer[][] $dominoes
     * @return Integer
     */
    function numEquivDominoPairs($dominoes) {
        $cnt = [];
        $ans = 0;
        foreach ($dominoes as [$a, $b]) {
            $key = min($a, $b) * 10 + max($a, $b);
            $ans += $cnt[$key] ?? 0;
            $cnt[$key] = ($cnt[$key] ?? 0) + 1;
        }
        return $ans;
    }
}
