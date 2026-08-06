<?php
class Solution {
    function buildArray($target, $n) {
        $answer = [];
        $current = 1;
        foreach ($target as $value) {
            while ($current < $value) {
                $answer[] = "Push";
                $answer[] = "Pop";
                $current++;
            }
            $answer[] = "Push";
            $current++;
        }
        return $answer;
    }
}
