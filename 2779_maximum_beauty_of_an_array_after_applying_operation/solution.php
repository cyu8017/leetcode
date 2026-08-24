<?php
// LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
// https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

class Solution {
    function maximumBeauty($nums, $k) {
        sort($nums);
        $ans = 0;
        $left = 0;
        for ($right = 0; $right < count($nums); $right++) {
            while ($nums[$right] - $nums[$left] > 2 * $k) $left++;
            $ans = max($ans, $right - $left + 1);
        }
        return $ans;
    }
}
