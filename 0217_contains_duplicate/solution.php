<?php
// LeetCode 0217 - Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/

class Solution {
    function containsDuplicate($nums) {
        return count(array_unique($nums)) !== count($nums);
    }
}
