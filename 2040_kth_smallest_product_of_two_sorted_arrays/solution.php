<?php
// LeetCode 2040 - Kth Smallest Product of Two Sorted Arrays
// https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer
     */
    function kthSmallestProduct($nums1, $nums2, $k) {
        $countLE = function ($x) use ($nums1, $nums2) {
            $cnt = 0;
            $m = count($nums2);
            foreach ($nums1 as $a) {
                if ($a > 0) {
                    $lo = 0;
                    $hi = $m;
                    while ($lo < $hi) {
                        $mid = ($lo + $hi) >> 1;
                        if ($a * $nums2[$mid] <= $x) $lo = $mid + 1;
                        else $hi = $mid;
                    }
                    $cnt += $lo;
                } else if ($a < 0) {
                    $lo = 0;
                    $hi = $m;
                    while ($lo < $hi) {
                        $mid = ($lo + $hi) >> 1;
                        if ($a * $nums2[$mid] <= $x) $hi = $mid;
                        else $lo = $mid + 1;
                    }
                    $cnt += $m - $lo;
                } else if ($x >= 0) $cnt += $m;
            }
            return $cnt;
        };
        $lo = -10000000000;
        $hi = 10000000000;
        while ($lo < $hi) {
            $mid = $lo + intdiv($hi - $lo, 2);
            if ($countLE($mid) >= $k) $hi = $mid;
            else $lo = $mid + 1;
        }
        return $lo;
    }
}
