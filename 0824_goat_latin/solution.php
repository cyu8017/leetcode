<?php
// LeetCode 0824 - Goat Latin
// https://leetcode.com/problems/goat-latin/

class Solution {
    /**
     * @param String $sentence
     * @return String
     */
    function toGoatLatin($sentence) {
        $vowels = ['a'=>true,'e'=>true,'i'=>true,'o'=>true,'u'=>true,'A'=>true,'E'=>true,'I'=>true,'O'=>true,'U'=>true];
        $words = explode(' ', $sentence);
        $result = [];
        $n = count($words);
        for ($i = 0; $i < $n; $i++) {
            $w = $words[$i];
            if (isset($vowels[$w[0]])) $w = $w . "ma";
            else $w = substr($w, 1) . $w[0] . "ma";
            $w .= str_repeat("a", $i + 1);
            $result[] = $w;
        }
        return implode(' ', $result);
    }
}
