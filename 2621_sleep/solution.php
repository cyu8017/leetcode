<?php
// LeetCode 2621 - Sleep
// https://leetcode.com/problems/sleep/

class Solution {
    function sleep($millis) {
        usleep((int)($millis * 1000));
        return null;
    }
}
