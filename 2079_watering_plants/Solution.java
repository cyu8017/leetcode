// LeetCode 2079 - Watering Plants
// https://leetcode.com/problems/watering-plants/

class Solution {
    public int wateringPlants(int[] plants, int capacity) {
        int ans = 0, cur = capacity;
        for (int i = 0; i < plants.length; i++) {
            if (cur < plants[i]) { ans += i * 2; cur = capacity; }
            cur -= plants[i];
            ans++;
        }
        return ans;
    }
}
