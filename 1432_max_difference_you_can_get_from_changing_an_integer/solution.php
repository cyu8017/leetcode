<?php
class Solution {
    function maxDiff($num) {
        $s = strval($num);
        $high = $s;
        for ($i = 0; $i < strlen($s); $i++) {
            if ($s[$i] !== "9") {
                $high = str_replace($s[$i], "9", $s);
                break;
            }
        }
        $low = $s;
        if ($s[0] !== "1") {
            $low = str_replace($s[0], "1", $s);
        } else {
            for ($i = 1; $i < strlen($s); $i++) {
                if ($s[$i] !== "0" && $s[$i] !== "1") {
                    $low = str_replace($s[$i], "0", $s);
                    break;
                }
            }
        }
        return intval($high) - intval($low);
    }
}
