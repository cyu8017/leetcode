<?php
// LeetCode 0859 - Buddy Strings
// https://leetcode.com/problems/buddy-strings/

class Solution {
    /**
     * @param String $s
     * @param String $goal
     * @return Boolean
     */
    function buddyStrings($s, $goal) {
        if (strlen($s) !== strlen($goal)) return false;
        if ($s === $goal) {
            $set = [];
            $n = strlen($s);
            for ($i = 0; $i < $n; $i++) {
                $ch = $s[$i];
                if (isset($set[$ch])) return true;
                $set[$ch] = true;
            }
            return false;
        }
        $diffs = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] !== $goal[$i]) $diffs[] = [$s[$i], $goal[$i]];
        }
        return count($diffs) === 2 && $diffs[0][0] === $diffs[1][1] && $diffs[0][1] === $diffs[1][0];
    }
}
