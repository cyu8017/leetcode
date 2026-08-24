// LeetCode 2794 - Create Object from Two Arrays
// https://leetcode.com/problems/create-object-from-two-arrays/

export function createObject(keysArr: any[], valuesArr: any[]): any {
    const output = {};
    const n = Math.min(keysArr.length, valuesArr.length);
    for (let i = 0; i < n; i++) {
        if (!(keysArr[i] in output)) output[keysArr[i]] = valuesArr[i];
    }
    return output;
}
