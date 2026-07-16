// LeetCode 0320 - Generalized Abbreviation
export function generateAbbreviations(word: string): string[] {
    const result: string[] = [];
    function backtrack(index: number, path: string, count: number): void {
        if (index === word.length) {
            result.push(path + (count ? String(count) : ""));
            return;
        }
        backtrack(index + 1, path, count + 1);
        backtrack(index + 1, path + (count ? String(count) : "") + word[index], 0);
    }
    backtrack(0, "", 0);
    return result;
}
