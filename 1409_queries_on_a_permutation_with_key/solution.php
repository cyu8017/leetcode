<?php
class Solution {
    function processQueries($queries, $m) {
        $values = range(1, $m);
        $answer = [];
        foreach ($queries as $query) {
            $index = array_search($query, $values);
            $answer[] = $index;
            array_splice($values, $index, 1);
            array_unshift($values, $query);
        }
        return $answer;
    }
}
