<?php
// LeetCode 0631 - Design Excel Sum Formula
// https://leetcode.com/problems/design-excel-sum-formula/

class Excel {
    private $values;
    private $formulas;

    function __construct($height, $width) {
        $cols = ord($width) - 64;
        $this->values = [];
        for ($r = 0; $r <= $height; ++$r) $this->values[$r] = array_fill(0, $cols, 0);
        $this->formulas = [];
    }

    private function key($row, $col) {
        return $row . "," . $col;
    }

    private function parse($cell) {
        return [intval(substr($cell, 1)), ord($cell[0]) - 65];
    }

    private function evalCell($row, $col) {
        $formula = $this->formulas[$this->key($row, $col)] ?? null;
        if ($formula) {
            $total = 0;
            foreach ($formula as $cell) $total += $this->evalCell($cell[0], $cell[1]);
            return $total;
        }
        return $this->values[$row][$col];
    }

    function set($row, $column, $val) {
        $col = ord($column) - 65;
        unset($this->formulas[$this->key($row, $col)]);
        $this->values[$row][$col] = $val;
    }

    function get($row, $column) {
        return $this->evalCell($row, ord($column) - 65);
    }

    function sum($row, $column, $numbers) {
        $col = ord($column) - 65;
        $cells = [];
        foreach ($numbers as $token) {
            $colon = strpos($token, ":");
            if ($colon !== false) {
                $p1 = $this->parse(substr($token, 0, $colon));
                $p2 = $this->parse(substr($token, $colon + 1));
                for ($r = $p1[0]; $r <= $p2[0]; ++$r) {
                    for ($c = $p1[1]; $c <= $p2[1]; ++$c) $cells[] = [$r, $c];
                }
            } else {
                $cells[] = $this->parse($token);
            }
        }
        $this->formulas[$this->key($row, $col)] = $cells;
        return $this->evalCell($row, $col);
    }
}
