"use strict";
// LeetCode 1310 - Xor Queries Of A Subarray
// https://leetcode.com/problems/xor-queries-of-a-subarray/
function xorQueries(arr, queries) {
    const prefix = [0];
    for (const value of arr)
        prefix.push(prefix[prefix.length - 1] ^ value);
    return queries.map(([left, right]) => prefix[right + 1] ^ prefix[left]);
}
