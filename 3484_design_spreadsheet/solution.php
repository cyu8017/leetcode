<?php
// LeetCode 3484 - Design Spreadsheet
// https://leetcode.com/problems/design-spreadsheet/

class Spreadsheet {
    public $cells;

    function __construct($rows) {
        $this->cells = [];
    }

    function setCell($cell, $value) {
        $this->cells[$cell] = $value;
    }

    function resetCell($cell) {
        unset($this->cells[$cell]);
    }

    function getValue($formula) {
        if (strlen($formula) && $formula[0] === "=") $formula = substr($formula, 1);
        $sum = 0;
        $start = 0;
        $n = strlen($formula);
        while ($start < $n) {
            $plus = strpos($formula, "+", $start);
            $p = $plus === false ? substr($formula, $start) : substr($formula, $start, $plus - $start);
            $plen = strlen($p);
            $isNum = $plen && (($p[0] >= "0" && $p[0] <= "9") || ($p[0] === "-" && $plen > 1));
            if ($isNum) {
                for ($i = 1; $i < $plen; $i++) {
                    if ($p[$i] < "0" || $p[$i] > "9") { $isNum = false; break; }
                }
            }
            if ($isNum) $sum += intval($p);
            else $sum += $this->cells[$p] ?? 0;
            if ($plus === false) break;
            $start = $plus + 1;
        }
        return $sum;
    }
}
