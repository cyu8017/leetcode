<?php
class Solution {
    function maxDotProduct($nums1, $nums2) {
        $n = count($nums2);
        $dp = array_fill(0, $n + 1, PHP_INT_MIN);
        foreach ($nums1 as $a) {
            $prev = $dp;
            for ($j = 1; $j <= $n; $j++) {
                $b = $nums2[$j - 1];
                $product = $a * $b;
                $dp[$j] = max($dp[$j - 1], $prev[$j], $product, $product + max(0, $prev[$j - 1]));
            }
        }
        return $dp[$n];
    }
}
