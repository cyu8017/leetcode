<?php
// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function removeDuplicates($s, $k) {
        $stack = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if (!empty($stack) && end($stack)[0] === $ch) {
                $stack[count($stack) - 1][1]++;
            } else {
                $stack[] = [$ch, 1];
            }
            if (end($stack)[1] === $k) array_pop($stack);
        }
        $ans = '';
        foreach ($stack as [$ch, $count]) $ans .= str_repeat($ch, $count);
        return $ans;
    }
}
