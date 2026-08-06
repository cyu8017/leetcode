<?php
class Solution {
    function printVertically($s) {
        $words = explode(" ", $s);
        $maxLen = 0;
        foreach ($words as $w) $maxLen = max($maxLen, strlen($w));
        $answer = [];
        for ($i = 0; $i < $maxLen; $i++) {
            $row = "";
            foreach ($words as $word) {
                $row .= $i < strlen($word) ? $word[$i] : " ";
            }
            $answer[] = rtrim($row);
        }
        return $answer;
    }
}
