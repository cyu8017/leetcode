<?php
// LeetCode 1002 - Find Common Characters
// https://leetcode.com/problems/find-common-characters/

class Solution {
    /**
     * @param String[] $words
     * @return String[]
     */
    function commonChars($words) {
        $common = array_count_values(str_split($words[0]));
        for ($w = 1; $w < count($words); $w++) {
            $cnt = array_count_values(str_split($words[$w]));
            foreach ($common as $ch => $_) {
                if (!isset($cnt[$ch])) {
                    unset($common[$ch]);
                } else {
                    $common[$ch] = min($common[$ch], $cnt[$ch]);
                }
            }
        }
        $ans = [];
        foreach ($common as $ch => $times) {
            for ($i = 0; $i < $times; $i++) {
                $ans[] = $ch;
            }
        }
        return $ans;
    }
}
