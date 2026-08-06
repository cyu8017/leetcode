<?php
class Solution {
    function maximum69Number($num) {
        $s = strval($num);
        $pos = strpos($s, "6");
        if ($pos !== false) $s[$pos] = "9";
        return intval($s);
    }
}
