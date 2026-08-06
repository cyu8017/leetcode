<?php
class Solution {
    private $words;
    private $result;
    private $value = [];
    private $used;
    private $leading = [];
    private $width;

    function isSolvable($words, $result) {
        $this->words = $words;
        $this->result = $result;
        $this->value = [];
        $this->used = array_fill(0, 10, false);
        $this->leading = [];
        $maxWord = 0;
        $letters = [];
        foreach ($words as $w) {
            $maxWord = max($maxWord, strlen($w));
            foreach (str_split($w) as $c) $letters[$c] = true;
            if (strlen($w) > 1) $this->leading[$w[0]] = true;
        }
        foreach (str_split($result) as $c) $letters[$c] = true;
        if (strlen($result) > 1) $this->leading[$result[0]] = true;
        if ($maxWord > strlen($result) || count($letters) > 10) return false;
        $this->width = strlen($result);
        return $this->solve(0, 0, 0);
    }

    private function solve($column, $row, $total) {
        if ($column === $this->width) return $total === 0;
        if ($row < count($this->words)) {
            if ($column >= strlen($this->words[$row])) return $this->solve($column, $row + 1, $total);
            $ch = $this->words[$row][strlen($this->words[$row]) - 1 - $column];
            if (array_key_exists($ch, $this->value)) return $this->solve($column, $row + 1, $total + $this->value[$ch]);
            for ($digit = 0; $digit < 10; $digit++) {
                if (!$this->used[$digit] && ($digit !== 0 || !isset($this->leading[$ch]))) {
                    $this->value[$ch] = $digit;
                    $this->used[$digit] = true;
                    if ($this->solve($column, $row + 1, $total + $digit)) return true;
                    $this->used[$digit] = false;
                    unset($this->value[$ch]);
                }
            }
            return false;
        }
        $ch = $this->result[strlen($this->result) - 1 - $column];
        $digit = $total % 10;
        $carry = intdiv($total, 10);
        if (array_key_exists($ch, $this->value)) {
            return $this->value[$ch] === $digit && $this->solve($column + 1, 0, $carry);
        }
        if ($this->used[$digit] || ($digit === 0 && isset($this->leading[$ch]))) return false;
        $this->value[$ch] = $digit;
        $this->used[$digit] = true;
        $ok = $this->solve($column + 1, 0, $carry);
        $this->used[$digit] = false;
        unset($this->value[$ch]);
        return $ok;
    }
}
