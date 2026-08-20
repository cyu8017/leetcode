"use strict";
// LeetCode 1564 - Put Boxes Into the Warehouse I
// https://leetcode.com/problems/put-boxes-into-the-warehouse-i/
// @ts-nocheck
function maxBoxesInWarehouse(boxes, warehouse) {
    for (let i = 1; i < warehouse.length; i++) {
        warehouse[i] = Math.min(warehouse[i], warehouse[i - 1]);
    }
    boxes.sort((a, b) => a - b);
    let room = warehouse.length - 1, used = 0;
    for (const box of boxes) {
        while (room >= 0 && warehouse[room] < box)
            room--;
        if (room < 0)
            break;
        used++;
        room--;
    }
    return used;
}
