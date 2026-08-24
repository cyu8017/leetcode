<?php
// LeetCode 2320 - Count Number of Ways to Place Houses
// https://leetcode.com/problems/count-number-of-ways-to-place-houses/

class Solution {
    function countHousePlacements($n) {
        $mod = 1000000007;
        $a = 1;
        $b = 1;
        for ($i = 1; $i <= $n; ++$i) {
            $na = ($a + $b) % $mod;
            $b = $a;
            $a = $na;
        }
        $ways = ($a + $b) % $mod;
        return ($ways * $ways) % $mod;
    }
}
