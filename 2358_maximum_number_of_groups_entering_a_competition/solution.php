<?php
// LeetCode 2358 - Maximum Number of Groups Entering a Competition
// https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

class Solution {
    function maximumGroups($grades) {
        $n = count($grades);
        $k = 0;
        while (intdiv(($k + 1) * ($k + 2), 2) <= $n) $k++;
        return $k;
    }
}
