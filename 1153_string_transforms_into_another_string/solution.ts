// LeetCode 1153 - String Transforms Into Another String
// https://leetcode.com/problems/string-transforms-into-another-string/

function canConvert(str1: string, str2: string): boolean {
    if (str1 === str2) return true;
    const mapping = new Map();
    for (let i = 0; i < str1.length; i++) {
        const a = str1[i], b = str2[i];
        if (mapping.has(a) && mapping.get(a) !== b) return false;
        mapping.set(a, b);
    }
    return new Set(str2).size < 26;
}
