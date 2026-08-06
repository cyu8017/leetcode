<?php
class Solution {
    function displayTable($orders) {
        $foods = [];
        $tables = [];
        $counts = [];
        foreach ($orders as [$customer, $table, $food]) {
            $foods[$food] = true;
            $tables[intval($table)] = true;
            $key = intval($table) . "|" . $food;
            $counts[$key] = ($counts[$key] ?? 0) + 1;
        }
        $foodList = array_keys($foods);
        sort($foodList);
        $tableList = array_keys($tables);
        sort($tableList);
        $result = [array_merge(["Table"], $foodList)];
        foreach ($tableList as $table) {
            $row = [strval($table)];
            foreach ($foodList as $food) $row[] = strval($counts[$table . "|" . $food] ?? 0);
            $result[] = $row;
        }
        return $result;
    }
}
