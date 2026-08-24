// LeetCode 3955 - Valid Binary Strings With Cost Limit
// https://leetcode.com/problems/valid-binary-strings-with-cost-limit/
var generateValidStrings = function(n, k) {
        let ans = [];
        let path = "";
        dfs(0, 0, n, k, path, ans);
        return ans;
    
};
var dfs = function(i, tot, n, k, path, ans) {
        if (i >= n) {
            ans.push(path);
            return;
        }
        path+= ('0');
        dfs(i + 1, tot, n, k, path, ans);
        path.deleteCharAt(path.length - 1);
        if ((path.length == 0 || path[path.length - 1] == '0') && tot + i <= k) {
            path+= ('1');
            dfs(i + 1, tot + i, n, k, path, ans);
            path.deleteCharAt(path.length - 1);
        }
    
};
