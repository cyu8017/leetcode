<?php
// LeetCode 0973 - K Closest Points to Origin
// https://leetcode.com/problems/k-closest-points-to-origin/

class Solution {
    function kClosest($points, $k) {
        usort($points, function ($a, $b) {
            return ($a[0] * $a[0] + $a[1] * $a[1]) <=> ($b[0] * $b[0] + $b[1] * $b[1]);
        });
        return array_slice($points, 0, $k);
    }
}
