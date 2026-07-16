from typing import List, Optional

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used, ans = {}, []
        for name in names:
            if name not in used:
                candidate = name
            else:
                k = used[name]
                while f"{name}({k})" in used:
                    k += 1
                candidate = f"{name}({k})"
                used[name] = k + 1
            used[candidate] = 1
            ans.append(candidate)
        return ans
