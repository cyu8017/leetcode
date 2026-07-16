// LeetCode 0388 - Longest Absolute File Path
export function lengthLongestPath(input: string): number {
    const stack: number[] = [];
    let maxLength = 0;

    for (const line of input.split("\n")) {
        const depth = line.lastIndexOf("\t") + 1;
        const name = line.slice(depth);
        while (stack.length > depth) stack.pop();

        if (name.includes(".")) {
            const total = name.length + (stack.length ? stack[stack.length - 1] : 0);
            maxLength = Math.max(maxLength, total);
        } else {
            const prefix = stack.length ? stack[stack.length - 1] : 0;
            stack.push(prefix + name.length + 1);
        }
    }

    return maxLength;
}
