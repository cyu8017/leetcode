// LeetCode 3990 - Create Grid With Exactly K Paths II
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/

export function BitWidth(k: any): any {
        let w = 0;
        while (k != 0) { ++w; k >>= 1; }
        return w;
    
}export function createGrid(k: any): any {
        if (k <= 0) return new Array(0);
        let l = BitWidth(k);
        let m = 2 * l, n = l + 3;
        let result = new Array(m);
        for (let i = 0; i < m; i++) {
            let row = new Array(n).fill('');
            for (let j = 0; j < n; j++) row[j] = '#';
            result[i] = new String(row);
        }
        for (let i = 0; i < l; i++) {
            let r = 2 * i;
            let row0 = result[r].split('');
            let row1 = result[r + 1].split('');
            row0[i] = row0[i + 1] = row1[i] = row1[i + 1] = '.';
            if ((k & (1 << i)) != 0) {
                for (let c = i + 2; c < n; c++) row0[c] = '.';
            }
            result[r] = new String(row0);
            result[r + 1] = new String(row1);
        }
        for (let r = 0; r < m; r++) {
            let row = result[r].split('');
            row[n - 1] = '.';
            result[r] = new String(row);
        }
        return result;
    
}
