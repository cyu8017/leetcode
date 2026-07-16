// LeetCode 0157 - Read N Characters Given Read4
// https://leetcode.com/problems/read-n-characters-given-read4/

export function read(file: string, n: number): number {
    let fileIndex = 0;

    const read4 = (buffer: string[]): number => {
        let count = 0;
        while (count < 4 && fileIndex < file.length) {
            buffer[count] = file[fileIndex];
            fileIndex += 1;
            count += 1;
        }
        return count;
    };

    let copied = 0;
    while (copied < n) {
        const count = read4([]);
        if (count === 0) break;
        copied += Math.min(count, n - copied);
    }

    return copied;
}