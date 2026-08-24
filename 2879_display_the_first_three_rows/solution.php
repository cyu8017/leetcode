<?php
// LeetCode 2879 - Display the First Three Rows
// https://leetcode.com/problems/display-the-first-three-rows/

class Solution {
    function selectFirstRows($employees) {
        return array_slice($employees, 0, 3);
    }
}
