// LeetCode 2782 - Number of Unique Categories
// https://leetcode.com/problems/number-of-unique-categories/

export function numberOfCategories(n: number, categoryHandler: CategoryHandler): number {
    const parent = Array.from({length: n}, (_, i) => i);
    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (categoryHandler.haveSameCategory(i, j)) {
                const a = find(i), b = find(j);
                if (a !== b) parent[a] = b;
            }
        }
    }
    let ans = 0;
    for (let i = 0; i < n; i++) if (find(i) === i) ans++;
    return ans;
}
