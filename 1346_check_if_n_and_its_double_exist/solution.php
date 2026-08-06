<?php
class Solution {
    function checkIfExist($arr) {
        $seen = [];
        foreach ($arr as $value) {
            if (isset($seen[2 * $value]) || ($value % 2 === 0 && isset($seen[intdiv($value, 2)]))) return true;
            $seen[$value] = true;
        }
        return false;
    }
}
