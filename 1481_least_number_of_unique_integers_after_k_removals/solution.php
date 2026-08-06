<?php
class Solution {
    function findLeastNumOfUniqueInts($arr, $k) {
        $counts = array_values(array_count_values($arr));
        sort($counts);
        $removed = 0;
        foreach ($counts as $count) {
            if ($k < $count) break;
            $k -= $count;
            $removed++;
        }
        return count($counts) - $removed;
    }
}
