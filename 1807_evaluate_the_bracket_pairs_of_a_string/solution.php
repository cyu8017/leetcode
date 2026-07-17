<?php
// LeetCode 1807 - Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

class Solution {
    /**
     * @param String $s
     * @param String[][] $knowledge
     * @return String
     */
    function evaluate($s, $knowledge) {
        $lookup = [];
        foreach ($knowledge as [$key, $value]) {
            $lookup[$key] = $value;
        }

        $result = [];
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === '(') {
                $j = strpos($s, ')', $i + 1);
                $key = substr($s, $i + 1, $j - $i - 1);
                $result[] = $lookup[$key] ?? '?';
                $i = $j;
            } else {
                $result[] = $s[$i];
            }
        }
        return implode('', $result);
    }
}
