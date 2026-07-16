export function maxSumSubmatrix(matrix: number[][], k: number): number {
    const rows = matrix.length;
    const cols = matrix[0]?.length ?? 0;
    let result = Number.NEGATIVE_INFINITY;

    const lowerBound = (arr: number[], target: number): number => {
        let left = 0;
        let right = arr.length;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (arr[mid] < target) left = mid + 1;
            else right = mid;
        }
        return left;
    };

    const insertSorted = (arr: number[], value: number): void => {
        arr.splice(lowerBound(arr, value), 0, value);
    };

    for (let top = 0; top < rows; top += 1) {
        const colSums = Array(cols).fill(0);
        for (let bottom = top; bottom < rows; bottom += 1) {
            const prefixSums = [0];
            let running = 0;
            for (let col = 0; col < cols; col += 1) {
                colSums[col] += matrix[bottom][col];
                running += colSums[col];
                const index = lowerBound(prefixSums, running - k);
                if (index < prefixSums.length) {
                    result = Math.max(result, running - prefixSums[index]);
                }
                insertSorted(prefixSums, running);
            }
        }
    }

    return result;
}
