<?php
// LeetCode 3002 - Maximum Size of a Set After Removals
// https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

class Solution {
    function maximumSetSize($nums1, $nums2) {
        $s1 = [];
        $s2 = [];
        foreach ($nums1 as $x) $s1[$x] = true;
        foreach ($nums2 as $x) $s2[$x] = true;
        $a = 0;
        $b = 0;
        $c = 0;
        foreach ($s1 as $x => $_) if (!isset($s2[$x])) $a++;
        foreach ($s2 as $x => $_) {
            if (!isset($s1[$x])) $b++;
            else $c++;
        }
        $n = count($nums1);
        $a = min($a, intdiv($n, 2));
        $b = min($b, intdiv($n, 2));
        return min($a + $b + $c, $n);
    }
}
