// LeetCode 2566 - Maximum Difference by Remapping a Digit
// https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

/**
 * @param {number} num
 * @return {number}
 */
var minMaxDifference = function(num) {
    const s = String(num);
    const remap = (from, to) => {
        let v = 0;
        for (const c of s) {
            const d = c === from ? to : c;
            v = v * 10 + (d.charCodeAt(0) - 48);
        }
        return v;
    };
    let maxV = num;
    for (const c of s) {
        if (c !== '9') {
            maxV = remap(c, '9');
            break;
        }
    }
    const minV = remap(s[0], '0');
    return maxV - minV;
};
