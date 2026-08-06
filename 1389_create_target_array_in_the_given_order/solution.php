<?php
class Solution {
    function createTargetArray($nums, $index) {
        $out = [];
        foreach ($nums as $i => $x) {
            array_splice($out, $index[$i], 0, [$x]);
        }
        return $out;
    }
}
