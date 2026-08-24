// LeetCode 2079 - Watering Plants
// https://leetcode.com/problems/watering-plants/

export function wateringPlants(plants: number[], capacity: number): number {
    let ans = 0, cur = capacity;
    for (let i = 0; i < plants.length; i++) {
        if (cur < plants[i]) { ans += i * 2; cur = capacity; }
        cur -= plants[i];
        ans++;
    }
    return ans;
}
