<?php
class Solution {
    function sortString($s) {
        $c = array_fill(0, 26, 0);
        for ($i = 0; $i < strlen($s); $i++) $c[ord($s[$i]) - 97]++;
        $out = "";
        while (strlen($out) < strlen($s)) {
            for ($i = 0; $i < 26; $i++) {
                if ($c[$i]) {
                    $out .= chr(97 + $i);
                    $c[$i]--;
                }
            }
            for ($i = 25; $i >= 0; $i--) {
                if ($c[$i]) {
                    $out .= chr(97 + $i);
                    $c[$i]--;
                }
            }
        }
        return $out;
    }
}
