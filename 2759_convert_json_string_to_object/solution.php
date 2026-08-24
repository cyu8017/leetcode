<?php
// LeetCode 2759 - Convert JSON String to Object
// https://leetcode.com/problems/convert-json-string-to-object/

class Solution {
    public $str;
    public $i;
    function jsonParse($str) {
        $this->str = $str;
        $this->i = 0;
        return $this->parse();
    }
    function parse() {
        $str = $this->str;
        if ($str[$this->i] === '"') {
            $this->i++;
            $s = '';
            while ($str[$this->i] !== '"') $s .= $str[$this->i++];
            $this->i++;
            return $s;
        }
        if ($str[$this->i] === 't') { $this->i += 4; return true; }
        if ($str[$this->i] === 'f') { $this->i += 5; return false; }
        if ($str[$this->i] === 'n') { $this->i += 4; return null; }
        if ($str[$this->i] === '[') {
            $this->i++;
            $arr = [];
            if ($str[$this->i] === ']') { $this->i++; return $arr; }
            while (true) {
                $arr[] = $this->parse();
                if ($str[$this->i] === ',') { $this->i++; continue; }
                $this->i++;
                return $arr;
            }
        }
        if ($str[$this->i] === '{') {
            $this->i++;
            $obj = [];
            if ($str[$this->i] === '}') { $this->i++; return $obj; }
            while (true) {
                $key = $this->parse();
                $this->i++;
                $obj[$key] = $this->parse();
                if ($str[$this->i] === ',') { $this->i++; continue; }
                $this->i++;
                return $obj;
            }
        }
        $start = $this->i;
        if ($str[$this->i] === '-') $this->i++;
        $n = strlen($str);
        while ($this->i < $n && (($str[$this->i] >= '0' && $str[$this->i] <= '9') || $str[$this->i] === '.')) $this->i++;
        $num = substr($str, $start, $this->i - $start);
        return strpos($num, '.') !== false ? (float)$num : (int)$num;
    }
}
