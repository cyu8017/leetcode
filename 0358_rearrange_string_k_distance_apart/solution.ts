export function rearrangeString(s: string, k: number): string {
    const counts = new Map<string, number>();
    for (const char of s) counts.set(char, (counts.get(char) ?? 0) + 1);

    let maxFreq = 0;
    let maxFreqChars = 0;
    for (const count of counts.values()) {
        if (count > maxFreq) {
            maxFreq = count;
            maxFreqChars = 1;
        } else if (count === maxFreq) maxFreqChars += 1;
    }

    if ((s.length - maxFreqChars) < (maxFreq - 1) * (k - 1)) return "";

    const heap = [...counts.entries()].map(([char, count]) => [-count, char] as [number, string]);
    heap.sort((a, b) => a[0] - b[0] || a[1].localeCompare(b[1]));
    const queue: Array<[number, string, number]> = [];
    const result: string[] = [];
    let index = 0;

    while (heap.length || queue.length) {
        while (queue.length && queue[0][2] <= index) {
            const [count, char] = queue.shift()!;
            heap.push([count, char]);
            heap.sort((a, b) => a[0] - b[0] || a[1].localeCompare(b[1]));
        }

        if (!heap.length) return "";

        const [count, char] = heap.shift()!;
        result.push(char);
        if (count + 1 < 0) queue.push([count + 1, char, index + k]);
        index += 1;
    }

    return result.join("");
}
