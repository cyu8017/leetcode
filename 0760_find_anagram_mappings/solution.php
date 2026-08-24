<?php
// LeetCode 0760 - Find Anagram Mappings
// https://leetcode.com/problems/find-anagram-mappings/

class Solution {
    function anagramMappings($nums1, $nums2) {
        $positions = [];
        $n2 = count($nums2);
        for ($i = 0; $i < $n2; $i++) {
            if (!isset($positions[$nums2[$i]])) $positions[$nums2[$i]] = [];
            $positions[$nums2[$i]][] = $i;
        }
        $n1 = count($nums1);
        $result = array_fill(0, $n1, 0);
        for ($i = 0; $i < $n1; $i++) {
            $result[$i] = array_shift($positions[$nums1[$i]]);
        }
        return $result;
    }
}
