<?php
// LeetCode 0820 - Short Encoding of Words
// https://leetcode.com/problems/short-encoding-of-words/

class Solution {
    /**
     * @param String[] $words
     * @return Integer
     */
    function minimumLengthEncoding($words) {
        $good = [];
        foreach ($words as $word) $good[$word] = true;
        foreach ($words as $word) {
            $len = strlen($word);
            for ($i = 1; $i < $len; $i++) unset($good[substr($word, $i)]);
        }
        $ans = 0;
        foreach ($good as $word => $_) $ans += strlen($word) + 1;
        return $ans;
    }
}
