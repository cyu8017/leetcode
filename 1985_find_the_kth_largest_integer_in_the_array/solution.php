<?php
class Solution {
    /**
     * @param String[] $nums
     * @param Integer $k
     * @return String
     */
    function kthLargestNumber($nums, $k) {
        usort($nums, function ($a, $b) {
            $la = strlen($a);
            $lb = strlen($b);
            if ($la !== $lb) {
                return $lb <=> $la;
            }
            return strcmp($b, $a);
        });
        return $nums[$k - 1];
    }
}
