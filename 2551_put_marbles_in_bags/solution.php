<?php
// LeetCode 2551 - Put Marbles in Bags
// https://leetcode.com/problems/put-marbles-in-bags/

class Solution {
    function putMarbles($weights, $k) {
        $n = count($weights);
        if ($k === 1 || $k === $n) return 0;
        $pair = [];
        for ($i = 0; $i < $n - 1; $i++) $pair[] = $weights[$i] + $weights[$i + 1];
        sort($pair);
        $mn = 0;
        $mx = 0;
        for ($i = 0; $i < $k - 1; $i++) {
            $mn += $pair[$i];
            $mx += $pair[$n - 2 - $i];
        }
        return $mx - $mn;
    }
}
