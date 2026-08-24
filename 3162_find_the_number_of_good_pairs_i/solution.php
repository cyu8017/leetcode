<?php
// LeetCode 3162 - Find the Number of Good Pairs I
// https://leetcode.com/problems/find-the-number-of-good-pairs-i/

class Solution {
    function numberOfPairs($nums1, $nums2, $k) {
        $ans = 0;
        foreach ($nums1 as $x)
            foreach ($nums2 as $y)
                if ($x % ($y * $k) === 0) $ans++;
        return $ans;
    }
}
