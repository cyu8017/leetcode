export function reverseVowels(s: string): string {
    const vowels = new Set("aeiouAEIOU");
    const chars = s.split("");
    let left = 0;
    let right = chars.length - 1;

    while (left < right) {
        while (left < right && !vowels.has(chars[left])) left += 1;
        while (left < right && !vowels.has(chars[right])) right -= 1;
        [chars[left], chars[right]] = [chars[right], chars[left]];
        left += 1;
        right -= 1;
    }

    return chars.join("");
}
