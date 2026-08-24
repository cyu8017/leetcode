// LeetCode 3963 - Create Grid With Exactly One Path
// https://leetcode.com/problems/create-grid-with-exactly-one-path/

export function createGrid(m: any, n: any): any {
        let g = new Array(m);
        for (let i = 0; i < m; i++) {
            let row = new Array(n).fill('');
            for (let j = 0; j < n; j++) row[j] = '#';
            if (i == 0) for (let j = 0; j < n; j++) row[j] = '.';
            row[n - 1] = '.';
            g[i] = new String(row);
        }
        return g;
    
}
