// LeetCode 0169 - Majority Element
// https://leetcode.com/problems/majority-element/

class Solution {
    function majorityElement(array $nums): int {
        $candidate = 0;
        $count = 0;
        foreach ($nums as $number) {
            if ($count === 0) $candidate = $number;
            $count += $number === $candidate ? 1 : -1;
        }
        return $candidate;
    }
}