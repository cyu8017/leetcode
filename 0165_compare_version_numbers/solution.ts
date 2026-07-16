// LeetCode 0165 - Compare Version Numbers
// https://leetcode.com/problems/compare-version-numbers/

export function compareVersion(version1: string, version2: string): number {
    const first = version1.split('.');
    const second = version2.split('.');
    const length = Math.max(first.length, second.length);

    for (let index = 0; index < length; index++) {
        const left = Number(first[index] ?? 0);
        const right = Number(second[index] ?? 0);
        if (left < right) {
            return -1;
        }
        if (left > right) {
            return 1;
        }
    }
    return 0;
}