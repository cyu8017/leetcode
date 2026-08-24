<?php
// LeetCode 2570 - Merge Two 2D Arrays by Summing Values
// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

class Solution {
    function mergeArrays($nums1, $nums2) {
        $ans = [];
        $i = 0;
        $j = 0;
        $n1 = count($nums1);
        $n2 = count($nums2);
        while ($i < $n1 && $j < $n2) {
            if ($nums1[$i][0] === $nums2[$j][0]) {
                $ans[] = [$nums1[$i][0], $nums1[$i][1] + $nums2[$j][1]];
                $i++;
                $j++;
            } else if ($nums1[$i][0] < $nums2[$j][0]) {
                $ans[] = [$nums1[$i][0], $nums1[$i][1]];
                $i++;
            } else {
                $ans[] = [$nums2[$j][0], $nums2[$j][1]];
                $j++;
            }
        }
        while ($i < $n1) {
            $ans[] = [$nums1[$i][0], $nums1[$i][1]];
            $i++;
        }
        while ($j < $n2) {
            $ans[] = [$nums2[$j][0], $nums2[$j][1]];
            $j++;
        }
        return $ans;
    }
}
