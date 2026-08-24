<?php
// LeetCode 2710 - Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

class Solution {
    function removeTrailingZeros($num) {
        $end = strlen($num);
        while ($end > 0 && $num[$end - 1] === "0") $end--;
        return substr($num, 0, $end);
    }
}
