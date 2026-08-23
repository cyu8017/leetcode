// LeetCode 2079 - Watering Plants
// https://leetcode.com/problems/watering-plants/

/**
 * @param {number[]} plants
 * @param {number} capacity
 * @return {number}
 */
var wateringPlants = function(plants, capacity) {
    let ans = 0, cur = capacity;
    for (let i = 0; i < plants.length; i++) {
        if (cur < plants[i]) { ans += i * 2; cur = capacity; }
        cur -= plants[i];
        ans++;
    }
    return ans;
};
