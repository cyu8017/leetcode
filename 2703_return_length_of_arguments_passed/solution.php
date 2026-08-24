<?php
// LeetCode 2703 - Return Length of Arguments Passed
// https://leetcode.com/problems/return-length-of-arguments-passed/

class Solution {
    function argumentsLength(...$args) {
        return count($args);
    }
}
