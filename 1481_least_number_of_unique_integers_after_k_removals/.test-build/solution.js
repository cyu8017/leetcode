"use strict";
function findLeastNumOfUniqueInts(arr, k) {
    const frequencies = new Map();
    for (const value of arr)
        frequencies.set(value, (frequencies.get(value) || 0) + 1);
    const counts = [...frequencies.values()].sort((a, b) => a - b);
    let remaining = counts.length;
    for (const count of counts) {
        if (k < count)
            break;
        k -= count;
        remaining--;
    }
    return remaining;
}
