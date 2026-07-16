// LeetCode 0407 - Trapping Rain Water II
export function trapRainWater(heightMap: number[][]): number {
    if (!heightMap.length || !heightMap[0].length) return 0;
    const rows = heightMap.length;
    const cols = heightMap[0].length;
    if (rows < 3 || cols < 3) return 0;

    const visited = Array.from({ length: rows }, () => Array(cols).fill(false));
    const heap: number[][] = [];

    const push = (height: number, row: number, col: number) => {
        heap.push([height, row, col]);
        let index = heap.length - 1;
        while (index > 0) {
            const parent = Math.floor((index - 1) / 2);
            if (heap[parent][0] <= heap[index][0]) break;
            [heap[parent], heap[index]] = [heap[index], heap[parent]];
            index = parent;
        }
    };

    const pop = (): number[] => {
        const top = heap[0];
        const last = heap.pop()!;
        if (!heap.length) return top;
        heap[0] = last;
        let index = 0;
        while (true) {
            let smallest = index;
            const left = index * 2 + 1;
            const right = index * 2 + 2;
            if (left < heap.length && heap[left][0] < heap[smallest][0]) smallest = left;
            if (right < heap.length && heap[right][0] < heap[smallest][0]) smallest = right;
            if (smallest === index) break;
            [heap[index], heap[smallest]] = [heap[smallest], heap[index]];
            index = smallest;
        }
        return top;
    };

    for (let row = 0; row < rows; row += 1) {
        for (let col = 0; col < cols; col += 1) {
            if (row === 0 || row === rows - 1 || col === 0 || col === cols - 1) {
                push(heightMap[row][col], row, col);
                visited[row][col] = true;
            }
        }
    }

    let trapped = 0;
    const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    while (heap.length) {
        const [height, row, col] = pop();
        for (const [dr, dc] of directions) {
            const nextRow = row + dr;
            const nextCol = col + dc;
            if (nextRow < 0 || nextRow >= rows || nextCol < 0 || nextCol >= cols || visited[nextRow][nextCol]) {
                continue;
            }
            visited[nextRow][nextCol] = true;
            const nextHeight = heightMap[nextRow][nextCol];
            trapped += Math.max(0, height - nextHeight);
            push(Math.max(height, nextHeight), nextRow, nextCol);
        }
    }
    return trapped;
}
