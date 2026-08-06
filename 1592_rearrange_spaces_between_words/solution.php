<?php

class Solution {
    /**
     * @param String $text
     * @return String
     */
    function reorderSpaces($text) {
        $words = preg_split('/\s+/', trim($text));
        if ($words === ['']) {
            $words = [];
        }
        $spaces = substr_count($text, ' ');
        $wordCount = count($words);
        if ($wordCount === 0) {
            return str_repeat(' ', $spaces);
        }
        if ($wordCount === 1) {
            return $words[0] . str_repeat(' ', $spaces);
        }
        $between = intdiv($spaces, $wordCount - 1);
        $trailing = $spaces % ($wordCount - 1);
        return implode(str_repeat(' ', $between), $words) . str_repeat(' ', $trailing);
    }
}
