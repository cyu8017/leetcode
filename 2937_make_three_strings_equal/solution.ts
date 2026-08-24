// LeetCode 2937 - Make Three Strings Equal
// https://leetcode.com/problems/make-three-strings-equal/

export function findMinimumOperations(s1: any, s2: any, s3: any): any {
    const n = Math.min(s1.length, s2.length, s3.length);
    let i = 0;
    while (i < n && s1[i] === s2[i] && s2[i] === s3[i]) i++;
    if (i === 0) return -1;
    return s1.length + s2.length + s3.length - 3 * i;
}
