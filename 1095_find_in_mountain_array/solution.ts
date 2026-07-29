// LeetCode 1095 - Find in Mountain Array
// https://leetcode.com/problems/find-in-mountain-array/

interface MountainArray {
    get(index: number): number;
    length(): number;
}

function findInMountainArray(target: number, mountainArr: MountainArray): number {
    const n = mountainArr.length();
    let lo = 0;
    let hi = n - 1;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (mountainArr.get(mid) < mountainArr.get(mid + 1)) lo = mid + 1;
        else hi = mid;
    }
    const peak = lo;
    lo = 0;
    hi = peak;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        const val = mountainArr.get(mid);
        if (val === target) return mid;
        if (val < target) lo = mid + 1;
        else hi = mid - 1;
    }
    lo = peak + 1;
    hi = n - 1;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        const val = mountainArr.get(mid);
        if (val === target) return mid;
        if (val > target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}
