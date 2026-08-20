"use strict";
// LeetCode 1394: Find Lucky Integer In An Array
function findLucky(arr) {
    const count = new Map();
    for (const value of arr)
        count.set(value, (count.get(value) || 0) + 1);
    let answer = -1;
    for (const [value, frequency] of count)
        if (value === frequency)
            answer = Math.max(answer, value);
    return answer;
}
