<?php
// LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

class Solution {
    function minimumTotalCost($nums1, $nums2) {
        $n = count($nums1);
        $freq = [];
        $ans = 0;
        $same = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($nums1[$i] === $nums2[$i]) {
                $same++;
                if (!isset($freq[$nums1[$i]])) $freq[$nums1[$i]] = 0;
                $freq[$nums1[$i]]++;
                $ans += $i;
            }
        }
        $maxFreq = 0;
        $maxVal = 0;
        foreach ($freq as $key => $value) {
            if ($value > $maxFreq) {
                $maxFreq = $value;
                $maxVal = $key;
            }
        }
        $need = $maxFreq * 2 - $same;
        if ($need <= 0) return $ans;
        for ($i = 0; $i < $n && $need > 0; $i++) {
            if ($nums1[$i] !== $nums2[$i] && $nums1[$i] !== $maxVal && $nums2[$i] !== $maxVal) {
                $ans += $i;
                $need--;
            }
        }
        return $need > 0 ? -1 : $ans;
    }
}
