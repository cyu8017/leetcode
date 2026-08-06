<?php
class Solution {
    function findTheLongestSubstring($s) {
        $first = [0 => -1];
        $mask = 0;
        $ans = 0;
        $vowels = "aeiou";
        for ($i = 0; $i < strlen($s); $i++) {
            $pos = strpos($vowels, $s[$i]);
            if ($pos !== false) $mask ^= 1 << $pos;
            if (array_key_exists($mask, $first)) $ans = max($ans, $i - $first[$mask]);
            else $first[$mask] = $i;
        }
        return $ans;
    }
}
