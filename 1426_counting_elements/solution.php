<?php
class Solution {
    function countElements($arr) {
        $values = array_flip($arr);
        $ans = 0;
        foreach ($arr as $value) if (isset($values[$value + 1])) $ans++;
        return $ans;
    }
}
