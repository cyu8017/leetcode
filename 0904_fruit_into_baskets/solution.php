<?php
// LeetCode 0904 - Fruit Into Baskets
// https://leetcode.com/problems/fruit-into-baskets/

class Solution {
    function totalFruit($fruits) {
        $count = [];
        $left = 0;
        $ans = 0;
        $n = count($fruits);
        for ($right = 0; $right < $n; $right++) {
            $count[$fruits[$right]] = ($count[$fruits[$right]] ?? 0) + 1;
            while (count($count) > 2) {
                $c = $count[$fruits[$left]] - 1;
                if ($c === 0) unset($count[$fruits[$left]]);
                else $count[$fruits[$left]] = $c;
                $left++;
            }
            $ans = max($ans, $right - $left + 1);
        }
        return $ans;
    }
}
