<?php
// LeetCode 0306 - Additive Number
// https://leetcode.com/problems/additive-number/

class Solution {
    /**
     * @param String $num
     * @return Boolean
     */
    function isAdditiveNumber($num) {
        $valid = function ($first, $second, $start) use ($num) {
            if ((strlen($first) > 1 && $first[0] === "0") || (strlen($second) > 1 && $second[0] === "0")) {
                return false;
            }
            $length = strlen($num);
            while ($start < $length) {
                $total = (string)((int)$first + (int)$second);
                if (substr($num, $start, strlen($total)) !== $total) {
                    return false;
                }
                $first = $second;
                $second = $total;
                $start += strlen($total);
            }
            return true;
        };

        $length = strlen($num);
        for ($firstEnd = 1; $firstEnd < $length; $firstEnd++) {
            for ($secondEnd = $firstEnd + 1; $secondEnd < $length; $secondEnd++) {
                if ($valid(substr($num, 0, $firstEnd), substr($num, $firstEnd, $secondEnd - $firstEnd), $secondEnd)) {
                    return true;
                }
            }
        }
        return false;
    }
}
