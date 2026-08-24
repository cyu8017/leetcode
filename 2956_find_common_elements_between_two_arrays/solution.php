<?php
// LeetCode 2956 - Find Common Elements Between Two Arrays
// https://leetcode.com/problems/find-common-elements-between-two-arrays/

class Solution {
    function findIntersectionValues($nums1, $nums2) {
        $s1 = array_flip($nums1);
        $s2 = array_flip($nums2);
        $a = 0;
        $b = 0;
        foreach ($nums1 as $v) if (isset($s2[$v])) $a++;
        foreach ($nums2 as $v) if (isset($s1[$v])) $b++;
        return [$a, $b];
    }
}
