// LeetCode 2891 - Method Chaining
// https://leetcode.com/problems/method-chaining/

export function findHeavyAnimals(animals: any[]): any[] {
    return animals
        .filter((r) => (Array.isArray(r) ? r[3] : r.weight) > 100)
        .sort((a, b) => (Array.isArray(b) ? b[3] : b.weight) - (Array.isArray(a) ? a[3] : a.weight))
        .map((r) => (Array.isArray(r) ? { name: r[0] } : { name: r.name }));
}
