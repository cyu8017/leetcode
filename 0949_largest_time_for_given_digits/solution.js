// LeetCode 0949 - Largest Time for Given Digits
// https://leetcode.com/problems/largest-time-for-given-digits/

/**
 * @param {number[]} arr
 * @return {string}
 */
var largestTimeFromDigits = function(arr) {
    arr.sort((a, b) => a - b);
    let best = "";
    const nextPermutation = (a) => {
        let i = a.length - 2;
        while (i >= 0 && a[i] >= a[i + 1]) i--;
        if (i < 0) return false;
        let j = a.length - 1;
        while (a[j] <= a[i]) j--;
        let tmp = a[i]; a[i] = a[j]; a[j] = tmp;
        for (let l = i + 1, r = a.length - 1; l < r; l++, r--) {
            tmp = a[l]; a[l] = a[r]; a[r] = tmp;
        }
        return true;
    };
    do {
        const hours = 10 * arr[0] + arr[1];
        const minutes = 10 * arr[2] + arr[3];
        if (hours < 24 && minutes < 60) {
            const cand = String(hours).padStart(2, "0") + ":" + String(minutes).padStart(2, "0");
            if (cand > best) best = cand;
        }
    } while (nextPermutation(arr));
    return best;
};
