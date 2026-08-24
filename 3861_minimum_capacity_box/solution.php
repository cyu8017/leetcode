<?php
// LeetCode 3861 - Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/

class Solution {
    function minimumIndex($capacity, $itemSize) {
        $ans = -1;
        $n = count($capacity);
        for ($i = 0; $i < $n; $i++) {
            if ($capacity[$i] >= $itemSize && ($ans === -1 || $capacity[$i] < $capacity[$ans])) $ans = $i;
        }
        return $ans;
    }
}
