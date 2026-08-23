// LeetCode 2079 - Watering Plants
// https://leetcode.com/problems/watering-plants/

public class Solution {
    public int WateringPlants(int[] plants, int capacity) {
        int ans = 0, cur = capacity;
        for (int i = 0; i < plants.Length; i++) {
            if (cur < plants[i]) { ans += i * 2; cur = capacity; }
            cur -= plants[i];
            ans++;
        }
        return ans;
    }
}
