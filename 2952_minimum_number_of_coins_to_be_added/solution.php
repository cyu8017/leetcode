<?php
// LeetCode 2952 - Minimum Number of Coins to be Added
// https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

class Solution {
    function minimumAddedCoins($coins, $target) {
        sort($coins);
        $ans = 0;
        $reach = 0;
        $i = 0;
        $n = count($coins);
        while ($reach < $target) {
            if ($i < $n && $coins[$i] <= $reach + 1) {
                $reach += $coins[$i];
                $i++;
            } else {
                $reach += $reach + 1;
                $ans++;
            }
        }
        return $ans;
    }
}
