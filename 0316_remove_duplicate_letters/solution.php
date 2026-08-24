<?php
// LeetCode 0316 - Remove Duplicate Letters
// https://leetcode.com/problems/remove-duplicate-letters/

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function removeDuplicateLetters($s) {
        $lastIndex = [];
        $length = strlen($s);
        for ($index = 0; $index < $length; $index++) {
            $lastIndex[$s[$index]] = $index;
        }

        $stack = [];
        $seen = [];
        for ($index = 0; $index < $length; $index++) {
            $char = $s[$index];
            if (isset($seen[$char])) {
                continue;
            }
            while (!empty($stack) &&
                   $stack[count($stack) - 1] > $char &&
                   $lastIndex[$stack[count($stack) - 1]] > $index) {
                $removed = array_pop($stack);
                unset($seen[$removed]);
            }
            $stack[] = $char;
            $seen[$char] = true;
        }
        return implode('', $stack);
    }
}
