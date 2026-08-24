<?php
// LeetCode 3269 - Constructing Two Increasing Arrays
// https://leetcode.com/problems/constructing-two-increasing-arrays/

class Solution {
    function minLargest($nums1, $nums2) {
        $n = count($nums1);
        $m = count($nums2);
        $inf = 1000000000;
        $dp = [];
        for ($i = 0; $i <= $n; $i++) $dp[$i] = array_fill(0, $m + 1, $inf);
        $dp[0][0] = 0;
        for ($i = 0; $i <= $n; $i++) {
            for ($j = 0; $j <= $m; $j++) {
                if ($dp[$i][$j] === $inf) continue;
                $prev = $dp[$i][$j];
                if ($i < $n) {
                    $need = $prev + 1;
                    if ($nums1[$i] === 0) { if ($need % 2 !== 0) $need++; }
                    else { if ($need % 2 === 0) $need++; }
                    if ($need < $dp[$i + 1][$j]) $dp[$i + 1][$j] = $need;
                }
                if ($j < $m) {
                    $need = $prev + 1;
                    if ($nums2[$j] === 0) { if ($need % 2 !== 0) $need++; }
                    else { if ($need % 2 === 0) $need++; }
                    if ($need < $dp[$i][$j + 1]) $dp[$i][$j + 1] = $need;
                }
            }
        }
        return $dp[$n][$m];
    }
}
