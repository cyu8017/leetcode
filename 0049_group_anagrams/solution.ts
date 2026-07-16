// LeetCode 0049 - Group Anagrams
// https://leetcode.com/problems/group-anagrams/

export function groupAnagrams(strs: string[]): string[][] {
    const groups = new Map<string, string[]>();

    for (const word of strs) {
        const key = word.split('').sort().join('');
        if (!groups.has(key)) {
            groups.set(key, []);
        }
        groups.get(key)!.push(word);
    }

    const result: string[][] = [];
    for (const group of groups.values()) {
        group.sort();
        result.push(group);
    }
    const minIndex = (group: string[]) =>
        Math.min(...group.map((word) => strs.indexOf(word)));
    result.sort((a, b) => minIndex(b) - minIndex(a));
    return result;
}
