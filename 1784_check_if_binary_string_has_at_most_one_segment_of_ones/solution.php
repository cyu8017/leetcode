<?php
// LeetCode 1784 - Check if Binary String Has at Most One Segment of Ones
// https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function checkOnesSegment($s) {
        $trimmed = trim($s, '0');
        return strpos($trimmed, '01') === false;
    }
}
