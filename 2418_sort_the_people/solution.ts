// LeetCode 2418 - Sort the People
// https://leetcode.com/problems/sort-the-people/

export function sortPeople(names: string[], heights: number[]): string[] {
    const n = names.length;
    const idx = Array.from({ length: n }, (_, i) => i);
    idx.sort((a, b) => heights[b] - heights[a]);
    return idx.map((i) => names[i]);
}
