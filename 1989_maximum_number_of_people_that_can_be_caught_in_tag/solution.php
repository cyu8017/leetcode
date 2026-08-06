<?php
// LeetCode 1989 - Maximum Number of People That Can Be Caught in Tag
// https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/

class Solution {
    /**
     * @param Integer[] $team
     * @param Integer $dist
     * @return Integer
     */
    function catchMaximumAmountofPeople($team, $dist) {
        $ans = 0;
        $j = 0;
        $n = count($team);
        for ($i = 0; $i < $n; $i++) {
            if ($team[$i]) {
                while ($j < $n && ($team[$j] || $i - $j > $dist)) {
                    $j++;
                }
                if ($j < $n && abs($i - $j) <= $dist) {
                    $ans++;
                    $j++;
                }
            }
        }
        return $ans;
    }
}
