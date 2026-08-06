<?php
class Solution {
    function stringMatching($words) {
        $answer = [];
        foreach ($words as $i => $word) {
            foreach ($words as $j => $other) {
                if ($i !== $j && strpos($other, $word) !== false) {
                    $answer[] = $word;
                    break;
                }
            }
        }
        return $answer;
    }
}
