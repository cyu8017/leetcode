<?php
// LeetCode 3541 - Find Most Frequent Vowel and Consonant
// https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

class Solution {
    function maxFreqSum($s) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $cnt[ord($s[$i]) - 97]++;
        $a = 0;
        $b = 0;
        $vowels = ['a' => 1, 'e' => 1, 'i' => 1, 'o' => 1, 'u' => 1];
        for ($i = 0; $i < 26; $i++) {
            $c = chr(97 + $i);
            if (isset($vowels[$c])) $a = max($a, $cnt[$i]);
            else $b = max($b, $cnt[$i]);
        }
        return $a + $b;
    }
}
