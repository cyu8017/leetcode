// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

/**
 * @param {number[]} status
 * @param {number[]} candies
 * @param {number[][]} keys
 * @param {number[][]} containedBoxes
 * @param {number[]} initialBoxes
 * @return {number}
 */
var maxCandies = function(status, candies, keys, containedBoxes, initialBoxes) {
    const owned = new Set(initialBoxes);
    const opened = new Set();
    const queue = initialBoxes.filter((box) => status[box] === 1);
    let total = 0;
    while (queue.length) {
        const box = queue.shift();
        if (opened.has(box) || status[box] === 0) continue;
        opened.add(box);
        total += candies[box];
        for (const key of keys[box]) {
            status[key] = 1;
            if (owned.has(key) && !opened.has(key)) queue.push(key);
        }
        for (const child of containedBoxes[box]) {
            owned.add(child);
            if (status[child] === 1 && !opened.has(child)) queue.push(child);
        }
    }
    return total;
};
