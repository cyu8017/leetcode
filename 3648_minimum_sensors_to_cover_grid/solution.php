<?php
// LeetCode 3648 - Minimum Sensors to Cover Grid
// https://leetcode.com/problems/minimum-sensors-to-cover-grid/

class Solution {
    function minSensors($n, $m, $k) {
        $cover = 2 * $k + 1;
        return (int)ceil($n / $cover) * (int)ceil($m / $cover);
    }
}
