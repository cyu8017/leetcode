<?php
// LeetCode 3131 - Find the Integer Added to Array I
// https://leetcode.com/problems/find-the-integer-added-to-array-i/

class Solution {
    function addedInteger($nums1, $nums2) {
        return min($nums2) - min($nums1);
    }
}
