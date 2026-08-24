// LeetCode 2727 - Is Object Empty
// https://leetcode.com/problems/is-object-empty/

export function isEmpty(obj: any | any[]): boolean {
    if (Array.isArray(obj)) return obj.length === 0;
    return Object.keys(obj).length === 0;
}
