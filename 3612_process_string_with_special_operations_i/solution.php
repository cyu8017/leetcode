<?php
// LeetCode 3612 - Process String with Special Operations I
// https://leetcode.com/problems/process-string-with-special-operations-i/

class Solution {
    function processStr($s) {
        $result = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if (($c >= 'a' && $c <= 'z') || ($c >= 'A' && $c <= 'Z')) $result[] = $c;
            else if ($c === '*') {
                if (count($result) > 0) array_pop($result);
            } else if ($c === '#') $result = array_merge($result, $result);
            else if ($c === '%') $result = array_reverse($result);
        }
        return implode('', $result);
    }
}
