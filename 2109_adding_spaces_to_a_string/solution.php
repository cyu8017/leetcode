<?php
// LeetCode 2109 - Adding Spaces to a String
// https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution {
    /**
     * @param String $s
     * @param Integer[] $spaces
     * @return String
     */
    function addSpaces($s, $spaces) {
        $b = [];
        $j = 0;
        $n = strlen($s);
        $m = count($spaces);
        for ($i = 0; $i < $n; $i++) {
            if ($j < $m && $spaces[$j] === $i) {
                $b[] = ' ';
                $j++;
            }
            $b[] = $s[$i];
        }
        return implode('', $b);
    }
}
