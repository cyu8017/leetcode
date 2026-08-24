from pathlib import Path

root = Path("/Users/cyu/Documents/Git/github-cyu8017/leetcode")
files = {}

files["2876_count_visited_nodes_in_a_directed_graph"] = '''# LeetCode 2876 - Count Visited Nodes in a Directed Graph
# https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

from typing import List


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        ans = [0] * n
        state = [0] * n
        stack = []

        def dfs(u: int) -> None:
            state[u] = 1
            stack.append(u)
            v = edges[u]
            if state[v] == 0:
                dfs(v)
            elif state[v] == 1:
                idx = len(stack) - 1
                while stack[idx] != v:
                    idx -= 1
                cyc = len(stack) - idx
                for i in range(idx, len(stack)):
                    ans[stack[i]] = cyc
            if ans[u] == 0:
                ans[u] = ans[edges[u]] + 1
            state[u] = 2
            stack.pop()

        for i in range(n):
            if state[i] == 0:
                dfs(i)
        return ans
'''

files["2877_create_a_dataframe_from_list"] = '''# LeetCode 2877 - Create a DataFrame from List
# https://leetcode.com/problems/create-a-dataframe-from-list/

from typing import Any, List


class Solution:
    def createDataframe(self, student_data: List[List[int]]) -> List[Any]:
        return [{"student_id": student_id, "age": age} for student_id, age in student_data]
'''

files["2878_get_the_size_of_a_dataframe"] = '''# LeetCode 2878 - Get the Size of a DataFrame
# https://leetcode.com/problems/get-the-size-of-a-dataframe/

from typing import Any, List


class Solution:
    def getDataframeSize(self, players: Any) -> List[int]:
        if not players:
            return [0, 0]
        rows = len(players)
        first = players[0]
        cols = len(first) if isinstance(first, list) else len(first.keys())
        return [rows, cols]
'''

files["2879_display_the_first_three_rows"] = '''# LeetCode 2879 - Display the First Three Rows
# https://leetcode.com/problems/display-the-first-three-rows/

from typing import Any, List


class Solution:
    def selectFirstRows(self, employees: List[Any]) -> List[Any]:
        return employees[:3]
'''

files["2880_select_data"] = '''# LeetCode 2880 - Select Data
# https://leetcode.com/problems/select-data/

from typing import Any, List


class Solution:
    def selectData(self, students: List[Any]) -> List[Any]:
        out = []
        for r in students:
            if (r[0] if isinstance(r, list) else r.get("student_id")) == 101:
                if isinstance(r, list):
                    out.append({"name": r[1], "age": r[2]})
                else:
                    out.append({"name": r["name"], "age": r["age"]})
        return out
'''

files["2881_create_a_new_column"] = '''# LeetCode 2881 - Create a New Column
# https://leetcode.com/problems/create-a-new-column/

from typing import Any, List


class Solution:
    def createBonusColumn(self, employees: List[Any]) -> List[Any]:
        out = []
        for r in employees:
            if isinstance(r, list):
                out.append({"name": r[0], "salary": r[1], "bonus": r[1] * 2})
            else:
                row = dict(r)
                row["bonus"] = r["salary"] * 2
                out.append(row)
        return out
'''

files["2882_drop_duplicate_rows"] = '''# LeetCode 2882 - Drop Duplicate Rows
# https://leetcode.com/problems/drop-duplicate-rows/

from typing import Any, List


class Solution:
    def dropDuplicateEmails(self, customers: List[Any]) -> List[Any]:
        seen = set()
        out = []
        for r in customers:
            email = r[2] if isinstance(r, list) else r["email"]
            if email in seen:
                continue
            seen.add(email)
            out.append(r)
        return out
'''

files["2883_drop_missing_data"] = '''# LeetCode 2883 - Drop Missing Data
# https://leetcode.com/problems/drop-missing-data/

from typing import Any, List


class Solution:
    def dropMissingData(self, students: List[Any]) -> List[Any]:
        out = []
        for r in students:
            name = r[1] if isinstance(r, list) else r.get("name")
            if name is not None and name != "":
                out.append(r)
        return out
'''

files["2884_modify_columns"] = '''# LeetCode 2884 - Modify Columns
# https://leetcode.com/problems/modify-columns/

from typing import Any, List


class Solution:
    def modifySalaryColumn(self, employees: List[Any]) -> List[Any]:
        out = []
        for r in employees:
            if isinstance(r, list):
                out.append([r[0], r[1] * 2])
            else:
                row = dict(r)
                row["salary"] = r["salary"] * 2
                out.append(row)
        return out
'''

files["2885_rename_columns"] = '''# LeetCode 2885 - Rename Columns
# https://leetcode.com/problems/rename-columns/

from typing import Any, List


class Solution:
    def renameColumns(self, students: List[Any]) -> List[Any]:
        out = []
        for r in students:
            if isinstance(r, list):
                out.append(
                    {
                        "student_id": r[0],
                        "first_name": r[1],
                        "last_name": r[2],
                        "age_in_years": r[3],
                    }
                )
            else:
                out.append(
                    {
                        "student_id": r["id"],
                        "first_name": r["first"],
                        "last_name": r["last"],
                        "age_in_years": r["age"],
                    }
                )
        return out
'''

files["2886_change_data_type"] = '''# LeetCode 2886 - Change Data Type
# https://leetcode.com/problems/change-data-type/

from typing import Any, List


class Solution:
    def changeDatatype(self, students: List[Any]) -> List[Any]:
        out = []
        for r in students:
            if isinstance(r, list):
                out.append([r[0], r[1], r[2], int(r[3])])
            else:
                row = dict(r)
                row["grade"] = int(r["grade"])
                out.append(row)
        return out
'''

files["2887_fill_missing_data"] = '''# LeetCode 2887 - Fill Missing Data
# https://leetcode.com/problems/fill-missing-data/

from typing import Any, List


class Solution:
    def fillMissingValues(self, products: List[Any]) -> List[Any]:
        out = []
        for r in products:
            if isinstance(r, list):
                q = r[1]
                out.append([r[0], 0 if q is None else q, r[2]])
            else:
                row = dict(r)
                row["quantity"] = 0 if r.get("quantity") is None else r["quantity"]
                out.append(row)
        return out
'''

files["2888_reshape_data_concatenate"] = '''# LeetCode 2888 - Reshape Data: Concatenate
# https://leetcode.com/problems/reshape-data-concatenate/

from typing import Any, List


class Solution:
    def concatenateTables(self, df1: List[Any], df2: List[Any]) -> List[Any]:
        return df1 + df2
'''

files["2889_reshape_data_pivot"] = '''# LeetCode 2889 - Reshape Data: Pivot
# https://leetcode.com/problems/reshape-data-pivot/

from typing import Any, List


class Solution:
    def pivotTable(self, weather: List[Any]) -> List[Any]:
        months = []
        by_month = {}
        for r in weather:
            if isinstance(r, list):
                city, month, temperature = r[0], r[1], r[2]
            else:
                city, month, temperature = r["city"], r["month"], r["temperature"]
            if month not in by_month:
                by_month[month] = {}
                months.append(month)
            by_month[month][city] = temperature
        return [{"month": month, **by_month[month]} for month in months]
'''

files["2890_reshape_data_melt"] = '''# LeetCode 2890 - Reshape Data: Melt
# https://leetcode.com/problems/reshape-data-melt/

from typing import Any, List


class Solution:
    def meltTable(self, report: List[Any]) -> List[Any]:
        out = []
        for r in report:
            if isinstance(r, list):
                product = r[0]
                for q in range(1, 5):
                    out.append({"product": product, "quarter": "quarter_" + str(q), "sales": r[q]})
            else:
                for q in ["quarter_1", "quarter_2", "quarter_3", "quarter_4"]:
                    out.append({"product": r["product"], "quarter": q, "sales": r[q]})
        return out
'''

files["2891_method_chaining"] = '''# LeetCode 2891 - Method Chaining
# https://leetcode.com/problems/method-chaining/

from typing import Any, List


class Solution:
    def findHeavyAnimals(self, animals: List[Any]) -> List[Any]:
        def weight(r: Any) -> int:
            return r[3] if isinstance(r, list) else r["weight"]

        filtered = [r for r in animals if weight(r) > 100]
        filtered.sort(key=weight, reverse=True)
        return [{"name": r[0] if isinstance(r, list) else r["name"]} for r in filtered]
'''

files["2892_minimizing_array_after_replacing_pairs_with_their_product"] = '''# LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
# https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

from typing import List


class Solution:
    def minArrayLength(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        ans = 1
        prod = nums[0]
        for i in range(1, len(nums)):
            if prod <= k and nums[i] <= k and (nums[i] == 0 or prod <= k // nums[i]):
                prod *= nums[i]
            else:
                ans += 1
                prod = nums[i]
        return ans
'''

files["2894_divisible_and_non_divisible_sums_difference"] = '''# LeetCode 2894 - Divisible and Non-divisible Sums Difference
# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = num2 = 0
        for i in range(1, n + 1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        return num1 - num2
'''

files["2895_minimum_processing_time"] = '''# LeetCode 2895 - Minimum Processing Time
# https://leetcode.com/problems/minimum-processing-time/

from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime = sorted(processorTime)
        tasks = sorted(tasks, reverse=True)
        ans = 0
        for i in range(len(processorTime)):
            fin = processorTime[i] + tasks[i * 4]
            if fin > ans:
                ans = fin
        return ans
'''

files["2896_apply_operations_to_make_two_strings_equal"] = '''# LeetCode 2896 - Apply Operations to Make Two Strings Equal
# https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        diff = [i for i in range(len(s1)) if s1[i] != s2[i]]
        m = len(diff)
        if m % 2 == 1:
            return -1
        if m == 0:
            return 0
        inf = 1 << 30
        dp2 = [inf] * (m + 1)
        dp2[0] = 0
        for i in range(m):
            if dp2[i] >= inf:
                continue
            if i + 1 < m:
                cand = diff[i + 1] - diff[i]
                if cand > x:
                    cand = x
                if dp2[i] + cand < dp2[i + 2]:
                    dp2[i + 2] = dp2[i] + cand
        return -1 if dp2[m] >= inf else dp2[m]
'''

written = 0
for folder, content in files.items():
    path = root / folder / "solution.py"
    path.write_text(content, encoding="utf-8", newline="\n")
    written += 1
    print("wrote", folder)
print("p2 written", written)
