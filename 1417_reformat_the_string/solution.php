<?php
class Solution {
    function reformat($s) {
        $letters = [];
        $digits = [];
        for ($i = 0; $i < strlen($s); $i++) {
            if (ctype_alpha($s[$i])) $letters[] = $s[$i];
            else $digits[] = $s[$i];
        }
        if (abs(count($letters) - count($digits)) > 1) return "";
        if (count($digits) >= count($letters)) {
            $tmp = $letters;
            $letters = $digits;
            $digits = $tmp;
        }
        $answer = "";
        foreach ($letters as $i => $char) {
            $answer .= $char;
            if ($i < count($digits)) $answer .= $digits[$i];
        }
        return $answer;
    }
}
