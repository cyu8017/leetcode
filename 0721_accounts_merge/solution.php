<?php
// LeetCode 0721 - Accounts Merge
// https://leetcode.com/problems/accounts-merge/

class Solution {
    function accountsMerge($accounts) {
        $parent = [];
        $find = function ($x) use (&$find, &$parent) {
            if (!array_key_exists($x, $parent)) $parent[$x] = $x;
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $unite = function ($a, $b) use (&$find, &$parent) {
            $parent[$find($a)] = $find($b);
        };
        $emailName = [];
        foreach ($accounts as $account) {
            $name = $account[0];
            $first = $account[1];
            for ($i = 1; $i < count($account); $i++) {
                $email = $account[$i];
                if (!array_key_exists($email, $parent)) $parent[$email] = $email;
                $emailName[$email] = $name;
                $unite($first, $email);
            }
        }
        $groups = [];
        foreach ($parent as $email => $_) {
            $root = $find($email);
            if (!isset($groups[$root])) $groups[$root] = [];
            $groups[$root][] = $email;
        }
        $result = [];
        foreach ($groups as $emails) {
            sort($emails);
            $result[] = array_merge([$emailName[$emails[0]]], $emails);
        }
        return $result;
    }
}
