<?php
class Solution {
    function arrangeWords($text) {
        $words = explode(" ", strtolower($text));
        usort($words, function($a, $b) {
            $la = strlen($a);
            $lb = strlen($b);
            if ($la !== $lb) return $la <=> $lb;
            return 0;
        });
        $s = implode(" ", $words);
        return $s === "" ? "" : strtoupper($s[0]) . substr($s, 1);
    }
}
