"use strict";
// LeetCode 1817 - Finding the Users Active Minutes
// https://leetcode.com/problems/finding-the-users-active-minutes/
function findingUsersActiveMinutes(logs, k) {
    const userMinutes = new Map();
    for (const [userId, minute] of logs) {
        if (!userMinutes.has(userId))
            userMinutes.set(userId, new Set());
        userMinutes.get(userId).add(minute);
    }
    const answer = new Array(k).fill(0);
    for (const minutes of userMinutes.values()) {
        const uam = minutes.size;
        if (uam <= k)
            answer[uam - 1] += 1;
    }
    return answer;
}
