// LeetCode 0158 - Read N Characters Given read4 II - Call Multiple Times
// https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

export function read(file: string, queries: number[]): number[] {
    let fileIndex = 0;
    const buffer: string[] = [];
    let bufferIndex = 0;
    let bufferSize = 0;

    const read4 = (): number => {
        bufferSize = 0;
        bufferIndex = 0;
        while (bufferSize < 4 && fileIndex < file.length) {
            buffer[bufferSize] = file[fileIndex];
            fileIndex += 1;
            bufferSize += 1;
        }
        return bufferSize;
    };

    const readOnce = (n: number): number => {
        let copied = 0;
        while (copied < n) {
            if (bufferIndex === bufferSize && read4() === 0) break;
            while (copied < n && bufferIndex < bufferSize) {
                copied += 1;
                bufferIndex += 1;
            }
        }
        return copied;
    };

    return queries.map(readOnce);
}