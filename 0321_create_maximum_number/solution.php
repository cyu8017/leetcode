// LeetCode 0321 - Create Maximum Number
// https://leetcode.com/problems/create-maximum-number/

class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k
     * @return Integer[]
     */
    function maxNumber($nums1, $nums2, $k) {
        $pickMax = function ($values, $count) {
            $drop = count($values) - $count;
            $stack = [];
            foreach ($values as $value) {
                while ($drop > 0 && !empty($stack) && $stack[count($stack) - 1] < $value) {
                    array_pop($stack);
                    $drop--;
                }
                $stack[] = $value;
            }
            return array_slice($stack, 0, $count);
        };

        $suffixGreater = function ($first, $left, $second, $right) {
            $firstCount = count($first);
            $secondCount = count($second);
            while ($left < $firstCount && $right < $secondCount) {
                if ($first[$left] !== $second[$right]) {
                    return $first[$left] > $second[$right];
                }
                $left++;
                $right++;
            }
            return $left < $firstCount;
        };

        $merge = function ($first, $second) use (&$suffixGreater) {
            $result = [];
            $left = 0;
            $right = 0;
            $firstCount = count($first);
            $secondCount = count($second);
            while ($left < $firstCount && $right < $secondCount) {
                if ($suffixGreater($first, $left, $second, $right)) {
                    $result[] = $first[$left];
                    $left++;
                } else {
                    $result[] = $second[$right];
                    $right++;
                }
            }
            while ($left < $firstCount) {
                $result[] = $first[$left];
                $left++;
            }
            while ($right < $secondCount) {
                $result[] = $second[$right];
                $right++;
            }
            return $result;
        };

        $best = [];
        $startTake = max(0, $k - count($nums2));
        $endTake = min($k, count($nums1));
        for ($takeFirst = $startTake; $takeFirst <= $endTake; $takeFirst++) {
            $takeSecond = $k - $takeFirst;
            $candidate = $merge($pickMax($nums1, $takeFirst), $pickMax($nums2, $takeSecond));
            if ($candidate > $best) {
                $best = $candidate;
            }
        }
        return $best;
    }
}
