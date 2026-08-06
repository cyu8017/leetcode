<?php
class Solution {
    function isPrefixOfWord($sentence, $searchWord) {
        foreach (explode(" ", $sentence) as $i => $w) {
            if (strpos($w, $searchWord) === 0) return $i + 1;
        }
        return -1;
    }
}
