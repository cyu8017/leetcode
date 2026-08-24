===== 2001_number_of_pairs_of_interchangeable_rectangles =====
TITLE: 2001. Number of Pairs of Interchangeable Rectangles
SLUG: number-of-pairs-of-interchangeable-rectangles
CONFIG: {"class": "Solution", "method": "interchangeableRectangles", "paramOrder": ["rectangles"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2001 - Number of Pairs of Interchangeable Rectangles
// https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var interchangeableRectangles = function(rectangles) {
    const gcd = (a, b) => {
        while (b !== 0) { const t = a % b; a = b; b = t; }
        return a;
    };
    const freq = new Map();
    let ans = 0;
    for (const rect of rectangles) {
        const g = gcd(rect[0], rect[1]);
        const key = (rect[0] / g) + "/" + (rect[1] / g);
        const f = freq.get(key) || 0;
        ans += f;
        freq.set(key, f + 1);
    }
    return ans;
};


===== 2002_maximum_product_of_the_length_of_two_palindromic_subsequences =====
TITLE: 2002. Maximum Product of the Length of Two Palindromic Subsequences
SLUG: maximum-product-of-the-length-of-two-palindromic-subsequences
CONFIG: {"class": "Solution", "method": "maxProduct", "paramOrder": ["s"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2002 - Maximum Product of the Length of Two Palindromic Subsequences
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

/**
 * @param {string} s
 * @return {number}
 */
var maxProduct = function(s) {
    const palLen = (mask) => {
        let chars = "";
        for (let i = 0; i < s.length; i++)
            if ((mask & (1 << i)) !== 0) chars += s[i];
        for (let l = 0, r = chars.length - 1; l < r; l++, r--)
            if (chars[l] !== chars[r]) return 0;
        return chars.length;
    };
    const n = s.length;
    let best = 0;
    const total = 1 << n;
    for (let mask1 = 1; mask1 < total; mask1++) {
        const len1 = palLen(mask1);
        if (len1 === 0) continue;
        const remain = (total - 1) ^ mask1;
        for (let mask2 = remain; mask2 > 0; mask2 = (mask2 - 1) & remain) {
            const len2 = palLen(mask2);
            if (len2 > 0 && len1 * len2 > best) best = len1 * len2;
        }
    }
    return best;
};


===== 2003_smallest_missing_genetic_value_in_each_subtree =====
TITLE: 2003. Smallest Missing Genetic Value in Each Subtree
SLUG: smallest-missing-genetic-value-in-each-subtree
CONFIG: {"class": "Solution", "method": "smallestMissingValueSubtree", "paramOrder": ["parents", "nums"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2003 - Smallest Missing Genetic Value in Each Subtree
// https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

/**
 * @param {number[]} parents
 * @param {number[]} nums
 * @return {number[]}
 */
var smallestMissingValueSubtree = function(parents, nums) {
    const n = parents.length;
    const children = Array.from({length: n}, () => []);
    for (let i = 1; i < n; i++) children[parents[i]].push(i);
    const ans = new Array(n).fill(1);
    let one = -1;
    for (let i = 0; i < n; i++) if (nums[i] === 1) { one = i; break; }
    if (one < 0) return ans;
    const seen = new Set();
    const collect = (u) => {
        if (seen.has(nums[u])) return;
        seen.add(nums[u]);
        for (const v of children[u]) collect(v);
    };
    let miss = 1, node = one, prev = -1;
    while (node !== -1) {
        for (const v of children[node]) if (v !== prev) collect(v);
        seen.add(nums[node]);
        while (seen.has(miss)) miss++;
        ans[node] = miss;
        prev = node;
        node = parents[node];
    }
    return ans;
};


===== 2005_subtree_removal_game_with_fibonacci_tree =====
TITLE: 2005. Subtree Removal Game with Fibonacci Tree
SLUG: subtree-removal-game-with-fibonacci-tree
CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["n"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2005 - Subtree Removal Game with Fibonacci Tree
// https://leetcode.com/problems/subtree-removal-game-with-fibonacci-tree/

/**
 * @param {number} n
 * @return {boolean}
 */
var findGameWinner = function(n) {
    return n % 6 !== 1;
};


===== 2006_count_number_of_pairs_with_absolute_difference_k =====
TITLE: 2006. Count Number of Pairs With Absolute Difference K
SLUG: count-number-of-pairs-with-absolute-difference-k
CONFIG: {"class": "Solution", "method": "countKDifference", "paramOrder": ["nums", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2006 - Count Number of Pairs With Absolute Difference K
// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countKDifference = function(nums, k) {
    const freq = new Map();
    let ans = 0;
    for (const x of nums) {
        ans += freq.get(x - k) || 0;
        ans += freq.get(x + k) || 0;
        freq.set(x, (freq.get(x) || 0) + 1);
    }
    return ans;
};


===== 2007_find_original_array_from_doubled_array =====
TITLE: 2007. Find Original Array From Doubled Array
SLUG: find-original-array-from-doubled-array
CONFIG: {"class": "Solution", "method": "findOriginalArray", "paramOrder": ["changed"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2007 - Find Original Array From Doubled Array
// https://leetcode.com/problems/find-original-array-from-doubled-array/

/**
 * @param {number[]} changed
 * @return {number[]}
 */
var findOriginalArray = function(changed) {
    if (changed.length % 2 !== 0) return [];
    changed.sort((a, b) => a - b);
    const freq = new Map();
    for (const x of changed) freq.set(x, (freq.get(x) || 0) + 1);
    const ans = [];
    for (const x of changed) {
        if ((freq.get(x) || 0) === 0) continue;
        freq.set(x, freq.get(x) - 1);
        if ((freq.get(2 * x) || 0) === 0) return [];
        freq.set(2 * x, freq.get(2 * x) - 1);
        ans.push(x);
    }
    return ans;
};


===== 2008_maximum_earnings_from_taxi =====
TITLE: 2008. Maximum Earnings From Taxi
SLUG: maximum-earnings-from-taxi
CONFIG: {"class": "Solution", "method": "maxTaxiEarnings", "paramOrder": ["n", "rides"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2008 - Maximum Earnings From Taxi
// https://leetcode.com/problems/maximum-earnings-from-taxi/

/**
 * @param {number} n
 * @param {number[][]} rides
 * @return {number}
 */
var maxTaxiEarnings = function(n, rides) {
    rides.sort((a, b) => a[1] - b[1]);
    const m = rides.length;
    const ends = rides.map(r => r[1]);
    const dp = new Array(m + 1).fill(0);
    for (let i = 0; i < m; i++) {
        const [start, end, tip] = rides[i];
        const earn = end - start + tip;
        let lo = 0, hi = m;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (ends[mid] <= start) lo = mid + 1;
            else hi = mid;
        }
        dp[i + 1] = Math.max(dp[i], earn + dp[lo]);
    }
    return dp[m];
};


===== 2009_minimum_number_of_operations_to_make_array_continuous =====
TITLE: 2009. Minimum Number of Operations to Make Array Continuous
SLUG: minimum-number-of-operations-to-make-array-continuous
CONFIG: {"class": "Solution", "method": "minOperations", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2009 - Minimum Number of Operations to Make Array Continuous
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    const n = nums.length;
    const uniq = [...new Set(nums)].sort((a, b) => a - b);
    let ans = n, j = 0;
    for (let i = 0; i < uniq.length; i++) {
        while (j < uniq.length && uniq[j] - uniq[i] + 1 <= n) j++;
        ans = Math.min(ans, n - (j - i));
    }
    return ans;
};


===== 2011_final_value_of_variable_after_performing_operations =====
TITLE: 2011. Final Value of Variable After Performing Operations
SLUG: final-value-of-variable-after-performing-operations
CONFIG: {"class": "--X", "description": "Update method name and add cases to cases.json when implementing the solution.", "kind": "design", "runnable": true}
---JS---
// LeetCode 2011 - Final Value of Variable After Performing Operations
// https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let x = 0;
    for (const op of operations) {
        if (op[1] === '+') x++;
        else x--;
    }
    return x;
};


===== 2012_sum_of_beauty_in_the_array =====
TITLE: 2012. Sum of Beauty in the Array
SLUG: sum-of-beauty-in-the-array
CONFIG: {"class": "Solution", "method": "sumOfBeauties", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2012 - Sum of Beauty in the Array
// https://leetcode.com/problems/sum-of-beauty-in-the-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfBeauties = function(nums) {
    const n = nums.length;
    const prefixMax = new Array(n), suffixMin = new Array(n);
    prefixMax[0] = nums[0];
    for (let i = 1; i < n; i++) prefixMax[i] = Math.max(prefixMax[i - 1], nums[i]);
    suffixMin[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) suffixMin[i] = Math.min(suffixMin[i + 1], nums[i]);
    let ans = 0;
    for (let i = 1; i < n - 1; i++) {
        if (prefixMax[i - 1] < nums[i] && nums[i] < suffixMin[i + 1]) ans += 2;
        else if (nums[i - 1] < nums[i] && nums[i] < nums[i + 1]) ans++;
    }
    return ans;
};


===== 2013_detect_squares =====
TITLE: 2013. Detect Squares
SLUG: detect-squares
CONFIG: {"class": "DetectSquares", "description": "Update method name and add cases to cases.json when implementing the solution.", "kind": "design", "runnable": true}
---JS---
// LeetCode 2013 - Detect Squares
// https://leetcode.com/problems/detect-squares/

class DetectSquares {
    constructor() {
        this.cnt = new Map();
    }

    key(x, y) {
        return x + "," + y;
    }

    /**
     * @param {number[]} point
     * @return {void}
     */
    add(point) {
        const k = this.key(point[0], point[1]);
        this.cnt.set(k, (this.cnt.get(k) || 0) + 1);
    }

    /**
     * @param {number[]} point
     * @return {number}
     */
    count(point) {
        const x = point[0], y = point[1];
        let ans = 0;
        for (const [k, c] of this.cnt) {
            const [px, py] = k.split(",").map(Number);
            if (px === x || py === y) continue;
            if (Math.abs(px - x) !== Math.abs(py - y)) continue;
            const c1 = this.cnt.get(this.key(px, y)) || 0;
            const c2 = this.cnt.get(this.key(x, py)) || 0;
            ans += c * c1 * c2;
        }
        return ans;
    }
}



===== 2014_longest_subsequence_repeated_k_times =====
TITLE: 2014. Longest Subsequence Repeated k Times
SLUG: longest-subsequence-repeated-k-times
CONFIG: {"class": "Solution", "method": "longestSubsequenceRepeatedK", "paramOrder": ["s", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2014 - Longest Subsequence Repeated K Times
// https://leetcode.com/problems/longest-subsequence-repeated-k-times/

/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var longestSubsequenceRepeatedK = function(s, k) {
    const freq = new Array(26).fill(0);
    for (const c of s) freq[c.charCodeAt(0) - 97]++;
    let chars = "";
    for (let c = 25; c >= 0; c--) if (freq[c] >= k) chars += String.fromCharCode(97 + c);
    const isSubseq = (t) => {
        let need = 0, times = 0;
        for (let i = 0; i < s.length; i++) {
            if (s[i] === t[need]) {
                need++;
                if (need === t.length) {
                    times++;
                    if (times === k) return true;
                    need = 0;
                }
            }
        }
        return false;
    };
    let best = "";
    const q = [""];
    while (q.length) {
        const cur = q.shift();
        for (let i = 0; i < chars.length; i++) {
            const nxt = cur + chars[i];
            if (isSubseq(nxt)) {
                if (nxt.length > best.length || (nxt.length === best.length && nxt > best))
                    best = nxt;
                q.push(nxt);
            }
        }
    }
    return best;
};


===== 2015_average_height_of_buildings_in_each_segment =====
TITLE: 2015. Average Height of Buildings in Each Segment
SLUG: average-height-of-buildings-in-each-segment
CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["buildings"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2015 - Average Height of Buildings in Each Segment
// https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

/**
 * @param {number[][]} buildings
 * @return {number[][]}
 */
var averageHeightOfBuildings = function(buildings) {
    const events = [];
    for (const b of buildings) {
        events.push([b[0], 1, b[2]]);
        events.push([b[1], -1, b[2]]);
    }
    events.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]);
    const ans = [];
    let count = 0, sum = 0, prev = events[0][0];
    for (const e of events) {
        if (e[0] !== prev && count > 0) {
            const avg = Math.floor(sum / count);
            if (ans.length && ans[ans.length - 1][1] === prev && ans[ans.length - 1][2] === avg)
                ans[ans.length - 1][1] = e[0];
            else ans.push([prev, e[0], avg]);
        }
        count += e[1];
        sum += e[1] * e[2];
        prev = e[0];
    }
    return ans;
};


===== 2016_maximum_difference_between_increasing_elements =====
TITLE: 2016. Maximum Difference Between Increasing Elements
SLUG: maximum-difference-between-increasing-elements
CONFIG: {"class": "Solution", "method": "maximumDifference", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2016 - Maximum Difference Between Increasing Elements
// https://leetcode.com/problems/maximum-difference-between-increasing-elements/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumDifference = function(nums) {
    let ans = -1, mn = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > mn) ans = Math.max(ans, nums[i] - mn);
        else mn = nums[i];
    }
    return ans;
};


===== 2017_grid_game =====
TITLE: 2017. Grid Game
SLUG: grid-game
CONFIG: {"class": "Solution", "method": "gridGame", "paramOrder": ["grid"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2017 - Grid Game
// https://leetcode.com/problems/grid-game/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var gridGame = function(grid) {
    const n = grid[0].length;
    let top = 0, bottom = 0, ans = Number.MAX_SAFE_INTEGER;
    for (const v of grid[0]) top += v;
    for (let i = 0; i < n; i++) {
        top -= grid[0][i];
        ans = Math.min(ans, Math.max(top, bottom));
        bottom += grid[1][i];
    }
    return ans;
};


===== 2018_check_if_word_can_be_placed_in_crossword =====
TITLE: 2018. Check if Word Can Be Placed In Crossword
SLUG: check-if-word-can-be-placed-in-crossword
CONFIG: {"class": "Solution", "method": "placeWordInCrossword", "paramOrder": ["board", "word"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2018 - Check if Word Can Be Placed In Crossword
// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var placeWordInCrossword = function(board, word) {
    const m = board.length, n = board[0].length, L = word.length;
    const match = (cells) => {
        if (cells.length !== L) return false;
        let ok1 = true, ok2 = true;
        for (let i = 0; i < L; i++) {
            if (cells[i] !== ' ' && cells[i] !== word[i]) ok1 = false;
            if (cells[i] !== ' ' && cells[i] !== word[L - 1 - i]) ok2 = false;
        }
        return ok1 || ok2;
    };
    for (let r = 0; r < m; r++) {
        let c = 0;
        while (c < n) {
            while (c < n && board[r][c] === '#') c++;
            const start = c;
            while (c < n && board[r][c] !== '#') c++;
            if (c - start === L) {
                let sb = "";
                for (let i = start; i < c; i++) sb += board[r][i];
                if (match(sb)) return true;
            }
        }
    }
    for (let c = 0; c < n; c++) {
        let r = 0;
        while (r < m) {
            while (r < m && board[r][c] === '#') r++;
            const start = r;
            while (r < m && board[r][c] !== '#') r++;
            if (r - start === L) {
                let sb = "";
                for (let i = 0; i < L; i++) sb += board[start + i][c];
                if (match(sb)) return true;
            }
        }
    }
    return false;
};


===== 2019_the_score_of_students_solving_math_expression =====
TITLE: 2019. The Score of Students Solving Math Expression
SLUG: the-score-of-students-solving-math-expression
CONFIG: {"class": "Solution", "method": "scoreOfStudents", "paramOrder": ["s", "answers"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2019 - The Score of Students Solving Math Expression
// https://leetcode.com/problems/the-score-of-students-solving-math-expression/

/**
 * @param {string} s
 * @param {number[]} answers
 * @return {number}
 */
var scoreOfStudents = function(s, answers) {
    const evalCorrect = (str) => {
        const nums = [], ops = [];
        for (const c of str) {
            if (c >= '0' && c <= '9') nums.push(c.charCodeAt(0) - 48);
            else ops.push(c);
        }
        const newNums = [nums[0]];
        const newOps = [];
        for (let j = 0; j < ops.length; j++) {
            if (ops[j] === '*') newNums[newNums.length - 1] *= nums[j + 1];
            else { newOps.push(ops[j]); newNums.push(nums[j + 1]); }
        }
        let res = newNums[0];
        for (let j = 0; j < newOps.length; j++) res += newNums[j + 1];
        return res;
    };
    const n = s.length;
    const correct = evalCorrect(s);
    const dp = Array.from({length: n}, () => new Array(n).fill(null));
    const dfs = (l, r) => {
        if (dp[l][r] !== null) return dp[l][r];
        const res = new Set();
        if (l === r) { res.add(s.charCodeAt(l) - 48); dp[l][r] = res; return res; }
        for (let i = l + 1; i < r; i += 2) {
            for (const a of dfs(l, i - 1))
                for (const b of dfs(i + 1, r)) {
                    const v = s[i] === '+' ? a + b : a * b;
                    if (v <= 1000) res.add(v);
                }
        }
        dp[l][r] = res;
        return res;
    };
    const possible = dfs(0, n - 1);
    let ans = 0;
    for (const a of answers) {
        if (a === correct) ans += 5;
        else if (possible.has(a)) ans += 2;
    }
    return ans;
};


===== 2021_brightest_position_on_street =====
TITLE: 2021. Brightest Position on Street
SLUG: brightest-position-on-street
CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["lights"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2021 - Brightest Position on Street
// https://leetcode.com/problems/brightest-position-on-street/

/**
 * @param {number[][]} lights
 * @return {number}
 */
var brightestPosition = function(lights) {
    const events = [];
    for (const light of lights) {
        const pos = light[0], r = light[1];
        events.push([pos - r, 1]);
        events.push([pos + r + 1, -1]);
    }
    events.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : b[1] - a[1]);
    let best = 0, cur = 0, ans = 0;
    for (const e of events) {
        cur += e[1];
        if (cur > best) { best = cur; ans = e[0]; }
    }
    return ans;
};


===== 2022_convert_1d_array_into_2d_array =====
TITLE: 2022. Convert 1D Array Into 2D Array
SLUG: convert-1d-array-into-2d-array
CONFIG: {"class": "Solution", "method": "construct2DArray", "paramOrder": ["original", "m", "n"], "types": {"return": "integer[][]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2022 - Convert 1D Array Into 2D Array
// https://leetcode.com/problems/convert-1d-array-into-2d-array/

/**
 * @param {number[]} original
 * @param {number} m
 * @param {number} n
 * @return {number[][]}
 */
var construct2DArray = function(original, m, n) {
    if (original.length !== m * n) return [];
    const ans = Array.from({length: m}, () => new Array(n));
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++) ans[i][j] = original[i * n + j];
    return ans;
};


===== 2023_number_of_pairs_of_strings_with_concatenation_equal_to_target =====
TITLE: 2023. Number of Pairs of Strings With Concatenation Equal to Target
SLUG: number-of-pairs-of-strings-with-concatenation-equal-to-target
CONFIG: {"class": "Solution", "method": "numOfPairs", "paramOrder": ["nums", "target"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2023 - Number of Pairs of Strings With Concatenation Equal to Target
// https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

/**
 * @param {string[]} nums
 * @param {string} target
 * @return {number}
 */
var numOfPairs = function(nums, target) {
    let ans = 0;
    for (let i = 0; i < nums.length; i++)
        for (let j = 0; j < nums.length; j++)
            if (i !== j && nums[i] + nums[j] === target) ans++;
    return ans;
};


===== 2024_maximize_the_confusion_of_an_exam =====
TITLE: 2024. Maximize the Confusion of an Exam
SLUG: maximize-the-confusion-of-an-exam
CONFIG: {"class": "Solution", "method": "maxConsecutiveAnswers", "paramOrder": ["answerKey", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2024 - Maximize the Confusion of an Exam
// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

/**
 * @param {string} answerKey
 * @param {number} k
 * @return {number}
 */
var maxConsecutiveAnswers = function(answerKey, k) {
    const maxWith = (ch) => {
        let left = 0, bad = 0, best = 0;
        for (let right = 0; right < answerKey.length; right++) {
            if (answerKey[right] !== ch) bad++;
            while (bad > k) {
                if (answerKey[left] !== ch) bad--;
                left++;
            }
            best = Math.max(best, right - left + 1);
        }
        return best;
    };
    return Math.max(maxWith('T'), maxWith('F'));
};


===== 2025_maximum_number_of_ways_to_partition_an_array =====
TITLE: 2025. Maximum Number of Ways to Partition an Array
SLUG: maximum-number-of-ways-to-partition-an-array
CONFIG: {"class": "Solution", "method": "waysToPartition", "paramOrder": ["nums", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2025 - Maximum Number of Ways to Partition an Array
// https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var waysToPartition = function(nums, k) {
    const n = nums.length;
    const pref = new Array(n);
    pref[0] = nums[0];
    for (let i = 1; i < n; i++) pref[i] = pref[i - 1] + nums[i];
    const total = pref[n - 1];
    const right = new Map(), left = new Map();
    for (let i = 0; i < n - 1; i++) right.set(pref[i], (right.get(pref[i]) || 0) + 1);
    let ans = 0;
    if (total % 2 === 0) ans = right.get(total / 2) || 0;
    for (let i = 0; i < n; i++) {
        const diff = k - nums[i];
        const newTotal = total + diff;
        let cur = 0;
        if (newTotal % 2 === 0) {
            const half = newTotal / 2;
            cur = (left.get(half) || 0) + (right.get(half - diff) || 0);
        }
        ans = Math.max(ans, cur);
        if (i < n - 1) {
            left.set(pref[i], (left.get(pref[i]) || 0) + 1);
            right.set(pref[i], right.get(pref[i]) - 1);
        }
    }
    return ans;
};


===== 2027_minimum_moves_to_convert_string =====
TITLE: 2027. Minimum Moves to Convert String
SLUG: minimum-moves-to-convert-string
CONFIG: {"class": "Solution", "method": "minimumMoves", "paramOrder": ["s"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2027 - Minimum Moves to Convert String
// https://leetcode.com/problems/minimum-moves-to-convert-string/

/**
 * @param {string} s
 * @return {number}
 */
var minimumMoves = function(s) {
    let ans = 0;
    for (let i = 0; i < s.length; ) {
        if (s[i] === 'X') { ans++; i += 3; }
        else i++;
    }
    return ans;
};


===== 2028_find_missing_observations =====
TITLE: 2028. Find Missing Observations
SLUG: find-missing-observations
CONFIG: {"class": "Solution", "method": "missingRolls", "paramOrder": ["rolls", "mean", "n"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2028 - Find Missing Observations
// https://leetcode.com/problems/find-missing-observations/

/**
 * @param {number[]} rolls
 * @param {number} mean
 * @param {number} n
 * @return {number[]}
 */
var missingRolls = function(rolls, mean, n) {
    let sum = 0;
    for (const r of rolls) sum += r;
    const remain = mean * (rolls.length + n) - sum;
    if (remain < n || remain > 6 * n) return [];
    const ans = new Array(n);
    const baseVal = Math.floor(remain / n), extra = remain % n;
    for (let i = 0; i < n; i++) ans[i] = baseVal + (i < extra ? 1 : 0);
    return ans;
};


===== 2029_stone_game_ix =====
TITLE: 2029. Stone Game IX
SLUG: stone-game-ix
CONFIG: {"class": "Solution", "method": "stoneGameIX", "paramOrder": ["stones"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2029 - Stone Game IX
// https://leetcode.com/problems/stone-game-ix/

/**
 * @param {number[]} stones
 * @return {boolean}
 */
var stoneGameIX = function(stones) {
    const cnt = [0, 0, 0];
    for (const s of stones) cnt[s % 3]++;
    if (cnt[0] % 2 === 0) return cnt[1] > 0 && cnt[2] > 0;
    return Math.abs(cnt[1] - cnt[2]) > 2;
};


===== 2030_smallest_k_length_subsequence_with_occurrences_of_a_letter =====
TITLE: 2030. Smallest K-Length Subsequence With Occurrences of a Letter
SLUG: smallest-k-length-subsequence-with-occurrences-of-a-letter
CONFIG: {"class": "Solution", "method": "smallestSubsequence", "paramOrder": ["s", "k", "letter", "repetition"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2030 - Smallest K-Length Subsequence With Occurrences of a Letter
// https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

/**
 * @param {string} s
 * @param {number} k
 * @param {character} letter
 * @param {number} repetition
 * @return {string}
 */
var smallestSubsequence = function(s, k, letter, repetition) {
    const n = s.length;
    let remainLetter = 0;
    for (const c of s) if (c === letter) remainLetter++;
    let stack = "";
    let inStackLetter = 0;
    for (let i = 0; i < n; i++) {
        const ch = s[i];
        while (stack.length > 0 && ch < stack[stack.length - 1] && stack.length + n - i > k) {
            const top = stack[stack.length - 1];
            if (top === letter) {
                if (inStackLetter + remainLetter - 1 < repetition) break;
                inStackLetter--;
            }
            stack = stack.slice(0, -1);
        }
        if (stack.length < k) {
            if (ch === letter) { stack += ch; inStackLetter++; }
            else if (k - stack.length > repetition - inStackLetter) stack += ch;
        }
        if (ch === letter) remainLetter--;
    }
    return stack;
};


===== 2031_count_subarrays_with_more_ones_than_zeros =====
TITLE: 2031. Count Subarrays With More Ones Than Zeros
SLUG: count-subarrays-with-more-ones-than-zeros
CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2031 - Count Subarrays With More Ones Than Zeros
// https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

/**
 * @param {number[]} nums
 * @return {number}
 */
var subarraysWithMoreZerosThanOnes = function(nums) {
    const MOD = 1000000007;
    class Fenwick {
        constructor(n) { this.bit = new Array(n + 2).fill(0); }
        add(i, v) { for (; i < this.bit.length; i += i & -i) this.bit[i] += v; }
        sum(i) { let s = 0; for (; i > 0; i -= i & -i) s += this.bit[i]; return s; }
    }
    const n = nums.length, offset = n + 1;
    const fw = new Fenwick(2 * n + 5);
    let pref = 0, ans = 0;
    fw.add(offset, 1);
    for (const x of nums) {
        pref += (x === 1) ? 1 : -1;
        const idx = pref + offset;
        ans = (ans + fw.sum(idx - 1)) % MOD;
        fw.add(idx, 1);
    }
    return ans;
};


===== 2032_two_out_of_three =====
TITLE: 2032. Two Out of Three
SLUG: two-out-of-three
CONFIG: {"class": "Solution", "method": "twoOutOfThree", "paramOrder": ["nums1", "nums2", "nums3"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2032 - Two Out of Three
// https://leetcode.com/problems/two-out-of-three/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @return {number[]}
 */
var twoOutOfThree = function(nums1, nums2, nums3) {
    const s0 = new Set(nums1), s1 = new Set(nums2), s2 = new Set(nums3);
    const ans = [];
    for (let v = 1; v <= 100; v++) {
        const c = (s0.has(v) ? 1 : 0) + (s1.has(v) ? 1 : 0) + (s2.has(v) ? 1 : 0);
        if (c >= 2) ans.push(v);
    }
    return ans;
};


===== 2033_minimum_operations_to_make_a_uni_value_grid =====
TITLE: 2033. Minimum Operations to Make a Uni-Value Grid
SLUG: minimum-operations-to-make-a-uni-value-grid
CONFIG: {"class": "Solution", "method": "minOperations", "paramOrder": ["grid", "x"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2033 - Minimum Operations to Make a Uni-Value Grid
// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

/**
 * @param {number[][]} grid
 * @param {number} x
 * @return {number}
 */
var minOperations = function(grid, x) {
    const vals = [];
    const bas = grid[0][0] % x;
    for (const row of grid) for (const v of row) {
        if (v % x !== bas) return -1;
        vals.push(v);
    }
    vals.sort((a, b) => a - b);
    const median = vals[Math.floor(vals.length / 2)];
    let ans = 0;
    for (const v of vals) ans += Math.abs(v - median) / x;
    return ans;
};


===== 2034_stock_price_fluctuation =====
TITLE: 2034. Stock Price Fluctuation
SLUG: stock-price-fluctuation
CONFIG: {"class": "StockPrice", "description": "Update method name and add cases to cases.json when implementing the solution.", "kind": "design", "runnable": true}
---JS---
// LeetCode 2034 - Stock Price Fluctuation
// https://leetcode.com/problems/stock-price-fluctuation/

class StockPrice {
    constructor() {
        this.latestTs = 0;
        this.priceAt = new Map();
        this.maxHeap = [];
        this.minHeap = [];
    }

    _pushMax(item) {
        this.maxHeap.push(item);
        this.maxHeap.sort((a, b) => b[0] - a[0]);
    }
    _pushMin(item) {
        this.minHeap.push(item);
        this.minHeap.sort((a, b) => a[0] - b[0]);
    }

    /**
     * @param {number} timestamp
     * @param {number} price
     * @return {void}
     */
    update(timestamp, price) {
        this.priceAt.set(timestamp, price);
        if (timestamp >= this.latestTs) this.latestTs = timestamp;
        this._pushMax([price, timestamp]);
        this._pushMin([price, timestamp]);
    }

    /**
     * @return {number}
     */
    current() {
        return this.priceAt.get(this.latestTs);
    }

    /**
     * @return {number}
     */
    maximum() {
        while (true) {
            const top = this.maxHeap[0];
            if (this.priceAt.get(top[1]) === top[0]) return top[0];
            this.maxHeap.shift();
        }
    }

    /**
     * @return {number}
     */
    minimum() {
        while (true) {
            const top = this.minHeap[0];
            if (this.priceAt.get(top[1]) === top[0]) return top[0];
            this.minHeap.shift();
        }
    }
}


===== 2035_partition_array_into_two_arrays_to_minimize_sum_difference =====
TITLE: 2035. Partition Array Into Two Arrays to Minimize Sum Difference
SLUG: partition-array-into-two-arrays-to-minimize-sum-difference
CONFIG: {"class": "Solution", "method": "minimumDifference", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2035 - Partition Array Into Two Arrays to Minimize Sum Difference
// https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDifference = function(nums) {
    const n = nums.length / 2;
    let total = 0;
    for (const v of nums) total += v;
    const left = nums.slice(0, n);
    const right = nums.slice(n);
    const sumsByCount = (arr) => {
        const m = arr.length;
        const res = Array.from({length: m + 1}, () => []);
        for (let mask = 0; mask < (1 << m); mask++) {
            let sum = 0, c = 0;
            for (let i = 0; i < m; i++) if ((mask & (1 << i)) !== 0) { sum += arr[i]; c++; }
            res[c].push(sum);
        }
        for (const v of res) v.sort((a, b) => a - b);
        return res;
    };
    const L = sumsByCount(left);
    const R = sumsByCount(right);
    let ans = Number.MAX_SAFE_INTEGER;
    for (let k = 0; k <= n; k++) {
        for (const s1 of L[k]) {
            const need = Math.floor(total / 2) - s1;
            const arr = R[n - k];
            let lo = 0, hi = arr.length;
            while (lo < hi) {
                const mid = (lo + hi) >> 1;
                if (arr[mid] < need) lo = mid + 1;
                else hi = mid;
            }
            for (const j of [lo - 1, lo]) {
                if (j >= 0 && j < arr.length) {
                    const s2 = arr[j];
                    ans = Math.min(ans, Math.abs(total - 2 * (s1 + s2)));
                }
            }
        }
    }
    return ans;
};


===== 2036_maximum_alternating_subarray_sum =====
TITLE: 2036. Maximum Alternating Subarray Sum
SLUG: maximum-alternating-subarray-sum
CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2036 - Maximum Alternating Subarray Sum
// https://leetcode.com/problems/maximum-alternating-subarray-sum/

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumAlternatingSubarraySum = function(nums) {
    let ans = Number.MIN_SAFE_INTEGER, even = 0, odd = 0;
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i];
        if (i % 2 === 0) even += x;
        else even = Math.max(0, even - x);
        ans = Math.max(ans, even);
    }
    odd = 0;
    for (let i = 1; i < nums.length; i++) {
        const x = nums[i];
        if (i % 2 === 1) odd += x;
        else odd = Math.max(0, odd - x);
        ans = Math.max(ans, odd);
    }
    return ans;
};


===== 2037_minimum_number_of_moves_to_seat_everyone =====
TITLE: 2037. Minimum Number of Moves to Seat Everyone
SLUG: minimum-number-of-moves-to-seat-everyone
CONFIG: {"class": "Solution", "method": "minMovesToSeat", "paramOrder": ["seats", "students"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2037 - Minimum Number of Moves to Seat Everyone
// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

/**
 * @param {number[]} seats
 * @param {number[]} students
 * @return {number}
 */
var minMovesToSeat = function(seats, students) {
    seats.sort((a, b) => a - b);
    students.sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i < seats.length; i++) ans += Math.abs(seats[i] - students[i]);
    return ans;
};


===== 2038_remove_colored_pieces_if_both_neighbors_are_the_same_color =====
TITLE: 2038. Remove Colored Pieces if Both Neighbors are the Same Color
SLUG: remove-colored-pieces-if-both-neighbors-are-the-same-color
CONFIG: {"class": "Solution", "method": "winnerOfGame", "paramOrder": ["colors"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2038 - Remove Colored Pieces if Both Neighbors are the Same Color
// https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

/**
 * @param {string} colors
 * @return {boolean}
 */
var winnerOfGame = function(colors) {
    let a = 0, b = 0;
    for (let i = 1; i + 1 < colors.length; i++) {
        if (colors[i - 1] === colors[i] && colors[i] === colors[i + 1]) {
            if (colors[i] === 'A') a++;
            else b++;
        }
    }
    return a > b;
};


===== 2039_the_time_when_the_network_becomes_idle =====
TITLE: 2039. The Time When the Network Becomes Idle
SLUG: the-time-when-the-network-becomes-idle
CONFIG: {"class": "Solution", "method": "networkBecomesIdle", "paramOrder": ["edges", "patience"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2039 - The Time When the Network Becomes Idle
// https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

/**
 * @param {number[][]} edges
 * @param {number[]} patience
 * @return {number}
 */
var networkBecomesIdle = function(edges, patience) {
    const n = patience.length;
    const g = Array.from({length: n}, () => []);
    for (const e of edges) { g[e[0]].push(e[1]); g[e[1]].push(e[0]); }
    const dist = new Array(n).fill(-1);
    const q = [0];
    dist[0] = 0;
    while (q.length) {
        const u = q.shift();
        for (const v of g[u]) if (dist[v] === -1) { dist[v] = dist[u] + 1; q.push(v); }
    }
    let ans = 0;
    for (let i = 1; i < n; i++) {
        const round = dist[i] * 2;
        const lastSend = Math.floor((round - 1) / patience[i]) * patience[i];
        ans = Math.max(ans, lastSend + round);
    }
    return ans + 1;
};


===== 2040_kth_smallest_product_of_two_sorted_arrays =====
TITLE: 2040. Kth Smallest Product of Two Sorted Arrays
SLUG: kth-smallest-product-of-two-sorted-arrays
CONFIG: {"class": "Solution", "method": "kthSmallestProduct", "paramOrder": ["nums1", "nums2", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2040 - Kth Smallest Product of Two Sorted Arrays
// https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
var kthSmallestProduct = function(nums1, nums2, k) {
    const countLE = (x) => {
        let cnt = 0;
        for (const a of nums1) {
            if (a > 0) {
                let lo = 0, hi = nums2.length;
                while (lo < hi) {
                    const mid = (lo + hi) >> 1;
                    if (a * nums2[mid] <= x) lo = mid + 1;
                    else hi = mid;
                }
                cnt += lo;
            } else if (a < 0) {
                let lo = 0, hi = nums2.length;
                while (lo < hi) {
                    const mid = (lo + hi) >> 1;
                    if (a * nums2[mid] <= x) hi = mid;
                    else lo = mid + 1;
                }
                cnt += nums2.length - lo;
            } else if (x >= 0) cnt += nums2.length;
        }
        return cnt;
    };
    let lo = -10000000000, hi = 10000000000;
    while (lo < hi) {
        const mid = lo + Math.floor((hi - lo) / 2);
        if (countLE(mid) >= k) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};


===== 2042_check_if_numbers_are_ascending_in_a_sentence =====
TITLE: 2042. Check if Numbers Are Ascending in a Sentence
SLUG: check-if-numbers-are-ascending-in-a-sentence
CONFIG: {"class": "Solution", "method": "areNumbersAscending", "paramOrder": ["s"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2042 - Check if Numbers Are Ascending in a Sentence
// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

/**
 * @param {string} s
 * @return {boolean}
 */
var areNumbersAscending = function(s) {
    let prev = -1;
    for (const tok of s.split(" ")) {
        if (!tok) continue;
        if (tok[0] >= '0' && tok[0] <= '9') {
            const v = parseInt(tok, 10);
            if (v <= prev) return false;
            prev = v;
        }
    }
    return true;
};


===== 2043_simple_bank_system =====
TITLE: 2043. Simple Bank System
SLUG: simple-bank-system
CONFIG: {"class": "Bank", "description": "Update method name and add cases to cases.json when implementing the solution.", "kind": "design", "runnable": true}
---JS---
// LeetCode 2043 - Simple Bank System
// https://leetcode.com/problems/simple-bank-system/

class Bank {
    /**
     * @param {number[]} balance
     */
    constructor(balance) {
        this.bal = balance.slice();
    }

    valid(account) {
        return account >= 1 && account <= this.bal.length;
    }

    /**
     * @param {number} account1
     * @param {number} account2
     * @param {number} money
     * @return {boolean}
     */
    transfer(account1, account2, money) {
        if (!this.valid(account1) || !this.valid(account2) || this.bal[account1 - 1] < money) return false;
        this.bal[account1 - 1] -= money;
        this.bal[account2 - 1] += money;
        return true;
    }

    /**
     * @param {number} account
     * @param {number} money
     * @return {boolean}
     */
    deposit(account, money) {
        if (!this.valid(account)) return false;
        this.bal[account - 1] += money;
        return true;
    }

    /**
     * @param {number} account
     * @param {number} money
     * @return {boolean}
     */
    withdraw(account, money) {
        if (!this.valid(account) || this.bal[account - 1] < money) return false;
        this.bal[account - 1] -= money;
        return true;
    }
}


===== 2044_count_number_of_maximum_bitwise_or_subsets =====
TITLE: 2044. Count Number of Maximum Bitwise-OR Subsets
SLUG: count-number-of-maximum-bitwise-or-subsets
CONFIG: {"class": "Solution", "method": "countMaxOrSubsets", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets
// https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countMaxOrSubsets = function(nums) {
    let maxOr = 0, ans = 0;
    for (const x of nums) maxOr |= x;
    const dfs = (i, cur) => {
        if (i === nums.length) { if (cur === maxOr) ans++; return; }
        dfs(i + 1, cur);
        dfs(i + 1, cur | nums[i]);
    };
    dfs(0, 0);
    return ans;
};


===== 2045_second_minimum_time_to_reach_destination =====
TITLE: 2045. Second Minimum Time to Reach Destination
SLUG: second-minimum-time-to-reach-destination
CONFIG: {"class": "Solution", "method": "secondMinimum", "paramOrder": ["n", "edges", "time", "change"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2045 - Second Minimum Time to Reach Destination
// https://leetcode.com/problems/second-minimum-time-to-reach-destination/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} time
 * @param {number} change
 * @return {number}
 */
var secondMinimum = function(n, edges, time, change) {
    const g = Array.from({length: n + 1}, () => []);
    for (const e of edges) { g[e[0]].push(e[1]); g[e[1]].push(e[0]); }
    const dist1 = new Array(n + 1).fill(-1), dist2 = new Array(n + 1).fill(-1);
    const q = [[1, 0]];
    dist1[1] = 0;
    while (q.length) {
        const [u, d] = q.shift();
        for (const v of g[u]) {
            const nd = d + 1;
            if (dist1[v] === -1) { dist1[v] = nd; q.push([v, nd]); }
            else if (dist2[v] === -1 && nd > dist1[v]) { dist2[v] = nd; q.push([v, nd]); }
        }
    }
    const steps = dist2[n];
    let ans = 0;
    for (let i = 0; i < steps; i++) {
        if (Math.floor(ans / change) % 2 === 1) ans += change - ans % change;
        ans += time;
    }
    return ans;
};


===== 2046_sort_linked_list_already_sorted_using_absolute_values =====
TITLE: 2046. Sort Linked List Already Sorted Using Absolute Values
SLUG: sort-linked-list-already-sorted-using-absolute-values
CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["head"], "types": {"head": "listnode"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2046 - Sort Linked List Already Sorted Using Absolute Values
// https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortLinkedList = function(head) {
    if (!head) return null;
    let prev = head, cur = head.next;
    while (cur) {
        if (cur.val < 0) {
            prev.next = cur.next;
            cur.next = head;
            head = cur;
            cur = prev.next;
        } else {
            prev = cur;
            cur = cur.next;
        }
    }
    return head;
};


===== 2047_number_of_valid_words_in_a_sentence =====
TITLE: 2047. Number of Valid Words in a Sentence
SLUG: number-of-valid-words-in-a-sentence
CONFIG: {"class": "Solution", "method": "countValidWords", "paramOrder": ["sentence"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2047 - Number of Valid Words in a Sentence
// https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

/**
 * @param {string} sentence
 * @return {number}
 */
var countValidWords = function(sentence) {
    const valid = (w) => {
        if (w.length === 0) return false;
        let hyphen = 0;
        for (let i = 0; i < w.length; i++) {
            const c = w[i];
            if (c >= '0' && c <= '9') return false;
            if (c === '-') {
                hyphen++;
                if (hyphen > 1 || i === 0 || i === w.length - 1) return false;
                if (w[i - 1] < 'a' || w[i - 1] > 'z' || w[i + 1] < 'a' || w[i + 1] > 'z') return false;
            } else if (c === '!' || c === '.' || c === ',') {
                if (i !== w.length - 1) return false;
            } else if (c < 'a' || c > 'z') return false;
        }
        return true;
    };
    let ans = 0;
    for (const tok of sentence.split(" "))
        if (valid(tok)) ans++;
    return ans;
};


===== 2048_next_greater_numerically_balanced_number =====
TITLE: 2048. Next Greater Numerically Balanced Number
SLUG: next-greater-numerically-balanced-number
CONFIG: {"class": "Solution", "method": "nextBeautifulNumber", "paramOrder": ["n"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2048 - Next Greater Numerically Balanced Number
// https://leetcode.com/problems/next-greater-numerically-balanced-number/

/**
 * @param {number} n
 * @return {number}
 */
var nextBeautifulNumber = function(n) {
    const balanced = (x) => {
        const cnt = new Array(10).fill(0);
        while (x > 0) { cnt[x % 10]++; x = Math.floor(x / 10); }
        for (let d = 0; d < 10; d++) if (cnt[d] !== 0 && cnt[d] !== d) return false;
        return true;
    };
    for (let x = n + 1; ; x++) if (balanced(x)) return x;
};


===== 2049_count_nodes_with_the_highest_score =====
TITLE: 2049. Count Nodes With the Highest Score
SLUG: count-nodes-with-the-highest-score
CONFIG: {"class": "Solution", "method": "countHighestScoreNodes", "paramOrder": ["parents"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2049 - Count Nodes With the Highest Score
// https://leetcode.com/problems/count-nodes-with-the-highest-score/

/**
 * @param {number[]} parents
 * @return {number}
 */
var countHighestScoreNodes = function(parents) {
    const n = parents.length;
    const children = Array.from({length: n}, () => []);
    for (let i = 1; i < n; i++) children[parents[i]].push(i);
    const size = new Array(n);
    const dfs = (u) => {
        size[u] = 1;
        for (const v of children[u]) size[u] += dfs(v);
        return size[u];
    };
    dfs(0);
    let best = 0, ans = 0;
    for (let u = 0; u < n; u++) {
        let score = 1;
        for (const v of children[u]) score *= size[v];
        const up = n - size[u];
        if (up > 0) score *= up;
        if (score > best) { best = score; ans = 1; }
        else if (score === best) ans++;
    }
    return ans;
};


===== 2050_parallel_courses_iii =====
TITLE: 2050. Parallel Courses III
SLUG: parallel-courses-iii
CONFIG: {"class": "Solution", "method": "minimumTime", "paramOrder": ["n", "relations", "time"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2050 - Parallel Courses III
// https://leetcode.com/problems/parallel-courses-iii/

/**
 * @param {number} n
 * @param {number[][]} relations
 * @param {number[]} time
 * @return {number}
 */
var minimumTime = function(n, relations, time) {
    const g = Array.from({length: n + 1}, () => []);
    const indeg = new Array(n + 1).fill(0);
    const dist = new Array(n + 1).fill(0);
    for (const e of relations) { g[e[0]].push(e[1]); indeg[e[1]]++; }
    const q = [];
    for (let i = 1; i <= n; i++) {
        dist[i] = time[i - 1];
        if (indeg[i] === 0) q.push(i);
    }
    while (q.length) {
        const u = q.shift();
        for (const v of g[u]) {
            dist[v] = Math.max(dist[v], dist[u] + time[v - 1]);
            if (--indeg[v] === 0) q.push(v);
        }
    }
    let ans = 0;
    for (let i = 1; i <= n; i++) ans = Math.max(ans, dist[i]);
    return ans;
};


===== 2052_minimum_cost_to_separate_sentence_into_rows =====
TITLE: 2052. Minimum Cost to Separate Sentence Into Rows
SLUG: minimum-cost-to-separate-sentence-into-rows
CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["sentence", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2052 - Minimum Cost to Separate Sentence Into Rows
// https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/

/**
 * @param {string} sentence
 * @param {number} k
 * @return {number}
 */
var minimumCost = function(sentence, k) {
    const words = sentence.trim().split(/\s+/);
    const n = words.length;
    const INF = 1e18;
    const dp = new Array(n + 1).fill(INF);
    dp[n] = 0;
    for (let i = n - 1; i >= 0; i--) {
        let length = -1;
        for (let j = i; j < n; j++) {
            length += 1 + words[j].length;
            if (length > k) break;
            let cost = 0;
            if (j < n - 1) {
                const extra = k - length;
                cost = extra * extra;
            }
            dp[i] = Math.min(dp[i], cost + dp[j + 1]);
        }
    }
    return dp[0];
};


===== 2053_kth_distinct_string_in_an_array =====
TITLE: 2053. Kth Distinct String in an Array
SLUG: kth-distinct-string-in-an-array
CONFIG: {"class": "Solution", "method": "kthDistinct", "paramOrder": ["arr", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2053 - Kth Distinct String in an Array
// https://leetcode.com/problems/kth-distinct-string-in-an-array/

/**
 * @param {string[]} arr
 * @param {number} k
 * @return {string}
 */
var kthDistinct = function(arr, k) {
    const freq = new Map();
    for (const s of arr) freq.set(s, (freq.get(s) || 0) + 1);
    for (const s of arr) if (freq.get(s) === 1 && --k === 0) return s;
    return "";
};


===== 2054_two_best_non_overlapping_events =====
TITLE: 2054. Two Best Non-Overlapping Events
SLUG: two-best-non-overlapping-events
CONFIG: {"class": "Solution", "method": "maxTwoEvents", "paramOrder": ["events"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2054 - Two Best Non-Overlapping Events
// https://leetcode.com/problems/two-best-non-overlapping-events/

/**
 * @param {number[][]} events
 * @return {number}
 */
var maxTwoEvents = function(events) {
    events.sort((a, b) => a[0] - b[0]);
    const n = events.length;
    const suffix = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; i--) suffix[i] = Math.max(suffix[i + 1], events[i][2]);
    let ans = 0;
    for (let i = 0; i < n; i++) {
        ans = Math.max(ans, events[i][2]);
        let lo = i + 1, hi = n;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (events[mid][0] > events[i][1]) hi = mid;
            else lo = mid + 1;
        }
        if (lo < n) ans = Math.max(ans, events[i][2] + suffix[lo]);
    }
    return ans;
};


===== 2055_plates_between_candles =====
TITLE: 2055. Plates Between Candles
SLUG: plates-between-candles
CONFIG: {"class": "Solution", "method": "platesBetweenCandles", "paramOrder": ["s", "queries"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2055 - Plates Between Candles
// https://leetcode.com/problems/plates-between-candles/

/**
 * @param {string} s
 * @param {number[][]} queries
 * @return {number[]}
 */
var platesBetweenCandles = function(s, queries) {
    const n = s.length;
    const pref = new Array(n + 1).fill(0);
    const left = new Array(n), right = new Array(n);
    let last = -1;
    for (let i = 0; i < n; i++) {
        pref[i + 1] = pref[i] + (s[i] === '*' ? 1 : 0);
        if (s[i] === '|') last = i;
        left[i] = last;
    }
    last = -1;
    for (let i = n - 1; i >= 0; i--) {
        if (s[i] === '|') last = i;
        right[i] = last;
    }
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const l = right[queries[i][0]], r = left[queries[i][1]];
        if (l !== -1 && r !== -1 && l < r) ans[i] = pref[r] - pref[l];
        else ans[i] = 0;
    }
    return ans;
};


===== 2056_number_of_valid_move_combinations_on_chessboard =====
TITLE: 2056. Number of Valid Move Combinations On Chessboard
SLUG: number-of-valid-move-combinations-on-chessboard
CONFIG: {"class": "Solution", "method": "countCombinations", "paramOrder": ["pieces", "positions"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2056 - Number of Valid Move Combinations On Chessboard
// https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

/**
 * @param {string[]} pieces
 * @param {number[][]} positions
 * @return {number}
 */
var countCombinations = function(pieces, positions) {
    const dirs = {
        rook: [[1,0],[-1,0],[0,1],[0,-1]],
        bishop: [[1,1],[1,-1],[-1,1],[-1,-1]],
        queen: [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]],
    };
    const n = pieces.length;
    const allMoves = Array.from({length: n}, () => []);
    for (let i = 0; i < n; i++) {
        const ms = [{dr: 0, dc: 0, steps: 0}];
        const r = positions[i][0], c = positions[i][1];
        for (const d of dirs[pieces[i]]) {
            let nr = r + d[0], nc = c + d[1], step = 1;
            while (nr >= 1 && nr <= 8 && nc >= 1 && nc <= 8) {
                ms.push({dr: d[0], dc: d[1], steps: step});
                nr += d[0]; nc += d[1]; step++;
            }
        }
        allMoves[i] = ms;
    }
    const chosen = new Array(n);
    let ans = 0;
    const okCombo = (end) => {
        let maxT = 0;
        for (let i = 0; i <= end; i++) maxT = Math.max(maxT, chosen[i].steps);
        for (let t = 1; t <= maxT; t++) {
            const seen = new Set();
            for (let i = 0; i <= end; i++) {
                const m = chosen[i];
                let pr, pc;
                if (m.steps === 0) { pr = positions[i][0]; pc = positions[i][1]; }
                else {
                    const use = Math.min(t, m.steps);
                    pr = positions[i][0] + m.dr * use;
                    pc = positions[i][1] + m.dc * use;
                }
                const key = (BigInt(pr) << 32n) ^ (BigInt(pc) & 0xffffffffn);
                if (seen.has(key)) return false;
                seen.add(key);
            }
        }
        return true;
    };
    const dfs = (i) => {
        if (i === pieces.length) { ans++; return; }
        for (const m of allMoves[i]) {
            chosen[i] = m;
            if (okCombo(i)) dfs(i + 1);
        }
    };
    dfs(0);
    return ans;
};


===== 2057_smallest_index_with_equal_value =====
TITLE: 2057. Smallest Index With Equal Value
SLUG: smallest-index-with-equal-value
CONFIG: {"class": "Solution", "method": "smallestEqual", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2057 - Smallest Index With Equal Value
// https://leetcode.com/problems/smallest-index-with-equal-value/

/**
 * @param {number[]} nums
 * @return {number}
 */
var smallestEqual = function(nums) {
    for (let i = 0; i < nums.length; i++)
        if (i % 10 === nums[i]) return i;
    return -1;
};


===== 2058_find_the_minimum_and_maximum_number_of_nodes_between_critical_points =====
TITLE: 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
SLUG: find-the-minimum-and-maximum-number-of-nodes-between-critical-points
CONFIG: {"class": "ListNode", "method": "__init__", "paramOrder": ["val=0", "next=None"], "types": {"head": "listnode"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points
// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

/**
 * @param {ListNode} head
 * @return {number[]}
 */
var nodesBetweenCriticalPoints = function(head) {
    const crit = [];
    let prev = head, cur = head.next, idx = 1;
    while (cur && cur.next) {
        if ((cur.val > prev.val && cur.val > cur.next.val) ||
            (cur.val < prev.val && cur.val < cur.next.val))
            crit.push(idx);
        prev = cur; cur = cur.next; idx++;
    }
    if (crit.length < 2) return [-1, -1];
    let mn = crit[1] - crit[0];
    for (let i = 2; i < crit.length; i++) mn = Math.min(mn, crit[i] - crit[i - 1]);
    return [mn, crit[crit.length - 1] - crit[0]];
};


===== 2059_minimum_operations_to_convert_number =====
TITLE: 2059. Minimum Operations to Convert Number
SLUG: minimum-operations-to-convert-number
CONFIG: {"class": "Solution", "method": "minimumOperations", "paramOrder": ["nums", "start", "goal"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2059 - Minimum Operations to Convert Number
// https://leetcode.com/problems/minimum-operations-to-convert-number/

/**
 * @param {number[]} nums
 * @param {number} start
 * @param {number} goal
 * @return {number}
 */
var minimumOperations = function(nums, start, goal) {
    if (start === goal) return 0;
    const vis = new Set([start]);
    const q = [start];
    let steps = 0;
    while (q.length) {
        steps++;
        let sz = q.length;
        while (sz-- > 0) {
            const cur = q.shift();
            for (const x of nums) {
                for (const nxt of [cur + x, cur - x, cur ^ x]) {
                    if (nxt === goal) return steps;
                    if (nxt >= 0 && nxt <= 1000 && !vis.has(nxt)) {
                        vis.add(nxt);
                        q.push(nxt);
                    }
                }
            }
        }
    }
    return -1;
};


===== 2060_check_if_an_original_string_exists_given_two_encoded_strings =====
TITLE: 2060. Check if an Original String Exists Given Two Encoded Strings
SLUG: check-if-an-original-string-exists-given-two-encoded-strings
CONFIG: {"class": "Solution", "method": "possiblyEquals", "paramOrder": ["s1", "s2"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2060 - Check if an Original String Exists Given Two Encoded Strings
// https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var possiblyEquals = function(s1, s2) {
    const memo = new Map();
    const isDigit = (c) => c >= '0' && c <= '9';
    const dfs = (i, j, diff) => {
        const key = i + "," + j + "," + diff;
        if (memo.has(key)) return memo.get(key);
        const n = s1.length, m = s2.length;
        if (i === n && j === m) { memo.set(key, diff === 0); return diff === 0; }
        let res = false;
        if (diff === 0 && i < n && j < m && !isDigit(s1[i]) && !isDigit(s2[j])) {
            if (s1[i] === s2[j]) res = dfs(i + 1, j + 1, 0);
        } else if (diff > 0 && i < n && !isDigit(s1[i])) {
            res = dfs(i + 1, j, diff - 1);
        } else if (diff < 0 && j < m && !isDigit(s2[j])) {
            res = dfs(i, j + 1, diff + 1);
        }
        if (!res && i < n && isDigit(s1[i])) {
            let val = 0;
            for (let p = i; p < n && isDigit(s1[p]); p++) {
                val = val * 10 + (s1.charCodeAt(p) - 48);
                if (dfs(p + 1, j, diff + val)) { res = true; break; }
            }
        }
        if (!res && j < m && isDigit(s2[j])) {
            let val = 0;
            for (let p = j; p < m && isDigit(s2[p]); p++) {
                val = val * 10 + (s2.charCodeAt(p) - 48);
                if (dfs(i, p + 1, diff - val)) { res = true; break; }
            }
        }
        memo.set(key, res);
        return res;
    };
    return dfs(0, 0, 0);
};


===== 2061_number_of_spaces_cleaning_robot_cleaned =====
TITLE: 2061. Number of Spaces Cleaning Robot Cleaned
SLUG: number-of-spaces-cleaning-robot-cleaned
CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["room"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2061 - Number of Spaces Cleaning Robot Cleaned
// https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

/**
 * @param {number[][]} room
 * @return {number}
 */
var numberOfCleanRooms = function(room) {
    const m = room.length, n = room[0].length;
    const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    const vis = new Set();
    const cleaned = new Set([0n]);
    let r = 0, c = 0, d = 0;
    while (true) {
        const state = r * 10000 + c * 10 + d;
        if (vis.has(state)) break;
        vis.add(state);
        const nr = r + dirs[d][0], nc = c + dirs[d][1];
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && room[nr][nc] === 0) {
            r = nr; c = nc;
            cleaned.add((BigInt(r) << 32n) ^ (BigInt(c) & 0xffffffffn));
        } else d = (d + 1) % 4;
    }
    return cleaned.size;
};


===== 2062_count_vowel_substrings_of_a_string =====
TITLE: 2062. Count Vowel Substrings of a String
SLUG: count-vowel-substrings-of-a-string
CONFIG: {"class": "Solution", "method": "countVowelSubstrings", "paramOrder": ["word"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2062 - Count Vowel Substrings of a String
// https://leetcode.com/problems/count-vowel-substrings-of-a-string/

/**
 * @param {string} word
 * @return {number}
 */
var countVowelSubstrings = function(word) {
    const isVowel = (c) => "aeiou".includes(c);
    let ans = 0;
    const n = word.length;
    for (let i = 0; i < n; i++) {
        const seen = new Set();
        for (let j = i; j < n && isVowel(word[j]); j++) {
            seen.add(word[j]);
            if (seen.size === 5) ans++;
        }
    }
    return ans;
};


===== 2063_vowels_of_all_substrings =====
TITLE: 2063. Vowels of All Substrings
SLUG: vowels-of-all-substrings
CONFIG: {"class": "Solution", "method": "countVowels", "paramOrder": ["word"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2063 - Vowels of All Substrings
// https://leetcode.com/problems/vowels-of-all-substrings/

/**
 * @param {string} word
 * @return {number}
 */
var countVowels = function(word) {
    const isVowel = (c) => "aeiou".includes(c);
    const n = word.length;
    let ans = 0;
    for (let i = 0; i < n; i++)
        if (isVowel(word[i])) ans += (i + 1) * (n - i);
    return ans;
};


===== 2064_minimized_maximum_of_products_distributed_to_any_store =====
TITLE: 2064. Minimized Maximum of Products Distributed to Any Store
SLUG: minimized-maximum-of-products-distributed-to-any-store
CONFIG: {"class": "Solution", "method": "minimizedMaximum", "paramOrder": ["n", "quantities"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2064 - Minimized Maximum of Products Distributed to Any Store
// https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

/**
 * @param {number} n
 * @param {number[]} quantities
 * @return {number}
 */
var minimizedMaximum = function(n, quantities) {
    const can = (x) => {
        let need = 0;
        for (const q of quantities) {
            need += Math.floor((q + x - 1) / x);
            if (need > n) return false;
        }
        return true;
    };
    let lo = 1, hi = 0;
    for (const q of quantities) hi = Math.max(hi, q);
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (can(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};


===== 2065_maximum_path_quality_of_a_graph =====
TITLE: 2065. Maximum Path Quality of a Graph
SLUG: maximum-path-quality-of-a-graph
CONFIG: {"class": "Solution", "method": "maximalPathQuality", "paramOrder": ["values", "edges", "maxTime"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2065 - Maximum Path Quality of a Graph
// https://leetcode.com/problems/maximum-path-quality-of-a-graph/

/**
 * @param {number[]} values
 * @param {number[][]} edges
 * @param {number} maxTime
 * @return {number}
 */
var maximalPathQuality = function(values, edges, maxTime) {
    const n = values.length;
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push([e[1], e[2]]);
        g[e[1]].push([e[0], e[2]]);
    }
    let ans = 0;
    const vis = new Array(n).fill(0);
    const dfs = (u, time, quality) => {
        if (time > maxTime) return;
        const first = vis[u] === 0;
        if (first) quality += values[u];
        vis[u]++;
        if (u === 0) ans = Math.max(ans, quality);
        for (const e of g[u]) dfs(e[0], time + e[1], quality);
        vis[u]--;
    };
    dfs(0, 0, 0);
    return ans;
};


===== 2067_number_of_equal_count_substrings =====
TITLE: 2067. Number of Equal Count Substrings
SLUG: number-of-equal-count-substrings
CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["s", "count"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2067 - Number of Equal Count Substrings
// https://leetcode.com/problems/number-of-equal-count-substrings/

/**
 * @param {string} s
 * @param {number} count
 * @return {number}
 */
var equalCountSubstrings = function(s, count) {
    let ans = 0;
    const n = s.length;
    const seen = new Array(26).fill(false);
    let maxUnique = 0;
    for (const c of s) {
        const i = c.charCodeAt(0) - 97;
        if (!seen[i]) { seen[i] = true; maxUnique++; }
    }
    for (let u = 1; u <= maxUnique; u++) {
        const needLen = u * count;
        if (needLen > n) break;
        const freq = new Array(26).fill(0);
        let have = 0;
        for (let i = 0; i < n; i++) {
            const c = s.charCodeAt(i) - 97;
            freq[c]++;
            if (freq[c] === count) have++;
            else if (freq[c] === count + 1) have--;
            if (i >= needLen) {
                const p = s.charCodeAt(i - needLen) - 97;
                if (freq[p] === count) have--;
                else if (freq[p] === count + 1) have++;
                freq[p]--;
            }
            if (i + 1 >= needLen && have === u) ans++;
        }
    }
    return ans;
};


===== 2068_check_whether_two_strings_are_almost_equivalent =====
TITLE: 2068. Check Whether Two Strings are Almost Equivalent
SLUG: check-whether-two-strings-are-almost-equivalent
CONFIG: {"class": "Solution", "method": "checkAlmostEquivalent", "paramOrder": ["word1", "word2"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2068 - Check Whether Two Strings Are Almost Equivalent
// https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var checkAlmostEquivalent = function(word1, word2) {
    const freq = new Array(26).fill(0);
    for (let i = 0; i < word1.length; i++) {
        freq[word1.charCodeAt(i) - 97]++;
        freq[word2.charCodeAt(i) - 97]--;
    }
    for (const v of freq) if (v > 3 || v < -3) return false;
    return true;
};


===== 2069_walking_robot_simulation_ii =====
TITLE: 2069. Walking Robot Simulation II
SLUG: walking-robot-simulation-ii
CONFIG: {"class": "Robot", "description": "Update method name and add cases to cases.json when implementing the solution.", "kind": "design", "runnable": true}
---JS---
// LeetCode 2069 - Walking Robot Simulation II
// https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot {
    /**
     * @param {number} width
     * @param {number} height
     */
    constructor(width, height) {
        this.w = width;
        this.h = height;
        this.peri = 2 * (width + height) - 4;
        this.pos = 0;
        this.moved = false;
    }

    getPosDir() {
        let p = this.pos;
        if (p === 0) {
            if (!this.moved) return [0, 0, 0];
            return [0, 0, 3];
        }
        if (p <= this.w - 1) return [p, 0, 0];
        p -= this.w - 1;
        if (p <= this.h - 1) return [this.w - 1, p, 1];
        p -= this.h - 1;
        if (p <= this.w - 1) return [this.w - 1 - p, this.h - 1, 2];
        p -= this.w - 1;
        return [0, this.h - 1 - p, 3];
    }

    /**
     * @param {number} num
     * @return {void}
     */
    step(num) {
        this.moved = true;
        this.pos = (this.pos + num) % this.peri;
    }

    /**
     * @return {number[]}
     */
    getPos() {
        const pd = this.getPosDir();
        return [pd[0], pd[1]];
    }

    /**
     * @return {string}
     */
    getDir() {
        const names = ["East", "North", "West", "South"];
        return names[this.getPosDir()[2]];
    }
}


===== 2070_most_beautiful_item_for_each_query =====
TITLE: 2070. Most Beautiful Item for Each Query
SLUG: most-beautiful-item-for-each-query
CONFIG: {"class": "Solution", "method": "maximumBeauty", "paramOrder": ["items", "queries"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2070 - Most Beautiful Item for Each Query
// https://leetcode.com/problems/most-beautiful-item-for-each-query/

/**
 * @param {number[][]} items
 * @param {number[]} queries
 * @return {number[]}
 */
var maximumBeauty = function(items, queries) {
    items.sort((a, b) => a[0] - b[0]);
    let maxB = 0;
    for (const it of items) {
        maxB = Math.max(maxB, it[1]);
        it[1] = maxB;
    }
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        let lo = 0, hi = items.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (items[mid][0] <= queries[i]) lo = mid + 1;
            else hi = mid;
        }
        ans[i] = lo === 0 ? 0 : items[lo - 1][1];
    }
    return ans;
};


===== 2071_maximum_number_of_tasks_you_can_assign =====
TITLE: 2071. Maximum Number of Tasks You Can Assign
SLUG: maximum-number-of-tasks-you-can-assign
CONFIG: {"class": "Solution", "method": "maxTaskAssign", "paramOrder": ["tasks", "workers", "pills", "strength"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2071 - Maximum Number of Tasks You Can Assign
// https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

/**
 * @param {number[]} tasks
 * @param {number[]} workers
 * @param {number} pills
 * @param {number} strength
 * @return {number}
 */
var maxTaskAssign = function(tasks, workers, pills, strength) {
    tasks.sort((a, b) => a - b);
    workers.sort((a, b) => a - b);
    const remove = (ws, x) => {
        const c = ws.get(x);
        if (c === 1) ws.delete(x);
        else ws.set(x, c - 1);
    };
    const can = (k) => {
        if (k === 0) return true;
        const ws = new Map();
        for (let i = workers.length - k; i < workers.length; i++)
            ws.set(workers[i], (ws.get(workers[i]) || 0) + 1);
        let p = pills;
        const keys = () => [...ws.keys()].sort((a, b) => a - b);
        for (let i = k - 1; i >= 0; i--) {
            const task = tasks[i];
            const ks = keys();
            const strongest = ks[ks.length - 1];
            if (strongest >= task) {
                remove(ws, strongest);
                continue;
            }
            if (p === 0) return false;
            const need = task - strength;
            let found = null;
            for (const key of ks) if (key >= need) { found = key; break; }
            if (found === null) return false;
            remove(ws, found);
            p--;
        }
        return true;
    };
    let lo = 0, hi = Math.min(tasks.length, workers.length);
    while (lo < hi) {
        const mid = (lo + hi + 1) >> 1;
        if (can(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};


===== 2073_time_needed_to_buy_tickets =====
TITLE: 2073. Time Needed to Buy Tickets
SLUG: time-needed-to-buy-tickets
CONFIG: {"class": "Solution", "method": "timeRequiredToBuy", "paramOrder": ["tickets", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2073 - Time Needed to Buy Tickets
// https://leetcode.com/problems/time-needed-to-buy-tickets/

/**
 * @param {number[]} tickets
 * @param {number} k
 * @return {number}
 */
var timeRequiredToBuy = function(tickets, k) {
    let ans = 0;
    for (let i = 0; i < tickets.length; i++) {
        if (i <= k) ans += Math.min(tickets[i], tickets[k]);
        else ans += Math.min(tickets[i], tickets[k] - 1);
    }
    return ans;
};


===== 2074_reverse_nodes_in_even_length_groups =====
TITLE: 2074. Reverse Nodes in Even Length Groups
SLUG: reverse-nodes-in-even-length-groups
CONFIG: {"class": "ListNode", "method": "__init__", "paramOrder": ["val=0", "next=None"], "types": {"head": "listnode"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2074 - Reverse Nodes in Even Length Groups
// https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseEvenLengthGroups = function(head) {
    const dummy = new ListNode(0, head);
    let prev = dummy;
    let group = 1;
    while (prev.next) {
        const cur = prev.next;
        let cnt = 0;
        let node = cur;
        while (node && cnt < group) { node = node.next; cnt++; }
        if (cnt % 2 === 0) {
            let revPrev = node;
            let p = cur;
            for (let i = 0; i < cnt; i++) {
                const nxt = p.next;
                p.next = revPrev;
                revPrev = p;
                p = nxt;
            }
            prev.next = revPrev;
            prev = cur;
        } else {
            for (let i = 0; i < cnt; i++) prev = prev.next;
        }
        group++;
    }
    return dummy.next;
};


===== 2075_decode_the_slanted_ciphertext =====
TITLE: 2075. Decode the Slanted Ciphertext
SLUG: decode-the-slanted-ciphertext
CONFIG: {"class": "Solution", "method": "decodeCiphertext", "paramOrder": ["encodedText", "rows"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2075 - Decode the Slanted Ciphertext
// https://leetcode.com/problems/decode-the-slanted-ciphertext/

/**
 * @param {string} encodedText
 * @param {number} rows
 * @return {string}
 */
var decodeCiphertext = function(encodedText, rows) {
    if (rows === 1) return encodedText;
    const cols = encodedText.length / rows;
    let b = "";
    for (let c = 0; c < cols; c++)
        for (let r = 0; r < rows && c + r < cols; r++)
            b += encodedText[r * cols + c + r];
    while (b.length > 0 && b[b.length - 1] === ' ') b = b.slice(0, -1);
    return b;
};


===== 2076_process_restricted_friend_requests =====
TITLE: 2076. Process Restricted Friend Requests
SLUG: process-restricted-friend-requests
CONFIG: {"class": "Solution", "method": "friendRequests", "paramOrder": ["n", "restrictions", "requests"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2076 - Process Restricted Friend Requests
// https://leetcode.com/problems/process-restricted-friend-requests/

/**
 * @param {number} n
 * @param {number[][]} restrictions
 * @param {number[][]} requests
 * @return {boolean[]}
 */
var friendRequests = function(n, restrictions, requests) {
    const parent = Array.from({length: n}, (_, i) => i);
    const find = (x) => parent[x] === x ? x : (parent[x] = find(parent[x]));
    const unite = (a, b) => {
        a = find(a); b = find(b);
        if (a !== b) parent[a] = b;
    };
    const ans = new Array(requests.length);
    for (let i = 0; i < requests.length; i++) {
        const u = find(requests[i][0]), v = find(requests[i][1]);
        let ok = true;
        if (u !== v) {
            for (const r of restrictions) {
                const x = find(r[0]), y = find(r[1]);
                if ((x === u && y === v) || (x === v && y === u)) { ok = false; break; }
            }
        }
        ans[i] = ok;
        if (ok) unite(u, v);
    }
    return ans;
};


===== 2077_paths_in_maze_that_lead_to_same_room =====
TITLE: 2077. Paths in Maze That Lead to Same Room
SLUG: paths-in-maze-that-lead-to-same-room
CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["n", "corridors"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2077 - Paths in Maze That Lead to Same Room
// https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/

/**
 * @param {number} n
 * @param {number[][]} corridors
 * @return {number}
 */
var numberOfPaths = function(n, corridors) {
    const g = Array.from({length: n + 1}, () => new Set());
    for (const e of corridors) {
        g[e[0]].add(e[1]);
        g[e[1]].add(e[0]);
    }
    let ans = 0;
    for (const e of corridors) {
        const a = e[0], b = e[1];
        for (const c of g[a]) if (g[b].has(c)) ans++;
    }
    return Math.floor(ans / 3);
};


===== 2078_two_furthest_houses_with_different_colors =====
TITLE: 2078. Two Furthest Houses With Different Colors
SLUG: two-furthest-houses-with-different-colors
CONFIG: {"class": "Solution", "method": "maxDistance", "paramOrder": ["colors"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2078 - Two Furthest Houses With Different Colors
// https://leetcode.com/problems/two-furthest-houses-with-different-colors/

/**
 * @param {number[]} colors
 * @return {number}
 */
var maxDistance = function(colors) {
    const n = colors.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (colors[i] !== colors[0]) ans = Math.max(ans, i);
        if (colors[i] !== colors[n - 1]) ans = Math.max(ans, n - 1 - i);
    }
    return ans;
};


===== 2079_watering_plants =====
TITLE: 2079. Watering Plants
SLUG: watering-plants
CONFIG: {"class": "Solution", "method": "wateringPlants", "paramOrder": ["plants", "capacity"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2079 - Watering Plants
// https://leetcode.com/problems/watering-plants/

/**
 * @param {number[]} plants
 * @param {number} capacity
 * @return {number}
 */
var wateringPlants = function(plants, capacity) {
    let ans = 0, cur = capacity;
    for (let i = 0; i < plants.length; i++) {
        if (cur < plants[i]) { ans += i * 2; cur = capacity; }
        cur -= plants[i];
        ans++;
    }
    return ans;
};


===== 2080_range_frequency_queries =====
TITLE: 2080. Range Frequency Queries
SLUG: range-frequency-queries
CONFIG: {"class": "RangeFreqQuery", "description": "Update method name and add cases to cases.json when implementing the solution.", "kind": "design", "runnable": true}
---JS---
// LeetCode 2080 - Range Frequency Queries
// https://leetcode.com/problems/range-frequency-queries/

class RangeFreqQuery {
    /**
     * @param {number[]} arr
     */
    constructor(arr) {
        this.pos = new Map();
        for (let i = 0; i < arr.length; i++) {
            if (!this.pos.has(arr[i])) this.pos.set(arr[i], []);
            this.pos.get(arr[i]).push(i);
        }
    }

    lower(p, x) {
        let lo = 0, hi = p.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (p[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    upper(p, x) {
        let lo = 0, hi = p.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (p[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    /**
     * @param {number} left
     * @param {number} right
     * @param {number} value
     * @return {number}
     */
    query(left, right, value) {
        const p = this.pos.get(value);
        if (!p) return 0;
        return this.upper(p, right) - this.lower(p, left);
    }
}


===== 2081_sum_of_k_mirror_numbers =====
TITLE: 2081. Sum of k-Mirror Numbers
SLUG: sum-of-k-mirror-numbers
CONFIG: {"class": "Solution", "method": "kMirror", "paramOrder": ["k", "n"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2081 - Sum of k-Mirror Numbers
// https://leetcode.com/problems/sum-of-k-mirror-numbers/

/**
 * @param {number} k
 * @param {number} n
 * @return {number}
 */
var kMirror = function(k, n) {
    const isPalBase = (x, bas) => {
        const digits = [];
        while (x > 0) { digits.push(x % bas); x = Math.floor(x / bas); }
        for (let l = 0, r = digits.length - 1; l < r; l++, r--)
            if (digits[l] !== digits[r]) return false;
        return true;
    };
    let ans = 0, count = 0;
    for (let length = 1; count < n; length++) {
        let start = 1;
        for (let i = 1; i < Math.floor((length + 1) / 2); i++) start *= 10;
        const end = start * 10;
        for (let half = start; half < end && count < n; half++) {
            let pal = half;
            if (length % 2 === 0) {
                let x = half;
                while (x > 0) { pal = pal * 10 + x % 10; x = Math.floor(x / 10); }
            } else {
                let x = Math.floor(half / 10);
                while (x > 0) { pal = pal * 10 + x % 10; x = Math.floor(x / 10); }
            }
            if (isPalBase(pal, k)) { ans += pal; count++; }
        }
    }
    return ans;
};


===== 2083_substrings_that_begin_and_end_with_the_same_letter =====
TITLE: 2083. Substrings That Begin and End With the Same Letter
SLUG: substrings-that-begin-and-end-with-the-same-letter
CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["s"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2083 - Substrings That Begin and End With the Same Letter
// https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/

/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    const freq = new Array(26).fill(0);
    let ans = 0;
    for (const c of s) {
        freq[c.charCodeAt(0) - 97]++;
        ans += freq[c.charCodeAt(0) - 97];
    }
    return ans;
};


===== 2085_count_common_words_with_one_occurrence =====
TITLE: 2085. Count Common Words With One Occurrence
SLUG: count-common-words-with-one-occurrence
CONFIG: {"class": "Solution", "method": "countWords", "paramOrder": ["words1", "words2"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2085 - Count Common Words With One Occurrence
// https://leetcode.com/problems/count-common-words-with-one-occurrence/

/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @return {number}
 */
var countWords = function(words1, words2) {
    const f1 = new Map(), f2 = new Map();
    for (const w of words1) f1.set(w, (f1.get(w) || 0) + 1);
    for (const w of words2) f2.set(w, (f2.get(w) || 0) + 1);
    let ans = 0;
    for (const [k, v] of f1)
        if (v === 1 && (f2.get(k) || 0) === 1) ans++;
    return ans;
};


===== 2086_minimum_number_of_food_buckets_to_feed_the_hamsters =====
TITLE: 2086. Minimum Number of Food Buckets to Feed the Hamsters
SLUG: minimum-number-of-food-buckets-to-feed-the-hamsters
CONFIG: {"class": "Solution", "method": "minimumBuckets", "paramOrder": ["hamsters"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2086 - Minimum Number of Food Buckets to Feed the Hamsters
// https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

/**
 * @param {string} hamsters
 * @return {number}
 */
var minimumBuckets = function(hamsters) {
    const b = hamsters.split('');
    let ans = 0;
    for (let i = 0; i < b.length; i++) {
        if (b[i] !== 'H') continue;
        if (i > 0 && b[i - 1] === 'B') continue;
        if (i + 1 < b.length && b[i + 1] === '.') { b[i + 1] = 'B'; ans++; }
        else if (i > 0 && b[i - 1] === '.') { b[i - 1] = 'B'; ans++; }
        else return -1;
    }
    return ans;
};


===== 2087_minimum_cost_homecoming_of_a_robot_in_a_grid =====
TITLE: 2087. Minimum Cost Homecoming of a Robot in a Grid
SLUG: minimum-cost-homecoming-of-a-robot-in-a-grid
CONFIG: {"class": "Solution", "method": "minCost", "paramOrder": ["startPos", "homePos", "rowCosts", "colCosts"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2087 - Minimum Cost Homecoming of a Robot in a Grid
// https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

/**
 * @param {number[]} startPos
 * @param {number[]} homePos
 * @param {number[]} rowCosts
 * @param {number[]} colCosts
 * @return {number}
 */
var minCost = function(startPos, homePos, rowCosts, colCosts) {
    let ans = 0;
    const sr = startPos[0], sc = startPos[1], hr = homePos[0], hc = homePos[1];
    if (sr < hr) for (let r = sr + 1; r <= hr; r++) ans += rowCosts[r];
    else for (let r = sr - 1; r >= hr; r--) ans += rowCosts[r];
    if (sc < hc) for (let c = sc + 1; c <= hc; c++) ans += colCosts[c];
    else for (let c = sc - 1; c >= hc; c--) ans += colCosts[c];
    return ans;
};


===== 2088_count_fertile_pyramids_in_a_land =====
TITLE: 2088. Count Fertile Pyramids in a Land
SLUG: count-fertile-pyramids-in-a-land
CONFIG: {"class": "Solution", "method": "countPyramids", "paramOrder": ["grid"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2088 - Count Fertile Pyramids in a Land
// https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var countPyramids = function(grid) {
    const count = (g) => {
        const m = g.length, n = g[0].length;
        const dp = g.map(row => row.slice());
        let ans = 0;
        for (let i = m - 2; i >= 0; i--) {
            for (let j = 1; j < n - 1; j++) {
                if (g[i][j] === 1) {
                    dp[i][j] = 1 + Math.min(dp[i + 1][j - 1], Math.min(dp[i + 1][j], dp[i + 1][j + 1]));
                    ans += dp[i][j] - 1;
                }
            }
        }
        return ans;
    };
    let ans = count(grid);
    const m = grid.length;
    const rev = Array.from({length: m}, (_, i) => grid[m - 1 - i]);
    return ans + count(rev);
};


===== 2089_find_target_indices_after_sorting_array =====
TITLE: 2089. Find Target Indices After Sorting Array
SLUG: find-target-indices-after-sorting-array
CONFIG: {"class": "Solution", "method": "targetIndices", "paramOrder": ["nums", "target"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2089 - Find Target Indices After Sorting Array
// https://leetcode.com/problems/find-target-indices-after-sorting-array/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    let less = 0, eq = 0;
    for (const x of nums) {
        if (x < target) less++;
        else if (x === target) eq++;
    }
    const ans = [];
    for (let i = 0; i < eq; i++) ans.push(less + i);
    return ans;
};


===== 2090_k_radius_subarray_averages =====
TITLE: 2090. K Radius Subarray Averages
SLUG: k-radius-subarray-averages
CONFIG: {"class": "Solution", "method": "getAverages", "paramOrder": ["nums", "k"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2090 - K Radius Subarray Averages
// https://leetcode.com/problems/k-radius-subarray-averages/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var getAverages = function(nums, k) {
    const n = nums.length;
    const ans = new Array(n).fill(-1);
    if (2 * k + 1 > n) return ans;
    let sum = 0;
    for (let i = 0; i < 2 * k + 1; i++) sum += nums[i];
    ans[k] = Math.floor(sum / (2 * k + 1));
    for (let i = k + 1; i + k < n; i++) {
        sum += nums[i + k] - nums[i - k - 1];
        ans[i] = Math.floor(sum / (2 * k + 1));
    }
    return ans;
};


===== 2091_removing_minimum_and_maximum_from_array =====
TITLE: 2091. Removing Minimum and Maximum From Array
SLUG: removing-minimum-and-maximum-from-array
CONFIG: {"class": "Solution", "method": "minimumDeletions", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2091 - Removing Minimum and Maximum From Array
// https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDeletions = function(nums) {
    const n = nums.length;
    let mi = 0, ma = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] < nums[mi]) mi = i;
        if (nums[i] > nums[ma]) ma = i;
    }
    if (mi > ma) { const t = mi; mi = ma; ma = t; }
    return Math.min(ma + 1, Math.min(n - mi, mi + 1 + n - ma));
};


===== 2092_find_all_people_with_secret =====
TITLE: 2092. Find All People With Secret
SLUG: find-all-people-with-secret
CONFIG: {"class": "Solution", "method": "findAllPeople", "paramOrder": ["n", "meetings", "firstPerson"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2092 - Find All People With Secret
// https://leetcode.com/problems/find-all-people-with-secret/

/**
 * @param {number} n
 * @param {number[][]} meetings
 * @param {number} firstPerson
 * @return {number[]}
 */
var findAllPeople = function(n, meetings, firstPerson) {
    meetings.sort((a, b) => a[2] - b[2]);
    const parent = Array.from({length: n}, (_, i) => i);
    const find = (x) => parent[x] === x ? x : (parent[x] = find(parent[x]));
    const unite = (a, b) => {
        a = find(a); b = find(b);
        if (a !== b) parent[a] = b;
    };
    const know = new Array(n).fill(false);
    know[0] = know[firstPerson] = true;
    unite(0, firstPerson);
    for (let i = 0; i < meetings.length; ) {
        let j = i;
        while (j < meetings.length && meetings[j][2] === meetings[i][2]) j++;
        for (let k = i; k < j; k++) unite(meetings[k][0], meetings[k][1]);
        const root0 = find(0);
        const reset = [];
        for (let k = i; k < j; k++) {
            const a = meetings[k][0], b = meetings[k][1];
            if (find(a) !== root0) { reset.push(a); reset.push(b); }
            else { know[a] = know[b] = true; }
        }
        for (const x of reset) parent[x] = x;
        i = j;
    }
    const ans = [];
    for (let i = 0; i < n; i++) if (find(i) === find(0) || know[i]) ans.push(i);
    return ans;
};


===== 2093_minimum_cost_to_reach_city_with_discounts =====
TITLE: 2093. Minimum Cost to Reach City With Discounts
SLUG: minimum-cost-to-reach-city-with-discounts
CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["n", "highways", "discounts"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2093 - Minimum Cost to Reach City With Discounts
// https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/

/**
 * @param {number} n
 * @param {number[][]} highways
 * @param {number} discounts
 * @return {number}
 */
var minimumCost = function(n, highways, discounts) {
    const g = Array.from({length: n}, () => []);
    for (const [a, b, c] of highways) {
        g[a].push([b, c]);
        g[b].push([a, c]);
    }
    const INF = 1 << 30;
    const dist = Array.from({length: n}, () => new Array(discounts + 1).fill(INF));
    const pq = [];
    const push = (item) => {
        pq.push(item);
        let i = pq.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (pq[p][0] <= pq[i][0]) break;
            [pq[p], pq[i]] = [pq[i], pq[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = pq[0];
        const last = pq.pop();
        if (pq.length) {
            pq[0] = last;
            let i = 0;
            while (true) {
                let l = i * 2 + 1, r = l + 1, s = i;
                if (l < pq.length && pq[l][0] < pq[s][0]) s = l;
                if (r < pq.length && pq[r][0] < pq[s][0]) s = r;
                if (s === i) break;
                [pq[s], pq[i]] = [pq[i], pq[s]];
                i = s;
            }
        }
        return top;
    };
    dist[0][discounts] = 0;
    push([0, 0, discounts]);
    while (pq.length) {
        const [cost, city, disc] = pop();
        if (city === n - 1) return cost;
        if (cost > dist[city][disc]) continue;
        for (const [v, w] of g[city]) {
            if (cost + w < dist[v][disc]) {
                dist[v][disc] = cost + w;
                push([dist[v][disc], v, disc]);
            }
            if (disc > 0 && cost + Math.floor(w / 2) < dist[v][disc - 1]) {
                dist[v][disc - 1] = cost + Math.floor(w / 2);
                push([dist[v][disc - 1], v, disc - 1]);
            }
        }
    }
    return -1;
};


===== 2094_finding_3_digit_even_numbers =====
TITLE: 2094. Finding 3-Digit Even Numbers
SLUG: finding-3-digit-even-numbers
CONFIG: {"class": "Solution", "method": "findEvenNumbers", "paramOrder": ["digits"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2094 - Finding 3-Digit Even Numbers
// https://leetcode.com/problems/finding-3-digit-even-numbers/

/**
 * @param {number[]} digits
 * @return {number[]}
 */
var findEvenNumbers = function(digits) {
    const freq = new Array(10).fill(0);
    for (const d of digits) freq[d]++;
    const ans = [];
    for (let x = 100; x <= 998; x += 2) {
        const a = Math.floor(x / 100), b = Math.floor(x / 10) % 10, c = x % 10;
        freq[a]--; freq[b]--; freq[c]--;
        if (freq[a] >= 0 && freq[b] >= 0 && freq[c] >= 0) ans.push(x);
        freq[a]++; freq[b]++; freq[c]++;
    }
    return ans;
};


===== 2095_delete_the_middle_node_of_a_linked_list =====
TITLE: 2095. Delete the Middle Node of a Linked List
SLUG: delete-the-middle-node-of-a-linked-list
CONFIG: {"class": "ListNode", "method": "__init__", "paramOrder": ["val=0", "next=None"], "types": {"head": "listnode"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2095 - Delete the Middle Node of a Linked List
// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteMiddle = function(head) {
    if (head.next === null) return null;
    let slow = head, fast = head, prev = null;
    while (fast !== null && fast.next !== null) {
        prev = slow;
        slow = slow.next;
        fast = fast.next.next;
    }
    prev.next = slow.next;
    return head;
};


===== 2096_step_by_step_directions_from_a_binary_tree_node_to_another =====
TITLE: 2096. Step-By-Step Directions From a Binary Tree Node to Another
SLUG: step-by-step-directions-from-a-binary-tree-node-to-another
CONFIG: {"class": "TreeNode", "method": "__init__", "paramOrder": ["val=0", "left=None", "right=None"], "types": {"root": "treenode"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} startValue
 * @param {number} destValue
 * @return {string}
 */
var getDirections = function(root, startValue, destValue) {
    const path = (node, target, p) => {
        if (node === null) return false;
        if (node.val === target) return true;
        p.push('L');
        if (path(node.left, target, p)) return true;
        p[p.length - 1] = 'R';
        if (path(node.right, target, p)) return true;
        p.pop();
        return false;
    };
    const ps = [], pd = [];
    path(root, startValue, ps);
    path(root, destValue, pd);
    let i = 0;
    while (i < ps.length && i < pd.length && ps[i] === pd[i]) i++;
    return 'U'.repeat(ps.length - i) + pd.slice(i).join('');
};


===== 2097_valid_arrangement_of_pairs =====
TITLE: 2097. Valid Arrangement of Pairs
SLUG: valid-arrangement-of-pairs
CONFIG: {"class": "Solution", "method": "validArrangement", "paramOrder": ["pairs"], "types": {"return": "integer[][]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2097 - Valid Arrangement of Pairs
// https://leetcode.com/problems/valid-arrangement-of-pairs/

/**
 * @param {number[][]} pairs
 * @return {number[][]}
 */
var validArrangement = function(pairs) {
    const g = new Map();
    const indeg = new Map();
    const outdeg = new Map();
    for (const [u, v] of pairs) {
        if (!g.has(u)) g.set(u, []);
        g.get(u).push(v);
        outdeg.set(u, (outdeg.get(u) || 0) + 1);
        indeg.set(v, (indeg.get(v) || 0) + 1);
    }
    let start = pairs[0][0];
    for (const [u, o] of outdeg) {
        if (o - (indeg.get(u) || 0) === 1) { start = u; break; }
    }
    const path = [];
    const dfs = (u) => {
        const nbrs = g.get(u) || [];
        while (nbrs.length) {
            const v = nbrs.pop();
            dfs(v);
        }
        path.push(u);
    };
    dfs(start);
    path.reverse();
    const ans = [];
    for (let i = 0; i + 1 < path.length; i++) ans.push([path[i], path[i + 1]]);
    return ans;
};


===== 2098_subsequence_of_size_k_with_the_largest_even_sum =====
TITLE: 2098. Subsequence of Size K With the Largest Even Sum
SLUG: subsequence-of-size-k-with-the-largest-even-sum
CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["nums", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2098 - Subsequence of Size K With the Largest Even Sum
// https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var largestEvenSum = function(nums, k) {
    const arr = nums.slice().sort((a, b) => b - a);
    let sum = 0;
    for (let i = 0; i < k; i++) sum += arr[i];
    if (sum % 2 === 0) return sum;
    let ans = -1;
    let oddIn = -1, evenIn = -1, oddOut = -1, evenOut = -1;
    for (let i = k - 1; i >= 0; i--) {
        if (arr[i] % 2 !== 0 && oddIn === -1) oddIn = i;
        if (arr[i] % 2 === 0 && evenIn === -1) evenIn = i;
    }
    for (let i = k; i < arr.length; i++) {
        if (arr[i] % 2 !== 0 && oddOut === -1) oddOut = i;
        if (arr[i] % 2 === 0 && evenOut === -1) evenOut = i;
    }
    if (oddIn !== -1 && evenOut !== -1) ans = Math.max(ans, sum - arr[oddIn] + arr[evenOut]);
    if (evenIn !== -1 && oddOut !== -1) ans = Math.max(ans, sum - arr[evenIn] + arr[oddOut]);
    return ans;
};


===== 2099_find_subsequence_of_length_k_with_the_largest_sum =====
TITLE: 2099. Find Subsequence of Length K With the Largest Sum
SLUG: find-subsequence-of-length-k-with-the-largest-sum
CONFIG: {"class": "Solution", "method": "maxSubsequence", "paramOrder": ["nums", "k"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2099 - Find Subsequence of Length K With the Largest Sum
// https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSubsequence = function(nums, k) {
    const n = nums.length;
    const arr = Array.from({length: n}, (_, i) => [nums[i], i]);
    arr.sort((a, b) => b[0] - a[0]);
    const idx = arr.slice(0, k).map(x => x[1]).sort((a, b) => a - b);
    return idx.map(i => nums[i]);
};


===== 2100_find_good_days_to_rob_the_bank =====
TITLE: 2100. Find Good Days to Rob the Bank
SLUG: find-good-days-to-rob-the-bank
CONFIG: {"class": "Solution", "method": "goodDaysToRobBank", "paramOrder": ["security", "time"], "types": {"return": "integer[]"}, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2100 - Find Good Days to Rob the Bank
// https://leetcode.com/problems/find-good-days-to-rob-the-bank/

/**
 * @param {number[]} security
 * @param {number} time
 * @return {number[]}
 */
var goodDaysToRobBank = function(security, time) {
    const n = security.length;
    if (time === 0) return Array.from({length: n}, (_, i) => i);
    const left = new Array(n).fill(0), right = new Array(n).fill(0);
    for (let i = 1; i < n; i++) if (security[i] <= security[i - 1]) left[i] = left[i - 1] + 1;
    for (let i = n - 2; i >= 0; i--) if (security[i] <= security[i + 1]) right[i] = right[i + 1] + 1;
    const ans = [];
    for (let i = time; i < n - time; i++)
        if (left[i] >= time && right[i] >= time) ans.push(i);
    return ans;
};


===== 2101_detonate_the_maximum_bombs =====
TITLE: 2101. Detonate the Maximum Bombs
SLUG: detonate-the-maximum-bombs
CONFIG: {"class": "Solution", "method": "maximumDetonation", "paramOrder": ["bombs"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2101 - Detonate the Maximum Bombs
// https://leetcode.com/problems/detonate-the-maximum-bombs/

/**
 * @param {number[][]} bombs
 * @return {number}
 */
var maximumDetonation = function(bombs) {
    const n = bombs.length;
    const g = Array.from({length: n}, () => []);
    for (let i = 0; i < n; i++) {
        const x1 = bombs[i][0], y1 = bombs[i][1], r1 = bombs[i][2];
        for (let j = 0; j < n; j++) {
            if (i === j) continue;
            const dx = bombs[j][0] - x1, dy = bombs[j][1] - y1;
            if (dx * dx + dy * dy <= r1 * r1) g[i].push(j);
        }
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const vis = new Array(n).fill(false);
        const q = [i];
        vis[i] = true;
        let cnt = 0;
        while (q.length) {
            const u = q.shift();
            cnt++;
            for (const v of g[u]) if (!vis[v]) { vis[v] = true; q.push(v); }
        }
        ans = Math.max(ans, cnt);
    }
    return ans;
};


===== 2102_sequentially_ordinal_rank_tracker =====
TITLE: 2102. Sequentially Ordinal Rank Tracker
SLUG: sequentially-ordinal-rank-tracker
CONFIG: {"class": "SORTracker", "description": "Update method name and add cases to cases.json when implementing the solution.", "kind": "design", "runnable": true}
---JS---
// LeetCode 2102 - Sequentially Ordinal Rank Tracker
// https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

class SORTracker {
    constructor() {
        this.best = []; // min-heap by score, then max name
        this.rest = []; // max-heap by score, then min name
        this.k = 0;
    }

    _cmpBest(a, b) {
        if (a.score !== b.score) return a.score - b.score;
        return b.name < a.name ? -1 : b.name > a.name ? 1 : 0;
    }

    _cmpRest(a, b) {
        if (a.score !== b.score) return b.score - a.score;
        return a.name < b.name ? -1 : a.name > b.name ? 1 : 0;
    }

    _push(heap, item, cmp) {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (cmp(heap[p], heap[i]) <= 0) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    }

    _pop(heap, cmp) {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length) {
            heap[0] = last;
            let i = 0;
            while (true) {
                let l = i * 2 + 1, r = l + 1, s = i;
                if (l < heap.length && cmp(heap[l], heap[s]) < 0) s = l;
                if (r < heap.length && cmp(heap[r], heap[s]) < 0) s = r;
                if (s === i) break;
                [heap[s], heap[i]] = [heap[i], heap[s]];
                i = s;
            }
        }
        return top;
    }

    /**
     * @param {string} name
     * @param {number} score
     * @return {void}
     */
    add(name, score) {
        this._push(this.best, {name, score}, this._cmpBest);
        if (this.best.length > this.k) this._push(this.rest, this._pop(this.best, this._cmpBest), this._cmpRest);
    }

    /**
     * @return {string}
     */
    get() {
        this.k++;
        if (this.rest.length) this._push(this.best, this._pop(this.rest, this._cmpRest), this._cmpBest);
        return this.best[0].name;
    }
}


===== 2103_rings_and_rods =====
TITLE: 2103. Rings and Rods
SLUG: rings-and-rods
CONFIG: {"class": "Solution", "method": "countPoints", "paramOrder": ["rings"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2103 - Rings and Rods
// https://leetcode.com/problems/rings-and-rods/

/**
 * @param {string} rings
 * @return {number}
 */
var countPoints = function(rings) {
    const mask = new Array(10).fill(0);
    for (let i = 0; i < rings.length; i += 2) {
        const c = rings[i];
        const r = rings.charCodeAt(i + 1) - 48;
        const bit = c === 'R' ? 1 : c === 'G' ? 2 : 4;
        mask[r] |= bit;
    }
    let ans = 0;
    for (const m of mask) if (m === 7) ans++;
    return ans;
};


===== 2104_sum_of_subarray_ranges =====
TITLE: 2104. Sum of Subarray Ranges
SLUG: sum-of-subarray-ranges
CONFIG: {"class": "Solution", "method": "subArrayRanges", "paramOrder": ["nums"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2104 - Sum of Subarray Ranges
// https://leetcode.com/problems/sum-of-subarray-ranges/

/**
 * @param {number[]} nums
 * @return {number}
 */
var subArrayRanges = function(nums) {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        let mn = nums[i], mx = nums[i];
        for (let j = i; j < n; j++) {
            mn = Math.min(mn, nums[j]);
            mx = Math.max(mx, nums[j]);
            ans += mx - mn;
        }
    }
    return ans;
};


===== 2105_watering_plants_ii =====
TITLE: 2105. Watering Plants II
SLUG: watering-plants-ii
CONFIG: {"class": "Solution", "method": "minimumRefill", "paramOrder": ["plants", "capacityA", "capacityB"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2105 - Watering Plants II
// https://leetcode.com/problems/watering-plants-ii/

/**
 * @param {number[]} plants
 * @param {number} capacityA
 * @param {number} capacityB
 * @return {number}
 */
var minimumRefill = function(plants, capacityA, capacityB) {
    let i = 0, j = plants.length - 1;
    let a = capacityA, b = capacityB, ans = 0;
    while (i < j) {
        if (a < plants[i]) { ans++; a = capacityA; }
        a -= plants[i++];
        if (b < plants[j]) { ans++; b = capacityB; }
        b -= plants[j--];
    }
    if (i === j) {
        if (a >= b) { if (a < plants[i]) ans++; }
        else if (b < plants[i]) ans++;
    }
    return ans;
};


===== 2106_maximum_fruits_harvested_after_at_most_k_steps =====
TITLE: 2106. Maximum Fruits Harvested After at Most K Steps
SLUG: maximum-fruits-harvested-after-at-most-k-steps
CONFIG: {"class": "Solution", "method": "maxTotalFruits", "paramOrder": ["fruits", "startPos", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2106 - Maximum Fruits Harvested After at Most K Steps
// https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

/**
 * @param {number[][]} fruits
 * @param {number} startPos
 * @param {number} k
 * @return {number}
 */
var maxTotalFruits = function(fruits, startPos, k) {
    const minSteps = (left, right, start) => {
        if (right <= start) return start - left;
        if (left >= start) return right - start;
        return Math.min((start - left) + (right - left), (right - start) + (right - left));
    };
    const n = fruits.length;
    const pref = new Array(n + 1).fill(0);
    const pos = new Array(n);
    for (let i = 0; i < n; i++) {
        pos[i] = fruits[i][0];
        pref[i + 1] = pref[i] + fruits[i][1];
    }
    let ans = 0, j = 0;
    for (let i = 0; i < n; i++) {
        while (j < n && minSteps(pos[i], pos[j], startPos) > k) j++;
        if (j <= i) ans = Math.max(ans, pref[i + 1] - pref[j]);
    }
    j = 0;
    for (let i = 0; i < n; i++) {
        while (j <= i && minSteps(pos[j], pos[i], startPos) > k) j++;
        ans = Math.max(ans, pref[i + 1] - pref[j]);
    }
    return ans;
};


===== 2107_number_of_unique_flavors_after_sharing_k_candies =====
TITLE: 2107. Number of Unique Flavors After Sharing K Candies
SLUG: number-of-unique-flavors-after-sharing-k-candies
CONFIG: {"class": "Solution", "method": "solve", "paramOrder": ["candies", "k"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2107 - Number of Unique Flavors After Sharing K Candies
// https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/

/**
 * @param {number[]} candies
 * @param {number} k
 * @return {number}
 */
var shareCandies = function(candies, k) {
    const n = candies.length;
    const freq = new Map();
    for (const c of candies) freq.set(c, (freq.get(c) || 0) + 1);
    if (k === 0) return freq.size;
    for (let i = 0; i < k; i++) {
        const c = candies[i];
        const v = freq.get(c) - 1;
        if (v === 0) freq.delete(c); else freq.set(c, v);
    }
    let ans = freq.size;
    for (let i = k; i < n; i++) {
        freq.set(candies[i - k], (freq.get(candies[i - k]) || 0) + 1);
        const c = candies[i];
        const v = freq.get(c) - 1;
        if (v === 0) freq.delete(c); else freq.set(c, v);
        ans = Math.max(ans, freq.size);
    }
    return ans;
};


===== 2108_find_first_palindromic_string_in_the_array =====
TITLE: 2108. Find First Palindromic String in the Array
SLUG: find-first-palindromic-string-in-the-array
CONFIG: {"class": "Solution", "method": "firstPalindrome", "paramOrder": ["words"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2108 - Find First Palindromic String in the Array
// https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

/**
 * @param {string[]} words
 * @return {string}
 */
var firstPalindrome = function(words) {
    for (const w of words) {
        let ok = true;
        for (let l = 0, r = w.length - 1; l < r; l++, r--)
            if (w[l] !== w[r]) { ok = false; break; }
        if (ok) return w;
    }
    return "";
};


===== 2109_adding_spaces_to_a_string =====
TITLE: 2109. Adding Spaces to a String
SLUG: adding-spaces-to-a-string
CONFIG: {"class": "Solution", "method": "addSpaces", "paramOrder": ["s", "spaces"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2109 - Adding Spaces to a String
// https://leetcode.com/problems/adding-spaces-to-a-string/

/**
 * @param {string} s
 * @param {number[]} spaces
 * @return {string}
 */
var addSpaces = function(s, spaces) {
    const b = [];
    let j = 0;
    for (let i = 0; i < s.length; i++) {
        if (j < spaces.length && spaces[j] === i) { b.push(' '); j++; }
        b.push(s[i]);
    }
    return b.join('');
};


===== 2110_number_of_smooth_descent_periods_of_a_stock =====
TITLE: 2110. Number of Smooth Descent Periods of a Stock
SLUG: number-of-smooth-descent-periods-of-a-stock
CONFIG: {"class": "Solution", "method": "getDescentPeriods", "paramOrder": ["prices"], "types": null, "description": "Update method name and add cases to cases.json when implementing the solution."}
---JS---
// LeetCode 2110 - Number of Smooth Descent Periods of a Stock
// https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

/**
 * @param {number[]} prices
 * @return {number}
 */
var getDescentPeriods = function(prices) {
    let ans = 1, cur = 1;
    for (let i = 1; i < prices.length; i++) {
        if (prices[i] === prices[i - 1] - 1) cur++;
        else cur = 1;
        ans += cur;
    }
    return ans;
};

