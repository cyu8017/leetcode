// LeetCode 2822 - Inversion of Object
// https://leetcode.com/problems/inversion-of-object/

export function invertObject(obj: any | any[]): any {
    const inverted = {};
    for (const key of Object.keys(obj)) {
        const val = obj[key];
        if (val in inverted) {
            if (!Array.isArray(inverted[val])) inverted[val] = [inverted[val]];
            inverted[val].push(key);
        } else {
            inverted[val] = key;
        }
    }
    return inverted;
}
