<?php
class Solution {
    function largestMultipleOfThree($digits) {
        $cnt = array_fill(0, 10, 0);
        $sum = 0;
        foreach ($digits as $d) {
            $cnt[$d]++;
            $sum += $d;
        }
        $rem = $sum % 3;
        $remove = function($r, $k) use (&$cnt) {
            for ($d = $r; $d < 10; $d += 3) {
                while ($cnt[$d] && $k) {
                    $cnt[$d]--;
                    $k--;
                }
                if (!$k) return true;
            }
            return false;
        };
        if ($rem && !$remove($rem, 1)) $remove(3 - $rem, 2);
        $s = "";
        for ($d = 9; $d >= 0; $d--) $s .= str_repeat(strval($d), $cnt[$d]);
        if ($s !== "" && $s[0] === "0") return "0";
        return $s;
    }
}
