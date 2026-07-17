"use strict";
// LeetCode 1710 - Maximum Units on a Truck
// https://leetcode.com/problems/maximum-units-on-a-truck/
function maximumUnits(boxTypes, truckSize) {
    boxTypes.sort((a, b) => b[1] - a[1]);
    let total = 0;
    for (const [count, units] of boxTypes) {
        const take = Math.min(count, truckSize);
        total += take * units;
        truckSize -= take;
        if (truckSize === 0) {
            break;
        }
    }
    return total;
}
