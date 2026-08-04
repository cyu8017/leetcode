#!/usr/bin/env python3
"""Port JavaScript solutions for LeetCode problems 1423-1462 batch D."""
from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOLUTIONS: dict[str, str] = {
    "1423_maximum_points_you_can_obtain_from_cards": r'''var maxScore = function(cardPoints, k) {
    const n = cardPoints.length, total = cardPoints.reduce((a, b) => a + b, 0);
    if (k === n) return total;
    let sum = 0, smallest = Infinity;
    for (let i = 0; i < n - k; i++) sum += cardPoints[i];
    smallest = sum;
    for (let i = n - k; i < n; i++) { sum += cardPoints[i] - cardPoints[i - (n - k)]; smallest = Math.min(smallest, sum); }
    return total - smallest;
};
''',
    "1424_diagonal_traverse_ii": r'''var findDiagonalOrder = function(nums) {
    const diagonals = new Map(), answer = [];
    for (let r = 0; r < nums.length; r++) for (let c = 0; c < nums[r].length; c++) {
        const d = r + c; if (!diagonals.has(d)) diagonals.set(d, []); diagonals.get(d).push(nums[r][c]);
    }
    for (let d = 0; diagonals.has(d); d++) answer.push(...diagonals.get(d).reverse());
    return answer;
};
''',
    "1425_constrained_subsequence_sum": r'''var constrainedSubsetSum = function(nums, k) {
    const dp = Array(nums.length), deque = [];
    for (let i = 0; i < nums.length; i++) {
        while (deque.length && deque[0] < i - k) deque.shift();
        dp[i] = nums[i] + Math.max(0, deque.length ? dp[deque[0]] : 0);
        while (deque.length && dp[deque[deque.length - 1]] <= dp[i]) deque.pop();
        deque.push(i);
    }
    return Math.max(...dp);
};
''',
    "1426_counting_elements": r'''var countElements = function(arr) {
    const values = new Set(arr); return arr.reduce((count, x) => count + values.has(x + 1), 0);
};
''',
    "1427_perform_string_shifts": r'''var stringShift = function(s, shift) {
    let offset = 0;
    for (const [direction, amount] of shift) offset += direction === 0 ? -amount : amount;
    offset = ((offset % s.length) + s.length) % s.length;
    return s.slice(s.length - offset) + s.slice(0, s.length - offset);
};
''',
    "1428_leftmost_column_with_at_least_a_one": r'''var leftMostColumnWithOne = function(binaryMatrix) {
    const [rows, cols] = binaryMatrix.dimensions();
    let row = 0, col = cols - 1, answer = -1;
    while (row < rows && col >= 0) {
        if (binaryMatrix.get(row, col) === 1) { answer = col; col--; } else row++;
    }
    return answer;
};
''',
    "1429_first_unique_number": r'''var FirstUnique = function(nums) {
    this.count = new Map(); this.queue = [];
    for (const x of nums) this.add(x);
};
FirstUnique.prototype.showFirstUnique = function() {
    while (this.queue.length && this.count.get(this.queue[0]) > 1) this.queue.shift();
    return this.queue.length ? this.queue[0] : -1;
};
FirstUnique.prototype.add = function(value) {
    this.count.set(value, (this.count.get(value) || 0) + 1);
    if (this.count.get(value) === 1) this.queue.push(value);
};
''',
    "1430_check_if_a_string_is_a_valid_sequence_from_root_to_leaves_path_in_a_binary_tree": r'''var isValidSequence = function(root, arr) {
    const dfs = (node, i) => node && node.val === arr[i] && (i === arr.length - 1 ? !node.left && !node.right : dfs(node.left, i + 1) || dfs(node.right, i + 1));
    return Boolean(dfs(root, 0));
};
''',
    "1431_kids_with_the_greatest_number_of_candies": r'''var kidsWithCandies = function(candies, extraCandies) {
    const maximum = Math.max(...candies); return candies.map((x) => x + extraCandies >= maximum);
};
''',
    "1432_max_difference_you_can_get_from_changing_an_integer": r'''var maxDiff = function(num) {
    const s = String(num);
    const maximum = Number(s.replace(new RegExp((s.match(/[0-8]/) || [""])[0], "g"), "9"));
    let target = s[0] === "1" ? [...s].find((x) => x !== "0" && x !== "1") : s[0];
    const minimum = target ? Number(s.replace(new RegExp(target, "g"), s[0] === target ? "1" : "0")) : num;
    return maximum - minimum;
};
''',
    "1433_check_if_a_string_can_break_another_string": r'''var checkIfCanBreak = function(s1, s2) {
    const a = [...s1].sort(), b = [...s2].sort(); let ab = true, ba = true;
    for (let i = 0; i < a.length; i++) { if (a[i] < b[i]) ab = false; if (b[i] < a[i]) ba = false; }
    return ab || ba;
};
''',
    "1434_number_of_ways_to_wear_different_hats_to_each_other": r'''var numberWays = function(hats) {
    const mod = 1000000007, n = hats.length, owners = Array.from({length: 41}, () => []);
    hats.forEach((list, person) => list.forEach((hat) => owners[hat].push(person)));
    const memo = new Map();
    const dfs = (hat, mask) => {
        if (mask === (1 << n) - 1) return 1;
        if (hat > 40) return 0;
        const key = hat + "," + mask; if (memo.has(key)) return memo.get(key);
        let ways = dfs(hat + 1, mask);
        for (const person of owners[hat]) if (!(mask & (1 << person))) ways = (ways + dfs(hat + 1, mask | (1 << person))) % mod;
        memo.set(key, ways); return ways;
    };
    return dfs(1, 0);
};
''',
    "1436_destination_city": r'''var destCity = function(paths) {
    const starts = new Set(paths.map((path) => path[0])); return paths.find((path) => !starts.has(path[1]))[1];
};
''',
    "1437_check_if_all_1s_are_at_least_length_k_places_away": r'''var kLengthApart = function(nums, k) {
    let previous = -k - 1;
    for (let i = 0; i < nums.length; i++) if (nums[i]) { if (i - previous <= k) return false; previous = i; }
    return true;
};
''',
    "1438_longest_continuous_subarray_with_absolute_diff_less_than_or_equal_to_limit": r'''var longestSubarray = function(nums, limit) {
    const minq = [], maxq = []; let left = 0, answer = 0;
    for (let right = 0; right < nums.length; right++) {
        while (minq.length && nums[minq[minq.length - 1]] > nums[right]) minq.pop(); minq.push(right);
        while (maxq.length && nums[maxq[maxq.length - 1]] < nums[right]) maxq.pop(); maxq.push(right);
        while (nums[maxq[0]] - nums[minq[0]] > limit) { if (minq[0] === left) minq.shift(); if (maxq[0] === left) maxq.shift(); left++; }
        answer = Math.max(answer, right - left + 1);
    } return answer;
};
''',
    "1439_find_the_kth_smallest_sum_of_a_matrix_with_sorted_rows": r'''var kthSmallest = function(mat, k) {
    let sums = [0];
    for (const row of mat) {
        const next = []; for (const sum of sums) for (const value of row) next.push(sum + value);
        next.sort((a, b) => a - b); sums = next.slice(0, k);
    } return sums[k - 1];
};
''',
    "1441_build_an_array_with_stack_operations": r'''var buildArray = function(target, n) {
    const answer = []; let value = 1;
    for (const wanted of target) { while (value < wanted) { answer.push("Push", "Pop"); value++; } answer.push("Push"); value++; }
    return answer;
};
''',
    "1442_count_triplets_that_can_form_two_arrays_of_equal_xor": r'''var countTriplets = function(arr) {
    let answer = 0, xor = 0; const count = new Map([[0, 1]]), indices = new Map([[0, 0]]);
    for (let i = 0; i < arr.length; i++) { xor ^= arr[i]; answer += (count.get(xor) || 0) * i - (indices.get(xor) || 0); count.set(xor, (count.get(xor) || 0) + 1); indices.set(xor, (indices.get(xor) || 0) + i + 1); }
    return answer;
};
''',
    "1443_minimum_time_to_collect_all_apples_in_a_tree": r'''var minTime = function(n, edges, hasApple) {
    const graph = Array.from({length: n}, () => []); for (const [a, b] of edges) { graph[a].push(b); graph[b].push(a); }
    const dfs = (node, parent) => { let time = 0; for (const child of graph[node]) if (child !== parent) { const childTime = dfs(child, node); if (childTime || hasApple[child]) time += childTime + 2; } return time; };
    return dfs(0, -1);
};
''',
    "1444_number_of_ways_of_cutting_a_pizza": r'''var ways = function(pizza, k) {
    const mod = 1000000007, m = pizza.length, n = pizza[0].length, apples = Array.from({length:m+1}, () => Array(n+1).fill(0));
    for (let r = m - 1; r >= 0; r--) for (let c = n - 1; c >= 0; c--) apples[r][c] = (pizza[r][c] === "A") + apples[r+1][c] + apples[r][c+1] - apples[r+1][c+1];
    const memo = new Map(), dfs = (r, c, cuts) => { if (apples[r][c] === 0) return 0; if (cuts === 1) return 1; const key = r+","+c+","+cuts; if (memo.has(key)) return memo.get(key); let result = 0; for (let x=r+1;x<m;x++) if (apples[r][c]-apples[x][c]>0) result=(result+dfs(x,c,cuts-1))%mod; for (let y=c+1;y<n;y++) if(apples[r][c]-apples[r][y]>0) result=(result+dfs(r,y,cuts-1))%mod; memo.set(key,result); return result; };
    return dfs(0, 0, k);
};
''',
    "1446_consecutive_characters": r'''var maxPower = function(s) { let best = 0, run = 0, previous = ""; for (const ch of s) { run = ch === previous ? run + 1 : 1; previous = ch; best = Math.max(best, run); } return best; };
''',
    "1447_simplified_fractions": r'''var simplifiedFractions = function(n) { const gcd = (a,b) => b ? gcd(b,a%b) : a, answer=[]; for(let d=2;d<=n;d++) for(let x=1;x<d;x++) if(gcd(x,d)===1) answer.push(x+"/"+d); return answer; };
''',
    "1448_count_good_nodes_in_binary_tree": r'''var goodNodes = function(root) { const dfs = (node, maximum) => !node ? 0 : (node.val >= maximum ? 1 : 0) + dfs(node.left, Math.max(maximum,node.val)) + dfs(node.right, Math.max(maximum,node.val)); return dfs(root, -Infinity); };
''',
    "1449_form_largest_integer_with_digits_that_add_up_to_target": r'''var largestNumber = function(cost, target) { const dp=Array(target+1).fill(null); dp[0]=""; for(let t=1;t<=target;t++) for(let d=1;d<=9;d++) if(t>=cost[d-1]&&dp[t-cost[d-1]]!==null){const s=String(d)+dp[t-cost[d-1]]; if(dp[t]===null||s.length>dp[t].length||(s.length===dp[t].length&&s>dp[t])) dp[t]=s;} return dp[target]||"0"; };
''',
    "1450_number_of_students_doing_homework_at_a_given_time": r'''var busyStudent = function(startTime, endTime, queryTime) { return startTime.reduce((answer,start,i)=>answer+(start<=queryTime&&queryTime<=endTime[i]),0); };
''',
    "1451_rearrange_words_in_a_sentence": r'''var arrangeWords = function(text) { const words=text.toLowerCase().split(" ").map((word,index)=>[word,index]); words.sort((a,b)=>a[0].length-b[0].length||a[1]-b[1]); const result=words.map(x=>x[0]).join(" "); return result[0].toUpperCase()+result.slice(1); };
''',
    "1452_people_whose_list_of_favorite_companies_is_not_a_subset_of_another_list": r'''var peopleIndexes = function(favoriteCompanies) { const sets=favoriteCompanies.map(x=>new Set(x)); return sets.map((set,i)=>sets.every((other,j)=>i===j||set.size>other.size||[...set].some(x=>!other.has(x)))?i:-1).filter(i=>i>=0); };
''',
    "1453_maximum_number_of_darts_inside_of_a_circular_dartboard": r'''var numPoints = function(darts, r) { let best=1, rr=2*r; for(let i=0;i<darts.length;i++) for(let j=i;j<darts.length;j++){const dx=darts[j][0]-darts[i][0],dy=darts[j][1]-darts[i][1],d=Math.hypot(dx,dy); if(d>rr+1e-8) continue; const mx=(darts[i][0]+darts[j][0])/2,my=(darts[i][1]+darts[j][1])/2,h=Math.sqrt(Math.max(0,r*r-d*d/4)),ux=-dy/d||0,uy=dx/d||0; for(const sign of [-1,1]){const x=mx+sign*h*ux,y=my+sign*h*uy; best=Math.max(best,darts.reduce((c,p)=>c+(Math.hypot(p[0]-x,p[1]-y)<=r+1e-7),0));}} return best; };
''',
    "1455_check_if_a_word_occurs_as_a_prefix_of_any_word_in_a_sentence": r'''var isPrefixOfWord = function(sentence, searchWord) { const words=sentence.split(" "); for(let i=0;i<words.length;i++) if(words[i].startsWith(searchWord)) return i+1; return -1; };
''',
    "1456_maximum_number_of_vowels_in_a_substring_of_given_length": r'''var maxVowels = function(s, k) { const vowels=new Set("aeiou"); let count=0,best=0; for(let i=0;i<s.length;i++){if(vowels.has(s[i]))count++; if(i>=k&&vowels.has(s[i-k]))count--; if(i>=k-1)best=Math.max(best,count);} return best; };
''',
    "1457_pseudo_palindromic_paths_in_a_binary_tree": r'''var pseudoPalindromicPaths = function(root) { const dfs=(node,mask)=>{if(!node)return 0; mask^=1<<node.val; return !node.left&&!node.right ? ((mask&(mask-1))===0?1:0) : dfs(node.left,mask)+dfs(node.right,mask);}; return dfs(root,0); };
''',
    "1458_max_dot_product_of_two_subsequences": r'''var maxDotProduct = function(nums1, nums2) { const m=nums1.length,n=nums2.length,dp=Array.from({length:m+1},()=>Array(n+1).fill(-Infinity)); for(let i=1;i<=m;i++)for(let j=1;j<=n;j++){const product=nums1[i-1]*nums2[j-1]; dp[i][j]=Math.max(product,product+Math.max(0,dp[i-1][j-1]),dp[i-1][j],dp[i][j-1]);} return dp[m][n]; };
''',
    "1460_make_two_arrays_equal_by_reversing_subarrays": r'''var canBeEqual = function(target, arr) { const count=new Map(); for(const x of target)count.set(x,(count.get(x)||0)+1); for(const x of arr){if(!count.has(x))return false; count.set(x,count.get(x)-1); if(count.get(x)===0)count.delete(x);} return count.size===0; };
''',
    "1461_check_if_a_string_contains_all_binary_codes_of_size_k": r'''var hasAllCodes = function(s, k) { const seen=new Set(); for(let i=0;i+k<=s.length;i++)seen.add(s.slice(i,i+k)); return seen.size===(1<<k); };
''',
    "1462_course_schedule_iv": r'''var checkIfPrerequisite = function(numCourses, prerequisites, queries) { const reach=Array.from({length:numCourses},()=>Array(numCourses).fill(false)); for(const [a,b] of prerequisites)reach[a][b]=true; for(let k=0;k<numCourses;k++)for(let i=0;i<numCourses;i++)if(reach[i][k])for(let j=0;j<numCourses;j++)reach[i][j]=reach[i][j]||reach[k][j]; return queries.map(([a,b])=>reach[a][b]); };
''',
}


def main() -> None:
    written = 0
    failures: list[str] = []
    for folder, content in SOLUTIONS.items():
        path = os.path.join(ROOT, folder, "solution.js")
        try:
            with open(path, "w", encoding="utf-8", newline="\n") as file:
                file.write(content)
            written += 1
            print(f"wrote {folder}")
        except OSError as error:
            failures.append(f"{folder}: {error}")
            print(f"failed {folder}: {error}")
    print(f"done: {written} written, {len(failures)} failures")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
