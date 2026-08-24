// LeetCode 3507 - Minimum Pair Removal to Sort Array I
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

function isNonDecreasing(a) {
    for (let i = 1; i < a.length; i++) if (a[i] < a[i - 1]) return false;
    return true;
}
var minimumPairRemoval = function(nums) {
    const arr = nums.slice();
    let ans = 0;
    while (!isNonDecreasing(arr)) {
        let k = 0, s = arr[0] + arr[1];
        for (let i = 1; i + 1 < arr.length; i++) {
            const t = arr[i] + arr[i + 1];
            if (s > t) { s = t; k = i; }
        }
        arr[k] = s;
        arr.splice(k + 1, 1);
        ans++;
    }
    return ans;
};
