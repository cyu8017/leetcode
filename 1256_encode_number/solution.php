<?php
// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

class Solution {
    /**
     * @param Integer $num
     * @return String
     */
    function encode($num) {
        return substr(decbin($num + 1), 1);
    }
}
