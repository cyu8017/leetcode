class Solution:
    def alertNames(self, keyName, keyTime):
        from collections import defaultdict
        times = defaultdict(list)
        for name, t in zip(keyName, keyTime):
            h, m = map(int, t.split(":")); times[name].append(h * 60 + m)
        ans = []
        for name, a in times.items():
            a.sort()
            if any(a[i + 2] - a[i] <= 60 for i in range(len(a) - 2)): ans.append(name)
        return sorted(ans)
