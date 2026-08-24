<?php
// LeetCode 0770 - Basic Calculator IV
// https://leetcode.com/problems/basic-calculator-iv/

class Solution {
    function basicCalculatorIV($expression, $evalvars, $evalints) {
        $values = [];
        for ($i = 0; $i < count($evalvars); $i++) $values[$evalvars[$i]] = $evalints[$i];
        $tokens = [];
        $cur = '';
        $elen = strlen($expression);
        for ($ti = 0; $ti < $elen; $ti++) {
            $ch = $expression[$ti];
            if ($ch === '(' || $ch === ')') {
                if (strlen($cur) > 0) { $tokens[] = $cur; $cur = ''; }
                $tokens[] = $ch;
            } else if (preg_match('/\s/', $ch)) {
                if (strlen($cur) > 0) { $tokens[] = $cur; $cur = ''; }
            } else $cur .= $ch;
        }
        if (strlen($cur) > 0) $tokens[] = $cur;
        $pos = 0;

        $keyOf = function ($items) { return implode("\0", $items); };
        $itemsOf = function ($key) { return $key === '' ? [] : explode("\0", $key); };

        $clean = function ($poly) {
            foreach ($poly as $k => $v) if ($v === 0) unset($poly[$k]);
            return $poly;
        };

        $add = function ($left, $right) use ($clean) {
            $result = $left;
            foreach ($right as $k => $v) $result[$k] = ($result[$k] ?? 0) + $v;
            return $clean($result);
        };

        $negate = function ($poly) {
            $result = [];
            foreach ($poly as $k => $v) $result[$k] = -$v;
            return $result;
        };

        $mul = function ($left, $right) use ($clean, $itemsOf, $keyOf) {
            $result = [];
            foreach ($left as $lk => $lv) {
                foreach ($right as $rk => $rv) {
                    $keyList = array_merge($itemsOf($lk), $itemsOf($rk));
                    sort($keyList);
                    $key = $keyOf($keyList);
                    $result[$key] = ($result[$key] ?? 0) + $lv * $rv;
                }
            }
            return $clean($result);
        };

        $atom = function ($token) use ($values, $clean, $keyOf) {
            $poly = [];
            if (preg_match('/[a-zA-Z]/', $token[0])) {
                if (array_key_exists($token, $values)) $poly[''] = $values[$token];
                else $poly[$keyOf([$token])] = 1;
            } else $poly[''] = intval($token, 10);
            return $clean($poly);
        };

        $parseExpr = null;
        $parseFactor = function () use (&$parseFactor, &$parseExpr, &$tokens, &$pos, $atom) {
            if ($tokens[$pos] === '(') {
                $pos++;
                $poly = $parseExpr();
                $pos++;
                return $poly;
            }
            return $atom($tokens[$pos++]);
        };

        $parseTerm = function () use (&$parseFactor, &$tokens, &$pos, $mul) {
            $poly = $parseFactor();
            while ($pos < count($tokens) && $tokens[$pos] === '*') {
                $pos++;
                $poly = $mul($poly, $parseFactor());
            }
            return $poly;
        };

        $parseExpr = function () use (&$parseTerm, &$tokens, &$pos, $add, $negate) {
            $poly = $parseTerm();
            while ($pos < count($tokens) && ($tokens[$pos] === '+' || $tokens[$pos] === '-')) {
                $op = $tokens[$pos++];
                $right = $parseTerm();
                $poly = $add($poly, $op === '+' ? $right : $negate($right));
            }
            return $poly;
        };

        $compareLists = function ($a, $b) {
            $n = min(count($a), count($b));
            for ($i = 0; $i < $n; $i++) {
                if ($a[$i] < $b[$i]) return -1;
                if ($a[$i] > $b[$i]) return 1;
            }
            return count($a) - count($b);
        };

        $poly = $parseExpr();
        $keys = [];
        foreach ($poly as $k => $v) $keys[] = [$k, $v];
        usort($keys, function ($a, $b) use ($itemsOf, $compareLists) {
            $ai = $itemsOf($a[0]);
            $bi = $itemsOf($b[0]);
            if (count($ai) !== count($bi)) return count($bi) - count($ai);
            return $compareLists($ai, $bi);
        });
        $answer = [];
        foreach ($keys as $pair) {
            $k = $pair[0];
            $v = $pair[1];
            if ($v === 0) continue;
            $items = $itemsOf($k);
            if (count($items) === 0) $answer[] = (string)$v;
            else $answer[] = (string)$v . '*' . implode('*', $items);
        }
        return $answer;
    }
}
