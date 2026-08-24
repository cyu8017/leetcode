<?php
// LeetCode 0267 - Palindrome Permutation II
// https://leetcode.com/problems/palindrome-permutation-ii/

class Solution {
    /**
     * @param String $s
     * @return String[]
     */
    function generatePalindromes($s) {
        $counts = [];
        $length = strlen($s);
        for ($i = 0; $i < $length; $i++) {
            $char = $s[$i];
            if (!isset($counts[$char])) {
                $counts[$char] = 0;
            }
            $counts[$char]++;
        }

        $middle = '';
        $oddChars = [];
        foreach ($counts as $char => $count) {
            if ($count % 2 !== 0) {
                $oddChars[] = $char;
            }
        }
        if (count($oddChars) > 1) {
            return [];
        }
        if (count($oddChars) === 1) {
            $middle = $oddChars[0];
        }

        $keys = array_keys($counts);
        sort($keys);
        $half = [];
        foreach ($keys as $char) {
            for ($i = 0; $i < intdiv($counts[$char], 2); $i++) {
                $half[] = $char;
            }
        }

        $result = [];
        $used = array_fill(0, count($half), false);
        $path = [];

        $backtrack = function () use (&$backtrack, &$result, $half, &$used, &$path, $middle) {
            if (count($path) === count($half)) {
                $prefix = implode('', $path);
                $result[] = $prefix . $middle . strrev($prefix);
                return;
            }
            foreach ($half as $index => $char) {
                if ($used[$index]) {
                    continue;
                }
                if ($index > 0 && $half[$index] === $half[$index - 1] && !$used[$index - 1]) {
                    continue;
                }
                $used[$index] = true;
                $path[] = $char;
                $backtrack();
                array_pop($path);
                $used[$index] = false;
            }
        };

        $backtrack();
        return $result;
    }
}
