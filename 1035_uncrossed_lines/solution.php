<?php
// LeetCode 1035 - Uncrossed Lines
// https://leetcode.com/problems/uncrossed-lines/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function maxUncrossedLines($nums1, $nums2) {
        $m = count($nums1);
        $n = count($nums2);
        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($i = 1; $i <= $m; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                if ($nums1[$i - 1] === $nums2[$j - 1]) {
                    $dp[$i][$j] = $dp[$i - 1][$j - 1] + 1;
                } else {
                    $dp[$i][$j] = max($dp[$i - 1][$j], $dp[$i][$j - 1]);
                }
            }
        }
        return $dp[$m][$n];
    }
}
