<?php
// LeetCode 1711 - Count Good Meals
// https://leetcode.com/problems/count-good-meals/

class Solution {
    /**
     * @param Integer[] $deliciousness
     * @return Integer
     */
    function countPairs($deliciousness) {
        $mod = 1000000007;
        $seen = [];
        $ans = 0;
        foreach ($deliciousness as $value) {
            for ($power = 0; $power < 22; $power++) {
                $target = (1 << $power) - $value;
                if (isset($seen[$target])) {
                    $ans += $seen[$target];
                }
            }
            $seen[$value] = ($seen[$value] ?? 0) + 1;
        }
        return $ans % $mod;
    }
}
