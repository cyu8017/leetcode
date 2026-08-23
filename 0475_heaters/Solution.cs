// LeetCode 0475 - Heaters
// https://leetcode.com/problems/heaters/

public class Solution {
    public int FindRadius(int[] houses, int[] heaters) {
        Array.Sort(heaters);
        int radius = 0;
        foreach (int house in houses) {
            int position = Array.BinarySearch(heaters, house);
            if (position < 0) {
                position = ~position;
            }
            int best = int.MaxValue;
            if (position < heaters.Length) {
                best = Math.Min(best, Math.Abs(heaters[position] - house));
            }
            if (position > 0) {
                best = Math.Min(best, Math.Abs(heaters[position - 1] - house));
            }
            radius = Math.Max(radius, best);
        }
        return radius;
    }
}
