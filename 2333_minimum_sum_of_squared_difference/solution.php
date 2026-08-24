<?php
// LeetCode 2333 - Minimum Sum of Squared Difference
// https://leetcode.com/problems/minimum-sum-of-squared-difference/

class Solution {
    function minSumSquareDiff($nums1, $nums2, $k1, $k2) {
        $n = count($nums1);
        $diff = [];
        $maxD = 0;
        for ($i = 0; $i < $n; $i++) {
            $d = abs($nums1[$i] - $nums2[$i]);
            $diff[$i] = $d;
            if ($d > $maxD) $maxD = $d;
        }
        $k = $k1 + $k2;
        $freq = array_fill(0, $maxD + 1, 0);
        foreach ($diff as $d) $freq[$d]++;
        for ($d = $maxD; $d > 0 && $k > 0; $d--) {
            if ($freq[$d] === 0) continue;
            $take = $freq[$d];
            if ($take > $k) $take = $k;
            $freq[$d] -= $take;
            $freq[$d - 1] += $take;
            $k -= $take;
        }
        $ans = 0;
        for ($d = 0; $d <= $maxD; $d++) $ans += $d * $d * $freq[$d];
        return $ans;
    }
}
