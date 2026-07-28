// LeetCode 1093 - Statistics from a Large Sample
// https://leetcode.com/problems/statistics-from-a-large-sample/

/**
 * @param {number[]} count
 * @return {number[]}
 */
var sampleStats = function(count) {
    let total = 0;
    for (const c of count) total += c;
    let minimum = 0;
    while (!count[minimum]) minimum++;
    let maximum = 255;
    while (!count[maximum]) maximum--;
    let sum = 0;
    let mode = 0;
    let modeCnt = -1;
    for (let i = 0; i < 256; i++) {
        sum += i * count[i];
        if (count[i] > modeCnt) {
            modeCnt = count[i];
            mode = i;
        }
    }
    const mean = sum / total;
    const mid1 = Math.floor((total + 1) / 2);
    const mid2 = Math.floor((total + 2) / 2);
    let seen = 0;
    let first = null;
    let second = null;
    for (let i = 0; i < 256; i++) {
        seen += count[i];
        if (first === null && seen >= mid1) first = i;
        if (second === null && seen >= mid2) {
            second = i;
            break;
        }
    }
    const median = (first + second) / 2;
    return [minimum, maximum, mean, median, mode];
};
