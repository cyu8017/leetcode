// LeetCode 2446 - Determine if Two Events Have Conflict
// https://leetcode.com/problems/determine-if-two-events-have-conflict/

export function haveConflict(event1: string[], event2: string[]): boolean {
    return event1[0] <= event2[1] && event2[0] <= event1[1];
}
