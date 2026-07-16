// LeetCode 0316 - Remove Duplicate Letters
export function removeDuplicateLetters(s: string): string {
    const lastIndex: Record<string, number> = {};
    for (let index = 0; index < s.length; index += 1) lastIndex[s[index]] = index;
    const stack: string[] = [];
    const seen = new Set<string>();
    for (let index = 0; index < s.length; index += 1) {
        const char = s[index];
        if (seen.has(char)) continue;
        while (stack.length > 0 && stack[stack.length - 1] > char && lastIndex[stack[stack.length - 1]] > index) {
            seen.delete(stack.pop() as string);
        }
        stack.push(char);
        seen.add(char);
    }
    return stack.join("");
}
