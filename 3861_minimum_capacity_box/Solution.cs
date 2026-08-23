// LeetCode 3861 - Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/

public class Solution {
    public int MinimumIndex(int[] capacity, int itemSize) {
        int ans = -1;
        for (int i = 0; i < capacity.Length; i++) {
            if (capacity[i] >= itemSize && (ans == -1 || capacity[i] < capacity[ans])) ans = i;
        }
        return ans;
    }
}
