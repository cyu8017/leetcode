<?php
// LeetCode 0925 - Long Pressed Name
// https://leetcode.com/problems/long-pressed-name/

class Solution {
    function isLongPressedName($name, $typed) {
        $i = 0;
        $j = 0;
        $n = strlen($name);
        $m = strlen($typed);
        while ($j < $m) {
            if ($i < $n && $name[$i] === $typed[$j]) { $i++; $j++; }
            elseif ($j > 0 && $typed[$j] === $typed[$j - 1]) $j++;
            else return false;
        }
        return $i === $n;
    }
}
