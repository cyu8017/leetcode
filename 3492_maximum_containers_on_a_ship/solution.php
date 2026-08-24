<?php
// LeetCode 3492 - Maximum Containers on a Ship
// https://leetcode.com/problems/maximum-containers-on-a-ship/

class Solution {
    function maxContainers($n, $w, $maxWeight) {
        $cap = $n * $n;
        $byW = intdiv($maxWeight, $w);
        return $cap < $byW ? $cap : $byW;
    }
}
