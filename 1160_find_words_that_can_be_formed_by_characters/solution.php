<?php
// LeetCode 1160 - Find Words That Can Be Formed by Characters
// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution {
    /**
     * @param String[] $words
     * @param String $chars
     * @return Integer
     */
    function countCharacters($words, $chars) {
        $avail = array_count_values(str_split($chars));
        $ans = 0;
        foreach ($words as $word) {
            $need = array_count_values(str_split($word));
            $ok = true;
            foreach ($need as $c => $v) {
                if (($avail[$c] ?? 0) < $v) { $ok = false; break; }
            }
            if ($ok) $ans += strlen($word);
        }
        return $ans;
    }
}
