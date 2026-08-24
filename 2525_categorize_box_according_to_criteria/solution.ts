// LeetCode 2525 - Categorize Box According to Criteria
// https://leetcode.com/problems/categorize-box-according-to-criteria/

export function categorizeBox(length: number, width: number, height: number, mass: number): string {
    const bulky = length >= 10000 || width >= 10000 || height >= 10000 ||
        length * width * height >= 1000000000;
    const heavy = mass >= 100;
    if (bulky && heavy) return "Both";
    if (bulky) return "Bulky";
    if (heavy) return "Heavy";
    return "Neither";
}
