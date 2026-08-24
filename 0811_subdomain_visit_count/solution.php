<?php
// LeetCode 0811 - Subdomain Visit Count
// https://leetcode.com/problems/subdomain-visit-count/

class Solution {
    /**
     * @param String[] $cpdomains
     * @return String[]
     */
    function subdomainVisits($cpdomains) {
        $counts = [];
        foreach ($cpdomains as $item) {
            $space = strpos($item, ' ');
            $count = intval(substr($item, 0, $space));
            $domain = substr($item, $space + 1);
            while (true) {
                $counts[$domain] = ($counts[$domain] ?? 0) + $count;
                $dot = strpos($domain, '.');
                if ($dot === false) break;
                $domain = substr($domain, $dot + 1);
            }
        }
        $ans = [];
        foreach ($counts as $key => $value) $ans[] = $value . " " . $key;
        return $ans;
    }
}
