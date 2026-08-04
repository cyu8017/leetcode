"""Port selected LeetCode reference solutions to JavaScript."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FOLDERS = {
    "1382_balance_a_binary_search_tree": r"""var balanceBST = function(root) {
    const values = [];
    const collect = node => { if (node) { collect(node.left); values.push(node.val); collect(node.right); } };
    const build = (left, right) => {
        if (left > right) return null;
        const mid = Math.floor((left + right) / 2);
        const node = new TreeNode(values[mid]);
        node.left = build(left, mid - 1);
        node.right = build(mid + 1, right);
        return node;
    };
    collect(root);
    return build(0, values.length - 1);
};""",
    "1383_maximum_performance_of_a_team": r"""var maxPerformance = function(n, speed, efficiency, k) {
    const engineers = speed.map((s, i) => [efficiency[i], s]).sort((a, b) => b[0] - a[0]);
    const heap = [];
    const push = value => { heap.push(value); let i = heap.length - 1; while (i) { const p = (i - 1) >> 1; if (heap[p] <= value) break; heap[i] = heap[p]; i = p; } heap[i] = value; };
    const pop = () => { const result = heap[0], value = heap.pop(); if (heap.length) { let i = 0; while (i * 2 + 1 < heap.length) { let c = i * 2 + 1; if (c + 1 < heap.length && heap[c + 1] < heap[c]) c++; if (heap[c] >= value) break; heap[i] = heap[c]; i = c; } heap[i] = value; } return result; };
    let sum = 0n, best = 0n;
    for (const [e, s] of engineers) {
        push(s); sum += BigInt(s);
        if (heap.length > k) sum -= BigInt(pop());
        const performance = sum * BigInt(e);
        if (performance > best) best = performance;
    }
    return Number(best % 1000000007n);
};""",
    "1385_find_the_distance_value_between_two_arrays": r"""var findTheDistanceValue = function(arr1, arr2, d) {
    arr2.sort((a, b) => a - b);
    return arr1.filter(value => {
        let left = 0, right = arr2.length;
        while (left < right) { const mid = (left + right) >> 1; if (arr2[mid] < value) left = mid + 1; else right = mid; }
        return (left === arr2.length || Math.abs(arr2[left] - value) > d) && (left === 0 || Math.abs(arr2[left - 1] - value) > d);
    }).length;
};""",
    "1386_cinema_seat_allocation": r"""var maxNumberOfFamilies = function(n, reservedSeats) {
    const reserved = new Map();
    for (const [row, seat] of reservedSeats) reserved.set(row, (reserved.get(row) || 0) | (1 << seat));
    let families = 2 * (n - reserved.size);
    for (const mask of reserved.values()) {
        const left = 0b0000011110, middle = 0b0111100000, right = 0b1111000000;
        if ((mask & left) === 0 && (mask & right) === 0) families += 2;
        else if ((mask & left) === 0 || (mask & middle) === 0 || (mask & right) === 0) families++;
    }
    return families;
};""",
    "1387_sort_integers_by_the_power_value": r"""var getKth = function(lo, hi, k) {
    const memo = new Map([[1, 0]]);
    const power = value => {
        if (!memo.has(value)) memo.set(value, 1 + power(value % 2 ? 3 * value + 1 : value / 2));
        return memo.get(value);
    };
    return Array.from({ length: hi - lo + 1 }, (_, i) => lo + i).sort((a, b) => power(a) - power(b) || a - b)[k - 1];
};""",
    "1388_pizza_with_3n_slices": r"""var maxSizeSlices = function(slices) {
    const solve = array => {
        const picks = Math.floor(slices.length / 3);
        let previous = Array(picks + 1).fill(0), current = Array(picks + 1).fill(0);
        for (let i = 1; i <= array.length; i++) {
            const next = Array(picks + 1).fill(0);
            for (let j = 1; j <= Math.min(picks, Math.ceil(i / 2)); j++) next[j] = Math.max(current[j], previous[j - 1] + array[i - 1]);
            previous = current; current = next;
        }
        return current[picks];
    };
    return Math.max(solve(slices.slice(1)), solve(slices.slice(0, -1)));
};""",
    "1389_create_target_array_in_the_given_order": r"""var createTargetArray = function(nums, index) {
    const target = [];
    for (let i = 0; i < nums.length; i++) target.splice(index[i], 0, nums[i]);
    return target;
};""",
    "1390_four_divisors": r"""var sumFourDivisors = function(nums) {
    let total = 0;
    for (const value of nums) {
        let count = 0, sum = 0;
        for (let divisor = 1; divisor * divisor <= value; divisor++) if (value % divisor === 0) {
            count++; sum += divisor;
            if (divisor * divisor !== value) { count++; sum += value / divisor; }
        }
        if (count === 4) total += sum;
    }
    return total;
};""",
    "1391_check_if_there_is_a_valid_path_in_a_grid": r"""var hasValidPath = function(grid) {
    const connections = [[], [[0, -1], [0, 1]], [[-1, 0], [1, 0]], [[0, -1], [1, 0]], [[0, 1], [1, 0]], [[0, -1], [-1, 0]], [[0, 1], [-1, 0]]];
    const rows = grid.length, cols = grid[0].length, queue = [[0, 0]], seen = new Set(["0,0"]);
    for (let head = 0; head < queue.length; head++) {
        const [r, c] = queue[head];
        if (r === rows - 1 && c === cols - 1) return true;
        for (const [dr, dc] of connections[grid[r][c]]) {
            const nr = r + dr, nc = c + dc, key = `${nr},${nc}`;
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || seen.has(key)) continue;
            if (connections[grid[nr][nc]].some(([rr, cc]) => rr === -dr && cc === -dc)) { seen.add(key); queue.push([nr, nc]); }
        }
    }
    return false;
};""",
    "1392_longest_happy_prefix": r"""var longestPrefix = function(s) {
    const lps = Array(s.length).fill(0);
    for (let i = 1, length = 0; i < s.length;) {
        if (s[i] === s[length]) lps[i++] = ++length;
        else if (length) length = lps[length - 1];
        else i++;
    }
    return s.slice(0, lps[s.length - 1]);
};""",
    "1394_find_lucky_integer_in_an_array": r"""var findLucky = function(arr) {
    const count = new Map();
    for (const value of arr) count.set(value, (count.get(value) || 0) + 1);
    let answer = -1;
    for (const [value, frequency] of count) if (value === frequency) answer = Math.max(answer, value);
    return answer;
};""",
    "1395_count_number_of_teams": r"""var numTeams = function(rating) {
    let teams = 0;
    for (let j = 0; j < rating.length; j++) {
        let lowerLeft = 0, higherLeft = 0, lowerRight = 0, higherRight = 0;
        for (let i = 0; i < j; i++) rating[i] < rating[j] ? lowerLeft++ : higherLeft++;
        for (let k = j + 1; k < rating.length; k++) rating[k] < rating[j] ? lowerRight++ : higherRight++;
        teams += lowerLeft * higherRight + higherLeft * lowerRight;
    }
    return teams;
};""",
    "1396_design_underground_system": r"""var UndergroundSystem = function() {
    this.checkIns = new Map();
    this.routes = new Map();
};

UndergroundSystem.prototype.checkIn = function(id, stationName, t) {
    this.checkIns.set(id, [stationName, t]);
};

UndergroundSystem.prototype.checkOut = function(id, stationName, t) {
    const [start, time] = this.checkIns.get(id), key = `${start}|${stationName}`;
    const [total, count] = this.routes.get(key) || [0, 0];
    this.routes.set(key, [total + t - time, count + 1]);
    this.checkIns.delete(id);
};

UndergroundSystem.prototype.getAverageTime = function(startStation, endStation) {
    const [total, count] = this.routes.get(`${startStation}|${endStation}`);
    return total / count;
};""",
    "1397_find_all_good_strings": r"""var findGoodStrings = function(n, s1, s2, evil) {
    const mod = 1000000007, m = evil.length, lps = Array(m).fill(0);
    for (let i = 1, j = 0; i < m;) if (evil[i] === evil[j]) lps[i++] = ++j; else if (j) j = lps[j - 1]; else i++;
    const next = (matched, ch) => { while (matched && evil[matched] !== ch) matched = lps[matched - 1]; return evil[matched] === ch ? matched + 1 : 0; };
    const count = bound => {
        const memo = new Map();
        const dfs = (pos, matched, tight) => {
            if (matched === m) return 0;
            if (pos === n) return 1;
            const key = `${pos},${matched},${tight}`;
            if (!tight && memo.has(key)) return memo.get(key);
            let result = 0, limit = tight ? bound.charCodeAt(pos) : 122;
            for (let code = 97; code <= limit; code++) result = (result + dfs(pos + 1, next(matched, String.fromCharCode(code)), tight && code === limit)) % mod;
            if (!tight) memo.set(key, result);
            return result;
        };
        return dfs(0, 0, true);
    };
    const decrement = value => { const chars = value.split(""); for (let i = chars.length - 1; i >= 0; i--) { if (chars[i] > "a") { chars[i] = String.fromCharCode(chars[i].charCodeAt(0) - 1); return chars.join(""); } chars[i] = "z"; } return ""; };
    return (count(s2) - (s1 ? count(decrement(s1)) : 0) + mod) % mod;
};""",
    "1399_count_largest_group": r"""var countLargestGroup = function(n) {
    const count = new Map();
    for (let value = 1; value <= n; value++) {
        let sum = 0, number = value;
        while (number) { sum += number % 10; number = Math.floor(number / 10); }
        count.set(sum, (count.get(sum) || 0) + 1);
    }
    const largest = Math.max(...count.values());
    return [...count.values()].filter(size => size === largest).length;
};""",
    "1400_construct_k_palindrome_strings": r"""var canConstruct = function(s, k) {
    if (s.length < k) return false;
    const count = Array(26).fill(0);
    for (const ch of s) count[ch.charCodeAt(0) - 97]++;
    return count.filter(value => value % 2).length <= k;
};""",
    "1401_circle_and_rectangle_overlapping": r"""var checkOverlap = function(radius, xCenter, yCenter, x1, y1, x2, y2) {
    const x = Math.max(x1, Math.min(xCenter, x2)), y = Math.max(y1, Math.min(yCenter, y2));
    return (x - xCenter) ** 2 + (y - yCenter) ** 2 <= radius ** 2;
};""",
    "1402_reducing_dishes": r"""var maxSatisfaction = function(satisfaction) {
    satisfaction.sort((a, b) => b - a);
    let prefix = 0, answer = 0;
    for (const value of satisfaction) { prefix += value; if (prefix <= 0) break; answer += prefix; }
    return answer;
};""",
    "1403_minimum_subsequence_in_non_increasing_order": r"""var minSubsequence = function(nums) {
    nums.sort((a, b) => b - a);
    const total = nums.reduce((sum, value) => sum + value, 0), result = [];
    let selected = 0;
    for (const value of nums) { selected += value; result.push(value); if (selected > total - selected) break; }
    return result;
};""",
    "1404_number_of_steps_to_reduce_a_number_in_binary_representation_to_one": r"""var numSteps = function(s) {
    let steps = 0, carry = 0;
    for (let i = s.length - 1; i > 0; i--) {
        const bit = Number(s[i]) + carry;
        if (bit === 1) { steps += 2; carry = 1; } else steps++;
    }
    return steps + carry;
};""",
    "1405_longest_happy_string": r"""var longestDiverseString = function(a, b, c) {
    const counts = [["a", a], ["b", b], ["c", c]], result = [];
    while (true) {
        counts.sort((x, y) => y[1] - x[1]);
        const [ch, count] = counts[0];
        if (!count) break;
        if (result.length >= 2 && result.at(-1) === ch && result.at(-2) === ch) {
            if (!counts[1][1]) break;
            result.push(counts[1][0]); counts[1][1]--;
        } else { result.push(ch); counts[0][1]--; }
    }
    return result.join("");
};""",
    "1406_stone_game_iii": r"""var stoneGameIII = function(stoneValue) {
    const dp = Array(stoneValue.length + 1).fill(0);
    for (let i = stoneValue.length - 1; i >= 0; i--) {
        let sum = 0; dp[i] = -Infinity;
        for (let take = 1; take <= 3 && i + take <= stoneValue.length; take++) { sum += stoneValue[i + take - 1]; dp[i] = Math.max(dp[i], sum - dp[i + take]); }
    }
    return dp[0] > 0 ? "Alice" : dp[0] < 0 ? "Bob" : "Tie";
};""",
    "1408_string_matching_in_an_array": r"""var stringMatching = function(words) {
    return words.filter((word, i) => words.some((other, j) => i !== j && other.includes(word)));
};""",
    "1409_queries_on_a_permutation_with_key": r"""var processQueries = function(queries, m) {
    const permutation = Array.from({ length: m }, (_, i) => i + 1);
    return queries.map(query => { const index = permutation.indexOf(query); permutation.splice(index, 1); permutation.unshift(query); return index; });
};""",
    "1410_html_entity_parser": r"""var entityParser = function(text) {
    const entities = {"&quot;": '"', "&apos;": "'", "&amp;": "&", "&gt;": ">", "&lt;": "<", "&frasl;": "/"};
    return text.replace(/&quot;|&apos;|&amp;|&gt;|&lt;|&frasl;/g, match => entities[match]);
};""",
    "1411_number_of_ways_to_paint_n_3_grid": r"""var numOfWays = function(n) {
    const mod = 1000000007;
    let two = 6, three = 6;
    for (let row = 2; row <= n; row++) [two, three] = [(3 * two + 2 * three) % mod, (2 * two + 2 * three) % mod];
    return (two + three) % mod;
};""",
    "1413_minimum_value_to_get_positive_step_by_step_sum": r"""var minStartValue = function(nums) {
    let sum = 0, minimum = 0;
    for (const value of nums) { sum += value; minimum = Math.min(minimum, sum); }
    return 1 - minimum;
};""",
    "1414_find_the_minimum_number_of_fibonacci_numbers_whose_sum_is_k": r"""var findMinFibonacciNumbers = function(k) {
    const fib = [1, 1];
    while (fib.at(-1) < k) fib.push(fib.at(-1) + fib.at(-2));
    let count = 0;
    for (let i = fib.length - 1; i >= 0 && k; i--) if (fib[i] <= k) { k -= fib[i]; count++; }
    return count;
};""",
    "1415_the_k_th_lexicographical_string_of_all_happy_strings_of_length_n": r"""var getHappyString = function(n, k) {
    const build = (prefix, remaining) => {
        if (!remaining) { if (--k === 0) return prefix; return ""; }
        for (const ch of "abc") if (ch !== prefix.at(-1)) { const answer = build(prefix + ch, remaining - 1); if (answer) return answer; }
        return "";
    };
    return build("", n);
};""",
    "1416_restore_the_array": r"""var numberOfArrays = function(s, k) {
    const mod = 1000000007, dp = Array(s.length + 1).fill(0);
    dp[0] = 1;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === "0") continue;
        let value = 0;
        for (let j = i; j < s.length; j++) { value = value * 10 + Number(s[j]); if (value > k) break; dp[j + 1] = (dp[j + 1] + dp[i]) % mod; }
    }
    return dp[s.length];
};""",
    "1417_reformat_the_string": r"""var reformat = function(s) {
    const letters = [], digits = [];
    for (const ch of s) (/[a-z]/.test(ch) ? letters : digits).push(ch);
    if (Math.abs(letters.length - digits.length) > 1) return "";
    const first = letters.length >= digits.length ? letters : digits, second = first === letters ? digits : letters;
    let answer = "";
    for (let i = 0; i < first.length; i++) { answer += first[i]; if (i < second.length) answer += second[i]; }
    return answer;
};""",
    "1418_display_table_of_food_orders_in_a_restaurant": r"""var displayTable = function(orders) {
    const foods = new Set(), tables = new Map();
    for (const [, table, food] of orders) { foods.add(food); if (!tables.has(table)) tables.set(table, new Map()); const row = tables.get(table); row.set(food, (row.get(food) || 0) + 1); }
    const menu = [...foods].sort(), result = [["Table", ...menu]];
    for (const table of [...tables.keys()].sort((a, b) => Number(a) - Number(b))) result.push([table, ...menu.map(food => String(tables.get(table).get(food) || 0))]);
    return result;
};""",
    "1419_minimum_number_of_frogs_croaking": r"""var minNumberOfFrogs = function(croakOfFrogs) {
    const order = "croak", count = Array(5).fill(0);
    let active = 0, maximum = 0;
    for (const ch of croakOfFrogs) {
        const index = order.indexOf(ch);
        if (index === 0) { count[0]++; active++; maximum = Math.max(maximum, active); }
        else { if (count[index - 1] === 0) return -1; count[index - 1]--; if (index === 4) active--; else count[index]++; }
    }
    return active === 0 ? maximum : -1;
};""",
    "1420_build_array_where_you_can_find_the_maximum_exactly_k_comparisons": r"""var numOfArrays = function(n, m, k) {
    const mod = 1000000007;
    let dp = Array.from({ length: m + 1 }, () => Array(k + 1).fill(0));
    for (let max = 1; max <= m; max++) dp[max][1] = 1;
    for (let length = 2; length <= n; length++) {
        const next = Array.from({ length: m + 1 }, () => Array(k + 1).fill(0));
        for (let max = 1; max <= m; max++) for (let cost = 1; cost <= k; cost++) {
            next[max][cost] = (next[max][cost] + dp[max][cost] * max) % mod;
            for (let previous = 1; previous < max; previous++) next[max][cost] = (next[max][cost] + dp[previous][cost - 1]) % mod;
        }
        dp = next;
    }
    return dp.reduce((sum, row) => (sum + row[k]) % mod, 0);
};""",
    "1422_maximum_score_after_splitting_a_string": r"""var maxScore = function(s) {
    let ones = [...s].filter(ch => ch === "1").length, zeros = 0, best = 0;
    for (let i = 0; i < s.length - 1; i++) { if (s[i] === "0") zeros++; else ones--; best = Math.max(best, zeros + ones); }
    return best;
};""",
}


def main():
    written, failures = [], []
    for folder, implementation in FOLDERS.items():
        directory = ROOT / folder
        try:
            # Confirm a reference exists before porting; Python is preferred.
            references = [directory / "solution.py", directory / "Solution.java", directory / "solution.go"]
            reference = next(path for path in references if path.exists())
            reference.read_text(encoding="utf-8")
            number, title = folder.split("_", 1)
            header = f"// LeetCode {number}: {title.replace('_', ' ').title()}\n\n"
            (directory / "solution.js").write_text(header + implementation + "\n", encoding="utf-8")
            written.append(folder)
        except Exception as error:
            failures.append(f"{folder}: {error}")
    print(f"Written: {len(written)}")
    print("Folders written:")
    print("\n".join(written))
    if failures:
        print("Failures:")
        print("\n".join(failures))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
