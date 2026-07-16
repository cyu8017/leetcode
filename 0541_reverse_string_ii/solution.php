<?php
// LeetCode 0541 - Reverse String II
// https://leetcode.com/problems/reverse-string-ii/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function reverseStr($s, $k) {
        return $this->reverse_str($s, $k);
    }

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function reverse_str($s, $k) {
        $chars = str_split($s);
        $length = count($chars);
        for ($start = 0; $start < $length; $start += 2 * $k) {
            $left = $start;
            $right = min($start + $k, $length) - 1;
            while ($left < $right) {
                $temp = $chars[$left];
                $chars[$left] = $chars[$right];
                $chars[$right] = $temp;
                $left++;
                $right--;
            }
        }
        return implode('', $chars);
    }
}
