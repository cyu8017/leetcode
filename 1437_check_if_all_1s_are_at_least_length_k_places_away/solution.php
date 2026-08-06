<?php
class Solution {
    function kLengthApart($nums, $k) {
        $previous = -$k - 1;
        foreach ($nums as $i => $value) {
            if ($value) {
                if ($i - $previous <= $k) return false;
                $previous = $i;
            }
        }
        return true;
    }
}
