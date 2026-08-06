<?php
class Solution {
    function freqAlphabets($s) {
        $answer = [];
        $i = strlen($s) - 1;
        while ($i >= 0) {
            if ($s[$i] === "#") {
                $answer[] = chr(96 + intval(substr($s, $i - 2, 2)));
                $i -= 3;
            } else {
                $answer[] = chr(96 + intval($s[$i]));
                $i -= 1;
            }
        }
        return implode("", array_reverse($answer));
    }
}
