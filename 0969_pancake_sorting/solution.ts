// LeetCode 0969 - Pancake Sorting
// https://leetcode.com/problems/pancake-sorting/

export function pancakeSort(arr: number[]): number[] {
    const a = arr.slice();
    const ans = [];
    const indexOf = (v) => {
        for (let i = 0; i < a.length; i++) if (a[i] === v) return i;
        return -1;
    };
    const reverse = (l, r) => {
        while (l < r) {
            const t = a[l]; a[l] = a[r]; a[r] = t;
            l++; r--;
        }
    };
    for (let size = a.length; size > 1; size--) {
        const i = indexOf(size);
        if (i === size - 1) continue;
        if (i > 0) {
            ans.push(i + 1);
            reverse(0, i);
        }
        ans.push(size);
        reverse(0, size - 1);
    }
    return ans;
}
