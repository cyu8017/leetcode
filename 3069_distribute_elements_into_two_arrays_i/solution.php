<?php
// LeetCode 3069 - Distribute Elements Into Two Arrays I
// https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

class Solution {
    function resultArray($nums) {
        $arr1 = [$nums[0]];
        $arr2 = [$nums[1]];
        $n = count($nums);
        for ($i = 2; $i < $n; $i++) {
            if ($arr1[count($arr1) - 1] > $arr2[count($arr2) - 1]) $arr1[] = $nums[$i];
            else $arr2[] = $nums[$i];
        }
        return array_merge($arr1, $arr2);
    }
}
