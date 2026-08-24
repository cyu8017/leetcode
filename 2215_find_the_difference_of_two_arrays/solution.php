<?php
// LeetCode 2215 - Find the Difference of Two Arrays
// https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution {
    function findDifference($nums1, $nums2) {
        $s1 = [];
        $s2 = [];
        foreach ($nums1 as $x) $s1[$x] = true;
        foreach ($nums2 as $x) $s2[$x] = true;
        $a = [];
        $b = [];
        foreach ($s1 as $x => $_) if (!isset($s2[$x])) $a[] = $x;
        foreach ($s2 as $x => $_) if (!isset($s1[$x])) $b[] = $x;
        return [$a, $b];
    }
}
