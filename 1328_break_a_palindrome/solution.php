<?php
class Solution {
    function breakPalindrome($palindrome) {
        if (strlen($palindrome) === 1) return "";
        $chars = str_split($palindrome);
        $n = count($chars);
        for ($i = 0; $i < intdiv($n, 2); $i++) {
            if ($chars[$i] !== "a") {
                $chars[$i] = "a";
                return implode("", $chars);
            }
        }
        $chars[$n - 1] = "b";
        return implode("", $chars);
    }
}
