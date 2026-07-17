<?php
// LeetCode 1898 - Maximum Number of Removable Characters
// https://leetcode.com/problems/maximum-number-of-removable-characters/

class Solution {
    /**
     * @param String $s
     * @param String $p
     * @param Integer[] $removable
     * @return Integer
     */
    function maximumRemovals($s, $p, $removable) {
        $stillSubsequence = function ($k) use ($s, $p, $removable) {
            $removed = array_flip(array_slice($removable, 0, $k));
            $index = 0;
            $len = strlen($s);
            $pLen = strlen($p);
            for ($position = 0; $position < $len; $position++) {
                if (isset($removed[$position])) {
                    continue;
                }
                if ($index < $pLen && $s[$position] === $p[$index]) {
                    $index++;
                }
            }
            return $index === $pLen;
        };

        $lo = 0;
        $hi = count($removable);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi + 1, 2);
            if ($stillSubsequence($mid)) {
                $lo = $mid;
            } else {
                $hi = $mid - 1;
            }
        }
        return $lo;
    }
}
