<?php
// LeetCode 2734 - Lexicographically Smallest String After Substring Operation
// https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

class Solution {
    function smallestString($s) {
        $arr = str_split($s);
        $n = count($arr);
        $i = 0;
        while ($i < $n && $arr[$i] === 'a') $i++;
        if ($i === $n) {
            $arr[$n - 1] = 'z';
            return implode('', $arr);
        }
        while ($i < $n && $arr[$i] !== 'a') {
            $arr[$i] = chr(ord($arr[$i]) - 1);
            $i++;
        }
        return implode('', $arr);
    }
}
