import java.util.*;
class Solution {
    public int maximumGap(int[] nums) {
        if (nums.length < 2) return 0; int low = Arrays.stream(nums).min().getAsInt(), high = Arrays.stream(nums).max().getAsInt(); if (low == high) return 0;
        int size = Math.max(1, (high - low) / (nums.length - 1)), count = (high - low) / size + 1; int[] mins = new int[count], maxs = new int[count]; boolean[] used = new boolean[count]; Arrays.fill(mins, Integer.MAX_VALUE); Arrays.fill(maxs, Integer.MIN_VALUE);
        for (int num : nums) { int index = (num - low) / size; used[index] = true; mins[index] = Math.min(mins[index], num); maxs[index] = Math.max(maxs[index], num); }
        int best = 0, previous = low; for (int i = 0; i < count; i++) if (used[i]) { best = Math.max(best, mins[i] - previous); previous = maxs[i]; } return best;
    }
}