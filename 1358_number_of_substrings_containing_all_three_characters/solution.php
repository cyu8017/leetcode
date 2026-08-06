<?php
class Solution {
    function numberOfSubstrings($s) {
        $last = [-1, -1, -1];
        $ans = 0;
        for ($i = 0; $i < strlen($s); $i++) {
            $last[ord($s[$i]) - 97] = $i;
            $ans += min($last) + 1;
        }
        return $ans;
    }
}
