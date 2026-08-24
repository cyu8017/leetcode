// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

export function sortBy(arr: any, fn: any): any {
    return arr.slice().sort((a, b) => fn(a) - fn(b));
}
