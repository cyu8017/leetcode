<?php
// LeetCode 0648 - Replace Words
// https://leetcode.com/problems/replace-words/

class Solution {
    function replaceWords($dictionary, $sentence) {
        $roots = array_flip($dictionary);
        $words = explode(" ", $sentence);
        $result = [];
        foreach ($words as $word) {
            $replacement = $word;
            $len = strlen($word);
            for ($i = 1; $i <= $len; ++$i) {
                $prefix = substr($word, 0, $i);
                if (isset($roots[$prefix])) {
                    $replacement = $prefix;
                    break;
                }
            }
            $result[] = $replacement;
        }
        return implode(" ", $result);
    }
}
