<?php
class Solution {
    function arrayRankTransform($arr) {
        $uniq = array_values(array_unique($arr));
        sort($uniq);
        $rank = [];
        foreach ($uniq as $i => $value) $rank[$value] = $i + 1;
        $answer = [];
        foreach ($arr as $value) $answer[] = $rank[$value];
        return $answer;
    }
}
