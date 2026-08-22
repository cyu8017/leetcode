// LeetCode 2079 - Watering Plants
// https://leetcode.com/problems/watering-plants/

int wateringPlants(int* plants, int plantsSize, int capacity) {
    int ans = 0, cur = capacity;
    for (int i = 0; i < plantsSize; i++) {
        if (cur < plants[i]) { ans += i * 2; cur = capacity; }
        cur -= plants[i];
        ans++;
    }
    return ans;
}
