<?php

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function maxSum($nums1, $nums2) {
        $i = $j = 0;
        $first = $second = 0;
        $n1 = count($nums1);
        $n2 = count($nums2);
        while ($i < $n1 || $j < $n2) {
            if ($j === $n2 || ($i < $n1 && $nums1[$i] < $nums2[$j])) {
                $first += $nums1[$i];
                $i++;
            } elseif ($i === $n1 || $nums2[$j] < $nums1[$i]) {
                $second += $nums2[$j];
                $j++;
            } else {
                $first = $second = max($first, $second) + $nums1[$i];
                $i++;
                $j++;
            }
        }
        return max($first, $second) % 1000000007;
    }
}
