<?php
// LeetCode 2785 - Sort Vowels in a String
// https://leetcode.com/problems/sort-vowels-in-a-string/

class Solution {
    function sortVowels($s) {
        $isVowel = function($c) { return strpos('aeiouAEIOU', $c) !== false; };
        $vowels = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) if ($isVowel($s[$i])) $vowels[] = $s[$i];
        sort($vowels);
        $arr = str_split($s);
        $vi = 0;
        for ($i = 0; $i < count($arr); $i++) if ($isVowel($arr[$i])) $arr[$i] = $vowels[$vi++];
        return implode('', $arr);
    }
}
