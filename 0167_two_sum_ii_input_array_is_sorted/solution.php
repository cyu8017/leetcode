// LeetCode 0167 - Two Sum II - Input Array Is Sorted
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution {
    function twoSum(array $numbers, int $target): array {
        $left = 0;
        $right = count($numbers) - 1;
        while ($left < $right) {
            $sum = $numbers[$left] + $numbers[$right];
            if ($sum === $target) return [$left + 1, $right + 1];
            if ($sum < $target) $left++;
            else $right--;
        }
        return [];
    }
}