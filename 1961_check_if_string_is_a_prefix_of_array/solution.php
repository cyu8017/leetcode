<?php
class Solution {
    /**
     * @param String $s
     * @param String[] $words
     * @return Boolean
     */
    function isPrefixString($s, $words) {
        $cur = '';
        foreach ($words as $w) {
            $cur .= $w;
            if ($cur === $s) {
                return true;
            }
            if (strlen($cur) > strlen($s) || strpos($s, $cur) !== 0) {
                return false;
            }
        }
        return false;
    }
}
