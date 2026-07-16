// LeetCode 0219 - Contains Duplicate II
// https://leetcode.com/problems/contains-duplicate-ii/

class Solution {
    function containsNearbyDuplicate($nums, $k) {
        $lastIndex = [];
        foreach ($nums as $i => $num) {
            if (isset($lastIndex[$num]) && $i - $lastIndex[$num] <= $k) {
                return true;
            }
            $lastIndex[$num] = $i;
        }
        return false;
    }
}
