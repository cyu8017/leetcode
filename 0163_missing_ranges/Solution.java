import java.util.*;
class Solution {
    public List<List<Integer>> findMissingRanges(int[] nums, int lower, int upper) {
        List<List<Integer>> result = new ArrayList<>(); long previous = (long) lower - 1;
        for (int i = 0; i <= nums.length; i++) { long current = i == nums.length ? (long) upper + 1 : nums[i]; if (current - previous >= 2) result.add(Arrays.asList((int) (previous + 1), (int) (current - 1))); previous = current; }
        return result;
    }
}