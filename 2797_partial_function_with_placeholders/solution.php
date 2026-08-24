<?php
// LeetCode 2797 - Partial Function with Placeholders
// https://leetcode.com/problems/partial-function-with-placeholders/

class Solution {
    function partial($fn, $args) {
        return function(...$restArgs) use ($fn, $args) {
            $full = [];
            $ri = 0;
            foreach ($args as $a) {
                if ($a === '_') {
                    if ($ri < count($restArgs)) $full[] = $restArgs[$ri++];
                } else {
                    $full[] = $a;
                }
            }
            while ($ri < count($restArgs)) $full[] = $restArgs[$ri++];
            return $fn(...$full);
        };
    }
}
