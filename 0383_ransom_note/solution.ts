// LeetCode 0383 - Ransom Note
export function canConstruct(ransomNote: string, magazine: string): boolean {
    const counts = new Map<string, number>();
    for (const char of magazine) {
        counts.set(char, (counts.get(char) || 0) + 1);
    }
    for (const char of ransomNote) {
        const remaining = counts.get(char) || 0;
        if (remaining === 0) return false;
        counts.set(char, remaining - 1);
    }
    return true;
}
