<?php
class Solution {
    function findLucky($arr) {
        $c = array_count_values($arr);
        $ans = -1;
        foreach ($c as $x => $cnt) if ($x === $cnt) $ans = max($ans, $x);
        return $ans;
    }
}
