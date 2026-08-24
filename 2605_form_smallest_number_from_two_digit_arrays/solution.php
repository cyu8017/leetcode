<?php
// LeetCode 2605 - Form Smallest Number From Two Digit Arrays
// https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

class Solution {
    function minNumber($nums1, $nums2) {
        $s1 = [];
        $s2 = [];
        foreach ($nums1 as $x) $s1[$x] = true;
        foreach ($nums2 as $x) $s2[$x] = true;
        $common = 10;
        foreach ($s1 as $x => $_) if (isset($s2[$x]) && $x < $common) $common = $x;
        if ($common < 10) return $common;
        $a = 10;
        $b = 10;
        foreach ($nums1 as $x) if ($x < $a) $a = $x;
        foreach ($nums2 as $x) if ($x < $b) $b = $x;
        return min($a * 10 + $b, $b * 10 + $a);
    }
}
