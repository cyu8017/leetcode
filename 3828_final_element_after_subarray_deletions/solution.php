<?php
// LeetCode 3828 - Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/

class Solution {
    function finalElement($nums) {
        return max($nums[0], $nums[count($nums) - 1]);
    }
}
