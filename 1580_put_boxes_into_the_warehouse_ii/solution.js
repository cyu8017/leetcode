// LeetCode 1580 - Put Boxes Into the Warehouse II
// https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/

/**
 * @param {number[]} boxes
 * @param {number[]} warehouse
 * @return {number}
 */
var maxBoxesInWarehouse = function(boxes, warehouse) {
    const n = warehouse.length;
    const left = warehouse.slice();
    const right = warehouse.slice();
    for (let i = 1; i < n; i++) left[i] = Math.min(left[i], left[i - 1]);
    for (let i = n - 2; i >= 0; i--) right[i] = Math.min(right[i], right[i + 1]);
    const capacity = [];
    for (let i = 0; i < n; i++) capacity.push(Math.max(left[i], right[i]));
    capacity.sort((a, b) => a - b);
    boxes.sort((a, b) => a - b);
    let i = 0;
    for (const room of capacity) {
        if (i < boxes.length && boxes[i] <= room) i++;
    }
    return i;
};
